---
title: Audience Examples
audiences: internal, partner
---

> Always use `audiences` (plural) in your page frontmatter, even when targeting only one audience type. This ensures consistency across all documentation and prevents confusion about field naming.

# Multi-Audience Documentation Examples

This page demonstrates how Stratum's audience-based system supports layered documentation from a single source of truth.

## Getting Started

```bash
cd ~/Documents/mkdocs-simple
python3 -m venv venv
source venv/bin/activate
pip install mkdocs mkdocs-material mkdocs-macros-plugin pyyaml
python generate_configs.py
mkdocs serve --open
````

## Public Foundation

This section is always visible and forms the baseline documentation for everyone.

## Internal Audience
{% if is_internal() %}
!!! internal "{{ 'internal' | audience_label }} Development Notes"
\- Internal API: `https://api-internal.company.com`
\- Debug mode: `DEBUG_MODE=true`
\- Staging: `https://staging.internal.company.com`
\- VPN required for access
{% endif %}

## Partner Audience

{% if is_partner() %}
!!! partner "{{ 'partner' | audience_label }} Partner Resources"
\- Portal: `https://partners.company.com`
\- API Rate: 10,000 req/hr
\- SLA: 24-hour response via [partners@company.com](mailto:partners@company.com)
\- Webhook templates available
{% endif %}

## Beta Audience

{% if is_beta() %}
!!! beta "{{ 'beta' | audience_label }} Beta Access"
\- Beta Dashboard (v2.1)
\- AI content suggestions
\- Weekly beta call: Fridays 2PM PST
\- Feedback via #beta-testing-2025 Slack
{% endif %}

## Multi-Audience Access

{% if for_audience('internal', 'partner') %}
!!! info "Advanced User Features"
Shared with trusted users for advanced support:
\- Slack access to engineers
\- Priority tickets
\- Custom branding options
{% endif %}

{% if for_audience('partner', 'beta') %}
!!! warning "Early Access Features"
Experimental tools available for early feedback:
\- API v2.1
\- Dashboard preview
\- Real-time integrations
{% endif %}

{% if for_audience('internal', 'beta') %}
!!! note "Testing Tools"
Shared testing kits for performance & UX feedback.
{% endif %}

## Content Blocks with Filters

{{ "**Q2 2025 Roadmap**

1. MFA with hardware tokens
2. CDN integration
3. Mobile app beta" | audience_content("internal") }}

{{ "**Partner Checklist**

* [ ] Webhooks verified
* [ ] Billing configured
* [ ] Go-live scheduled" | audience_content("partner") }}

{{ "**Beta Testing Protocols**

* Install in staging
* Submit issues via Slack
* Biweekly feedback calls" | audience_content("beta") }}

## Public API Example

```js
fetch('https://api.company.com/v1/public/data', {
  headers: {
    'Authorization': 'Bearer ' + publicApiKey
  }
})
```

{% if is_internal() %}

### Internal API Example

```js
fetch('https://api-internal.company.com/v1/admin', {
  headers: {
    'Authorization': 'Bearer ' + internalToken
  }
})
```

{% endif %}

{% if is_partner() %}

### Partner API Example

```js
fetch('https://api.company.com/v1/partner/analytics', {
  headers: {
    'Authorization': 'Bearer ' + partnerApiKey
  }
})
```

{% endif %}

{% if is_beta() %}

### Beta API Example

```js
fetch('https://api-beta.company.com/v2/ai-insights', {
  headers: {
    'Authorization': 'Bearer ' + betaApiKey
  }
})
```

{% endif %}

---

*This page demonstrates Stratum’s conditional content architecture—layering visibility by audience while preserving maintainability.*