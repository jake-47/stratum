# Stratum
>A multi-audience documentation framework for a single source of truth

Stratum is built on MkDocs with the Material for MkDocs theme. It lets you serve multiple audiences—internal teams, partners, beta users, and the public—from one unified documentation base.

Instead of duplicating files or running multiple sites, Stratum uses audience tags and conditional macros to selectively render content at build time. Writers work in Markdown. Visibility is determined by config and logic—not by duplication.

It’s a way of saying:
**“We care who is reading, but we don’t want five versions of the truth.”**

## Core strengths
- One set of Markdown files, many tailored outputs
- Granular access control per block, section, or page
- Seamless integration with MkDocs Material
- Clean build system that generates audience-specific config files
- Scalable architecture that’s easy to onboard and maintain

Stratum is ideal for teams who need clarity, maintainability, and layered access without sacrificing writing simplicity.

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

## Motivation
I'm not a dev. I'm not a designer. I'm a technical writer, a documentation specialist, if you will. It would've been nice if there was a ready-made solution out there, but I couldn't find any framework or theme that fully supports multi-audience conditional builds with macro logic, config generators, and styled content wrappers. Companies like Google or Stripe build similar frameworks _in-house_ on top of static site generators (SSGs) like Docusaurus, Hugo, Sphinx, Next.js** (with custom MDX pipelines). So, I used ChatGPT (OpenAI) and Claude (Anthropic) to keep the framework within MkDocs (fast, Markdown-native, great for non-devs). It [wasn't all fun](https://raw.githubusercontent.com/jake-47/stratum/blob/main/assets/ai.mp4)! But man, *techmology*! 

I built Stratum for my needs. But feel free to clone it, fork it, modify it, and even sell it. And if you're inclined, I'd appreciate any contributions to make this better. Cheers!

---