def define_env(env):
    """
    Define environment variables and macros for MkDocs.
    """

    # Build-time audience flags
    audiences = {
        "internal": env.variables.get("audience_internal", False),
        "partner": env.variables.get("audience_partner", False),
        "beta": env.variables.get("audience_beta", False),
    }

    # === Audience Check Macros ===
    @env.macro
    def is_internal():
        return audiences.get("internal", False)

    @env.macro
    def is_partner():
        return audiences.get("partner", False)

    @env.macro
    def is_beta():
        return audiences.get("beta", False)

    @env.macro
    def for_audience(*audience_types):
        return any(audiences.get(aud, False) for aud in audience_types)

    # === Logic: Should Show Content ===
    @env.macro 
    def should_show_content(content_audiences):
        """
        Determine if a content block should be shown based on audience tags.
        """
        if audiences.get("internal", False):
            return True  # Internal sees everything

        if not content_audiences:
            is_public_build = not any(audiences.values())
            return is_public_build

        if audiences.get("partner", False):
            return "partner" in content_audiences
        if audiences.get("beta", False):
            return "beta" in content_audiences

        return False

    # === Logic: Should Render Page ===
    @env.macro 
    def should_render_page():
        """
        Check if the current page should be rendered based on page metadata.
        """
        try:
            page = env.page
            if not page or not hasattr(page, 'meta'):
                return True

            raw = page.meta.get('audiences')
            if not raw:
                is_public_build = not any(audiences.values())
                return is_public_build

            if isinstance(raw, str):
                page_audiences = [x.strip() for x in raw.split(',')]
            elif isinstance(raw, list):
                page_audiences = raw
            else:
                return True

            return should_show_content(page_audiences)

        except AttributeError:
            return True

        return False

    # === Badge Label Filter ===
    @env.filter
    def audience_label(audience_type):
        return f'<span class="badge badge--{audience_type}">{audience_type.title()}</span>'

    # === Content Wrapper Filter ===
    @env.filter
    def audience_content(content, audience_type):
        content_audiences = [audience_type] if audience_type else []
        if should_show_content(content_audiences):
            return f"""<div class="audience-content audience-content--{audience_type}" markdown="1">

{content}

</div>"""
        return ""
