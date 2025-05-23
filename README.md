# Stratum
>an elegant multi-audience documentation framework

Stratum is built on [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. There isn't much of difference from an aesthetic angle, but it lets you serve multiple audiences—internal teams, partners, beta users, and the public — from one unified documentation base. Write documentation once, and serve different audiences (internal, partner, beta, public) with surgical precision using conditional macros and frontmatter tags.

|Audience|Can See Content Marked As|
|---|---|
|**Internal**| **everything**: default (public), partner, beta, internal |
|**Partner**|partner only|
|**Beta**|beta only|
|**Public**|default content with no `audiences:` frontmatter (i.e. untagged)|

The reason for that logic:
- Internal teams need full visibility to support partners, test beta features, and manage docs.
- Partners and beta users must only see their authorized content.
- Public users should only see untagged general documentation.

To prevent privacy leaks, confusion, and content drift, Stratum uses purpose-built automated builds—each precisely filtered and clearly labeled to ensure the right content reaches the right audience, every time. Instead of duplicating files or running multiple content trees, Stratum uses audience tags and conditional macros to selectively render content at build time. That’s its real advantage. Stratum's in a way of saying: **“We care about who's reading, but we don’t want five versions of the truth in ten different places.”**

## Core strengths
- One set of Markdown files, many tailored outputs
- Granular access control per block, section, or page
- Seamless integration with MkDocs Material
- Clean build system that generates audience-specific config files
- Scalable architecture that’s easy to onboard and maintain

Stratum is ideal for teams who need clarity, maintainability, and layered access without sacrificing writing simplicity.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/jake-47/stratum.git
cd stratum
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install .
```

This installs all dependencies listed in `pyproject.toml`, including `mkdocs`, `mkdocs-material`, macros, and any plugins used by Stratum.

### 4. Generate Audience Configs

```bash
python generate_configs.py
```

This creates `mkdocs.public.yml`, `mkdocs.internal.yml`, `mkdocs.partner.yml`, and `mkdocs.beta.yml` based on audience logic.

### 5. Run a Local Server

Pick the audience config you want to preview:

```bash
mkdocs serve --open     # Public content
mkdocs serve -f mkdocs.internal.yml   # Internal view
mkdocs serve -f mkdocs.partner.yml    # Partner-only docs
mkdocs serve -f mkdocs.beta.yml       # Beta feature set
```

## Philosophy
At its core, Stratum is committed to **minimal forking, maximum reuse**. Writers work in a unified Markdown corpus, embedding audience-specific content using simple, declarative logic. A developer building a CLI guide and a designer writing integration tips don’t need to worry about which file to use—there’s only one. The system handles visibility **surgically** at render time.

### One Source. Multiple Perspectives.
Stratum rejects the traditional tradeoff between centralized content and contextual relevance. With Stratum, documentation can serve diverse needs without creating parallel versions. Instead of duplicating files, writers embed conditional logic where necessary and let the build process determine what each audience sees.

This isn’t just a technical decision—it’s an editorial one. It prevents divergence, reduces maintenance costs, and ensures that updates flow cleanly to every version of the docs.

### Audience Visibility Without Complexity
Each audience—internal, partner, beta, and public—is configured at build time through YAML flags. Writers specify audience context using the `audiences:` field in the frontmatter and embed conditional content with macros like `{% if is_internal() %}` or `{{ "...content..." | audience_content("partner") }}`.

There is no need for non-technical contributors to learn Python or manipulate configuration files. Markdown remains the authoring language. Writers write; the system frames.

### Design Principles
1. **Clarity Through Context**
   Content is not hidden; it is framed. Readers see badges, styles, and signals that clarify what is meant for them. Relevance is established through framing, not exclusion.
2. **Configuration, Not Duplication**
   Audience segmentation lives in config files, not in forks. Whether you’re serving one audience or five, the documentation structure stays the same.
3. **Progressive Disclosure**
   Internal users see everything. Partners and beta testers see what’s meant for them. The public sees a refined core. No content is duplicated—only visibility changes.
4. **Scalable Without Fragmentation**
   Adding a new audience is as simple as adding a new build. There’s no need to reorganize files or maintain parallel docs. The system scales cleanly as the organization grows.
5. **Friendly to Writers, Scriptable for Developers**
   Writers work in familiar Markdown. Developers configure builds using Python and YAML. The tooling remains powerful, but never intrusive.
6. **Style Supports Semantics**
   Audience-specific content is styled with subtle consistency—purple for internal, blue for partners, amber for beta. This visual hierarchy supports clarity, not distraction.
7. **Operational Sustainability**
   Stratum’s architecture is designed for long-term maintainability. Updates are made once. Builds are automated. Docs stay in sync.

## Why MkDocs
MkDocs is a static site generator purpose-built for documentation. Written in Python, it provides a clean, efficient workflow for developers and writers alike. Unlike general-purpose tools like Jekyll or Docusaurus, MkDocs focuses on speed, simplicity, and structure—making it ideal for teams who want documentation that evolves with their code.

### Python-Friendly Workflow
MkDocs integrates naturally into Python ecosystems. With straightforward pip installation and plugin development in Python, it's ideal for teams that already build, test, and deploy in Python. Unlike Jekyll (Ruby) or Docusaurus (React/JavaScript), MkDocs avoids the context switch and offers direct extensibility in the language many developers already use.

### Simplicity Without Sacrifice
You can get started with MkDocs using only Markdown files and a YAML configuration. It offers a smooth learning curve without sacrificing extensibility. Compared to the complexity of Sphinx or the verbosity of Antora, MkDocs gives you productivity out of the box, ideal for small teams or fast-paced projects where results matter more than customization depth.

### Material Theme Advantage
Starting with the Material for MkDocs theme gives teams a powerful head start. It delivers a responsive, visually polished, and production-grade experience that works seamlessly across mobile and desktop. With support for tabbed content, collapsible sections, code highlighting, and styled admonitions, the Material theme dramatically shortens the time to create high-quality technical documentation. Unlike building a theme from scratch, it ensures consistent compatibility with devices and plugins, and eliminates the need for deep front-end expertise.

### Fast, Incremental Builds
MkDocs shines in developer experience with near-instant builds, even for large documentation sets. Its incremental build feature ensures that only changed files are rebuilt, which significantly outperforms Jekyll and Docusaurus as documentation grows.

### Plugin Ecosystem Flexibility
MkDocs has a strong, approachable plugin ecosystem. You can add support for diagrams, mathematical expressions, versioning, audience targeting, and more—all through well-maintained plugins. This flexibility exceeds what mdBook offers and avoids the complexity of Sphinx’s plugin system or Antora’s stricter architectural conventions.

### Perfect for Reference Documentation
While tools like Antora suit modular enterprise systems and mdBook favors tutorials, MkDocs excels at reference documentation. Its hierarchical navigation, built-in search, and semantic structure make it ideal for API references, product guides, and technical overviews.

### Collaborative-Friendly
With Markdown authoring and git-based workflows, MkDocs enables both developers and writers to contribute seamlessly. Teams avoid the overhead of GitBook’s SaaS model or Confluence’s licensing and platform constraints. Writers use familiar syntax, developers benefit from CI/CD-ready infrastructure, and no one is locked into a proprietary editor.

## MkDocs vs. Other Documentation Tools

### Antora
Antora’s strength lies in modular multi-repository docs using AsciiDoc, especially for enterprise use. But it demands greater setup effort and Node.js tooling. MkDocs, with Markdown and Python, offers a gentler learning curve and faster iteration. The Material theme also gives MkDocs more polished UI components out of the box.

### GitBook
GitBook provides ease of use with its WYSIWYG editor and collaboration tools, but comes at the cost of flexibility and control. It’s more expensive to scale, harder to customize, and limited in versioning. MkDocs offers local editing, git integration, and free hosting via GitHub Pages—ideal for developer-focused teams.

### Jekyll
Though Jekyll was an early leader in static sites, it wasn’t designed for documentation. Its Ruby-based workflow is less accessible, and it lacks built-in doc-centric features like nested navigation or content tabs. MkDocs, with the Material theme, offers those out of the box with simpler configuration.

### Sphinx
Sphinx is powerful for Python API docs, thanks to autodoc and semantic markup, but it has a steep learning curve and requires reStructuredText. MkDocs is easier to use, with Markdown at its core, and still supports complex needs through plugins. Material gives MkDocs modern visual design without requiring front-end expertise.

### mdBook
Built for linear reading and tutorials, mdBook is fast and simple, but less flexible for reference-style documentation. It lacks a right-hand TOC panel and has fewer UI options. MkDocs supports richer interaction via the Material theme and is easier to extend, especially for Python teams.

### Docusaurus
Docusaurus, based on React, supports documentation, blogs, and landing pages. It's powerful for integrated web platforms, but requires JavaScript knowledge and longer build times. MkDocs, with Python and Markdown, offers faster builds and simpler authoring for teams focused solely on documentation.

### Confluence
While Confluence is widely used for internal wiki-style documentation, it struggles with versioning, custom styling, and development workflow integration. Pages are loosely connected, making structured navigation difficult. It’s not ideal for version-specific docs or developer-driven pipelines. MkDocs, by contrast, uses structured YAML navs, supports multiple output builds, and integrates with git, CI/CD, and custom preview deployments. With full theming control, offline portability, and negligible hosting costs, MkDocs offers more precision, flexibility, and sustainability for growing product teams.

## Motivation
I'm not a dev. I'm not a designer. I'm a technical writer, if you will, a documentation specialist. It would've been nice if there was a ready-made solution out there, but I couldn't find any framework or theme that fully supports multi-audience conditional builds with macro logic, config generators, and styled content wrappers. Companies like Google or Stripe build similar frameworks _in-house_ on top of static site generators (SSGs) like Docusaurus, Hugo, Sphinx, Next.js** (with custom MDX pipelines). So, I used ChatGPT (OpenAI) and Claude (Anthropic) to keep the framework within MkDocs (fast, Markdown-native, great for non-devs). [It wasn't all fun](https://x.com/litteralyme0_/status/1925478490381722084)! But man, *techmology*!

I built Stratum for my needs. But feel free to clone it, fork it, modify it, and even sell it. And if you're inclined, I'd appreciate any contributions to make this better. Cheers!

---