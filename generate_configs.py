#!/usr/bin/env python3
import yaml
import os
from copy import deepcopy
from pathlib import Path

def parse_page_audiences(file_path):
    """Extract audiences from page frontmatter"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return None
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None
        
        frontmatter = yaml.safe_load(parts[1])
        audiences = frontmatter.get('audiences')
        
        if isinstance(audiences, str):
            return [x.strip() for x in audiences.split(',')]
        elif isinstance(audiences, list):
            return audiences
        return None
    except (yaml.YAMLError, FileNotFoundError, UnicodeDecodeError):
        return None

def should_include_page(page_audiences, build_audience):
    """
    Determine if page should be included based on new access logic:
    - Internal: sees everything
    - Partner: sees only partner-tagged content
    - Beta: sees only beta-tagged content
    - Public: sees only untagged content
    """
    if build_audience == 'internal':
        return True  # Internal sees everything
    
    if page_audiences is None:
        # Page has no audience tags - only show in public
        return build_audience == 'public'
    
    # For specific audiences, only show if build matches page audience
    return build_audience in page_audiences

def filter_navigation(nav_item, audience, level=0):
    """Recursively filter navigation based on new access logic"""
    indent = "  " * level
    
    if isinstance(nav_item, dict):
        filtered_nav = {}
        for key, value in nav_item.items():
            if isinstance(value, str):  # It's a page
                page_path = f"docs/{value}"
                page_audiences = parse_page_audiences(page_path)
                
                if should_include_page(page_audiences, audience):
                    filtered_nav[key] = value
                    if page_audiences is None:
                        print(f"{indent}✅ Including '{key}' (untagged)")
                    else:
                        print(f"{indent}✅ Including '{key}' (audiences: {page_audiences})")
                else:
                    if page_audiences is None:
                        print(f"{indent}❌ Skipping '{key}' (untagged, not public)")
                    else:
                        print(f"{indent}❌ Skipping '{key}' (requires: {page_audiences})")
                    
            elif isinstance(value, list):  # It's a section
                print(f"{indent}📁 Processing section '{key}':")
                filtered_section = []
                for item in value:
                    filtered_item = filter_navigation(item, audience, level + 1)
                    if filtered_item:
                        filtered_section.append(filtered_item)
                
                if filtered_section:
                    filtered_nav[key] = filtered_section
                    print(f"{indent}✅ Section '{key}' included ({len(filtered_section)} items)")
                else:
                    print(f"{indent}❌ Section '{key}' excluded (no accessible content)")
        
        return filtered_nav if filtered_nav else None
    
    return nav_item

def create_audience_config(base_config, audience):
    """Create config for specific audience"""
    print(f"\n🔧 Creating {audience} configuration...")
    
    config = deepcopy(base_config)
    
    # Keep original site name for all builds - template handles visual indicator
    config["site_name"] = base_config.get('site_name', 'Documentation')
    
    # Set audience flags
    config["extra"] = config.get("extra", {})
    
    if audience == 'public':
        # Ensure all audience flags are False for public
        config["extra"]["audience_internal"] = False
        config["extra"]["audience_partner"] = False
        config["extra"]["audience_beta"] = False
    else:
        # Set the appropriate audience flag to True
        config["extra"]["audience_internal"] = (audience == 'internal')
        config["extra"]["audience_partner"] = (audience == 'partner')
        config["extra"]["audience_beta"] = (audience == 'beta')
    
    # Filter navigation based on new access logic
    if 'nav' in config:
        print(f"📊 Filtering navigation for {audience} audience:")
        filtered_nav = []
        for nav_item in config['nav']:
            filtered_item = filter_navigation(nav_item, audience)
            if filtered_item:
                filtered_nav.append(filtered_item)
        config['nav'] = filtered_nav
        print(f"✅ Navigation filtered: {len(filtered_nav)} top-level items")
    
    return config

def main():
    print("🚀 Starting configuration generation with new access logic...")
    
    # Load base configuration
    try:
        with open("mkdocs.yml", "r") as f:
            base = yaml.load(f, Loader=yaml.FullLoader)
    except Exception as e:
        print(f"❌ Error loading mkdocs.yml: {e}")
        return
    
    # Read audiences from config (with fallback)
    configured_audiences = base.get("extra", {}).get("audiences", ['internal', 'partner', 'beta'])
    
    # Include public in the builds
    all_audiences = ['public'] + configured_audiences
    print(f"📋 Building for audiences: {all_audiences}")
    
    # Generate config for each audience
    generated_files = []
    for audience in all_audiences:
        config = create_audience_config(base, audience)
        
        if audience == 'public':
            filename = "mkdocs.public.yml"
        else:
            filename = f"mkdocs.{audience}.yml"
        
        with open(filename, "w") as f:
            yaml.dump(config, f, sort_keys=False, default_flow_style=False)
        
        generated_files.append(filename)
        print(f"✅ Generated {filename}")
    
    print(f"\n🎉 All {len(all_audiences)} configuration files generated successfully!")
    print("📁 Generated files:")
    for filename in generated_files:
        print(f"   - {filename}")
    
    print("\n📋 Testing commands:")
    print("   mkdocs serve --config-file mkdocs.public.yml    # Public: 'Stratum Knowledge Base'")
    print("   mkdocs serve --config-file mkdocs.internal.yml  # Internal: 'Stratum Knowledge Base (Internal)'")
    print("   mkdocs serve --config-file mkdocs.partner.yml   # Partner: 'Stratum Knowledge Base (Partner)'")
    print("   mkdocs serve --config-file mkdocs.beta.yml      # Beta: 'Stratum Knowledge Base (Beta)'")

if __name__ == '__main__':
    main()