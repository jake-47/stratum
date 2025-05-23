@env.macro 
def should_show_content(content_audiences):
    """
    Determine if a content block or page should render based on audience tags.

    Parameters:
    - content_audiences (list[str]): The list of audiences required for this content to appear.
      Example: ["internal", "partner"]

    Returns:
    - True if the current build context includes any of the given audiences
    - False otherwise

    Audience Rules:
    - Internal sees everything
    - Partner sees only partner content
    - Beta sees only beta content
    - Public sees only untagged content
    """
    # Internal sees everything
    if audiences.get("internal", False):
        return True
        
    # If content has no audience tags, only show in public
    if not content_audiences:
        is_public_build = not any(audiences.values())
        return is_public_build
    
    # For specific audiences, only show if build matches content audience
    if audiences.get("partner", False):
        return "partner" in content_audiences
    if audiences.get("beta", False):
        return "beta" in content_audiences
        
    return False  # Explicit fallback

@env.macro 
def should_render_page():
    """Check if current page should be rendered based on new access logic"""
    try:
        page = env.page
        if not page or not hasattr(page, 'meta'):
            return True  # Render if no metadata
        
        raw = page.meta.get('audiences')
        if not raw:
            # Page has no audience tags - only show in public build
            is_public_build = not any(audiences.values())
            return is_public_build
        
        # Parse page audiences
        if isinstance(raw, str):
            page_audiences = [x.strip() for x in raw.split(',')]
        elif isinstance(raw, list):
            page_audiences = raw
        else:
            return True
        
        # Apply new logic
        return should_show_content(page_audiences)
        
    except AttributeError:
        # Page info not available yet
        return True
    
    return False  # Explicit fallback