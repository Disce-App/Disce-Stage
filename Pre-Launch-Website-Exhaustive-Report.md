# State of the Art for a Pre-Launch Startup Website — Exhaustive Report

An evidence-based benchmark for digital startups (SaaS, AI, and data-sensitive B2B products) whose product is still in development and whose beta, waitlist, or early-access phase is upcoming.

A strong pre-launch website is not a showcase for an unfinished product and not a reduced version of a post-launch marketing site. It is a **strategic learning, trust-building, and qualification instrument**. Its main job is to make the product legible, qualify interest, create justified trust, and capture the next best commitment for the company's current stage — not to simulate a market maturity it does not yet have. Success is measured by whether the right visitors correctly understand the product, choose an appropriate next step, and deliver actionable signals for product and go-to-market decisions.

For most early-stage SaaS and AI startups, the right benchmark is not "maximum polish" but **"minimum ambiguity"**: visitors should quickly understand what the product is, who it is for, what problem it addresses, how it broadly works, what is already real, and what happens if they sign up.

**Evidence labeling used throughout this report:** **[E]** standard- or research-backed, **[P]** widespread industry practice, **[X]** reasoned expert judgment, **[K]** strongly context-dependent.

## Research Basis and Method

This report synthesizes formal standards, UX research, privacy and accessibility guidance, and direct benchmark observation of current digital-product websites. The strongest evidentiary base comes from W3C WCAG guidance, NIST's AI Risk Management Framework, GDPR/EDPB and BfDI guidance, and established UX research organizations such as Nielsen Norman Group (NN/g) and the Baymard Institute. [w3](https://www.w3.org/WAI/standards-guidelines/wcag/) [nvlpubs.nist](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)

Where primary evidence on historical pre-launch startup pages was limited, current product sites (Linear, Attio, Granola, Cursor, Replit Agent, v0, Descript, Screen Studio, Gamma, Notion AI, Tana, Arc, Vanta) were used as **pattern references**, not treated as verified pre-launch examples. The report distinguishes between directly observable facts on a current site and transferable interpretation for earlier-stage startups. Recommendations are therefore split conceptually into four buckets: source-backed findings **[E]**, widespread industry practice **[P]**, reasoned expert judgment **[X]**, and context-dependent decisions **[K]**.

## 1. Executive Summary

1. **The website needs a defined primary job per maturity phase.** In problem validation, an interview or a design-partner application is more valuable than a large, unqualified email list; shortly before public beta, a scalable early-access funnel can make sense. **[X]** Before launch, the site is usually a demand-validation and expectation-management layer as much as a marketing asset — conversion *quality* matters more than raw volume.

2. **A waitlist is only a product mechanism when access, value exchange, and follow-up are defined.** Without selection criteria, realistic expectations, and communication, it is merely a contact form with low informational value. It becomes strategically useful only when access is genuinely constrained or intentionally staged, invite logic is real, and signup gives the user a credible reason to act now rather than later.

3. **Clarity beats visual originality.** Visitors must quickly recognize: what is it, who is it for, what problem does it solve, how does it fundamentally work, and what is available now. A value proposition should make the offering, target audience, benefit, and differentiation understandable. [cxl](https://cxl.com/blog/value-proposition-examples-how-to-create/)

4. **Information architecture should grow with actual decision complexity.** A focused MVP can get by with a strong homepage, beta page, FAQ, privacy policy, and imprint; a data-sensitive B2B/AI product usually needs additional use-case, security, and process information. **[X]**

5. **The hero should not tell a complete product story.** It needs an understandable category frame, a concrete outcome, a mechanistic explanation, a dominant CTA, and ideally a credible product depiction — plus an honest status label ("Private Beta," "Applications Open," "Public Beta Soon") that prevents the bait-and-switch feel of a seemingly available product that actually ends in a waitlist.

6. **Real product images should be preferred over abstract AI visuals once a viable interface exists.** A screenshot or short workflow proves that a concrete product is being built; abstract visuals can convey brand character but rarely explain product mechanics.

7. **Pre-launch copy must distinguish between present and future.** Statements such as "already available," "tested in private beta," and "planned" must not be visually or linguistically mixed.

8. **AI products need additional explanations.** Relevant are data sources, human control, permitted inputs, handling of outputs, known limitations, and — depending on risk — security and data-protection measures. NIST counts transparency, explainability, privacy, security, and accountability among trustworthy AI properties; NN/g's current AI research highlights transparency, control, consistency, and support-when-the-system-fails as the practical trust fundamentals for AI products. [nvlpubs.nist](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)

9. **Social proof must be verifiable and semantically correct.** "Design partner," "pilot," "advisor," and "customer" are not interchangeable. a16z describes design partners specifically as early users who help *define the problem space and shape the solution* — not merely passive beta testers. Logos or testimonials without a clear relationship type may raise authority short-term but create significant credibility risk; Baymard's research on perceived security shows users distinguish sharply between self-asserted signals and externally or concretely substantiated proof.

10. **Conversion friction should be deliberately chosen.** An email field maximizes reach; a short application increases signal quality; a conversation CTA suits complex B2B validation. Forms should first eliminate unnecessary questions, then automate, then simplify. [nngroup](https://www.nngroup.com/articles/eas-framework-simplify-forms/)

11. **The thank-you experience is part of the conversion flow.** It must confirm sign-up, set expectations around selection and timing, offer the next reasonable step, and begin a reliable communication relationship — not just a generic "thanks."

12. **Motion is only valuable when it explains orientation, state, or product mechanics.** Auto-rotation, scroll hijacking, and persistent movement compete with copy and CTA; non-essential interaction-based motion must be reducible under WCAG 2.2. [w3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)

13. **Accessibility, performance, and privacy are trust signals, not later optimizations.** They shape perceived competence *before* any product trial begins. WCAG 2.2 structures accessibility along "perceivable, operable, understandable, robust"; the BfDI generally requires informed, voluntary consent for non-essential tracking. [w3](https://www.w3.org/WAI/standards-guidelines/wcag/)

14. **With low traffic, qualitative signals matter more than seemingly precise conversion benchmarks.** Relevant metrics are ICP fit, quality of described problems, willingness to be interviewed, response rate, use of existing alternatives, and actual commitment.

15. **The pragmatic minimum is small, but not superficial:** clear positioning, a visible product mechanism, honest status, a fitting CTA, an accessible conversion flow, team/contact transparency, a real follow-up process, and technically/legally sound foundations.

# 2. Roles and Goals of the Pre-Launch Website

## Core tasks

A pre-launch website should fulfill five jobs, which differ from a post-launch site where the dominant task is usually activation or sales efficiency rather than hypothesis testing:

- **Orient:** Make the product category, target audience, problem, and benefit understandable.
- **Qualify:** Distinguish relevant visitors from merely curious ones.
- **Enable trust:** Make team, product status, way of working, data processing, and contact options visible.
- **Measure behavior:** Capture not just visits, but CTA interest, completed applications, willingness to talk, and target-audience fit.
- **Learn:** Test messaging hypotheses, use cases, ICP assumptions, and objections.

In practical terms, the site should answer a small set of high-value questions with minimal delay: what the product is, who should care, why the existing workflow is inadequate, how the product intends to change that workflow, and what participation is currently possible. Sites that skip these answers and move directly to abstract vision or decorative branding shift interpretive work onto the visitor and weaken both comprehension and conversion.

A landing page can test demand, but alone it proves neither willingness to pay nor product-market fit. Painted-door or smoke-test approaches should use pre-defined hypotheses and a transparent post-click explanation, so interest is measured without deceiving users. [amplitude](https://amplitude.com/explore/experiment/fake-door-testing)

## Maturity phases

| Phase | Primary website job | Best-fit conversion / CTA | Main risk / unsuitable signal |
|---|---|---|---|
| Idea / problem validation | Test problem relevance and audience fit | Interview request, problem discovery, manual pilot outreach ("Explore the problem with us") | Collecting vanity emails / a large generic waitlist with no learning value |
| MVP in development | Test solution framing and workflow resonance | Design-partner inquiry, prototype feedback ("Apply as a design partner") | Overpromising readiness — "Get started now" when nothing is startable |
| Closed / private beta | Recruit a narrow, suitable cohort | Qualified beta application ("Apply for the private beta") | Treating all interest as equally valuable; unconditional access promises |
| Open waitlist | Aggregate and segment broad demand | Email signup with light qualification ("Get early-access updates") | Waitlist with no clear value exchange; queue position without recognizable logic |
| Near / before public beta | Build activatable demand | Launch notification, invite waves, demo | Artificial scarcity without an operational reason |
| Public beta | Activation and feedback | Account creation, onboarding, bug feedback ("Try the beta") | Another waitlist despite available capacity |

The closer the product moves toward a usable beta, the more the website can optimize for scalable acquisition. Earlier than that, the better objective is usually structured learning from the right people.

## Business-model dependency

| Model | Website focus | Suitable conversion goal |
|---|---|---|
| Self-serve B2C / prosumer | Immediate understanding, emotional benefit, low friction | Email, download, or public-beta access |
| SMB SaaS | Workflow, integrations, time savings, easy onboarding | Beta application or early access |
| Enterprise B2B | Business case, security, stakeholder fit, implementation | Demo, discovery call, or design partner |
| Developer tool | Technical mechanism, APIs, docs, example output | Sandbox, docs, GitHub, or beta access |
| Data-sensitive AI product | Control, data flows, human oversight, limits | Qualified beta or accompanied pilot project |
| Marketplace | Benefit for both market sides and liquidity strategy | Separate CTAs per market side |

## Trade-offs

- **Hype vs. credibility:** Vision can generate attention; unsubstantiated superlatives shift the burden of proof onto a product that cannot yet carry them.
- **Clarity vs. strategic openness:** Overly broad statements seem generic; persona positioning that is too narrow can close off later learning space.
- **Conversion vs. lead quality:** A short form typically increases completion likelihood; additional questions can improve beta selection. The EAS principle and NN/g's form-simplification guidance both stress that users complete forms more readily when perceived effort is lower and non-essential fields are removed or deferred. [nngroup](https://www.nngroup.com/articles/eas-framework-simplify-forms/)
- **Transparency vs. fear of uncertainty:** An honest beta status can slow things short-term but prevents false expectations and later disappointment.
- **Exclusivity vs. fairness:** Limited spots are plausible when support, infrastructure, or research capacity is limited; otherwise scarcity is quickly recognized as manipulative gamification.

## Waitlist decision

A waitlist makes sense when at least three questions are answered:

1. **Why can't everyone access it yet?**
2. **According to what criteria or in what waves are invitations sent?**
3. **What does the person receive during the waiting period?**

Otherwise, "join the waitlist" is usually too weak because it communicates effort without a clear return.

Alternatives are: problem/feedback interview, prototype test, newsletter with domain-specific value, design-partner program, beta application, demo request, community access, launch notification, manually provided concierge version, or preorder/letter of intent with a sufficiently concrete offer.

Design partners are not merely early testers: they should bring a representative problem, sufficient capacity to collaborate, and genuine commitment. a16z frames this precisely — design partners help *define the problem space and shape the solution*, which is a materially different relationship than passive beta testing. Documented programs sometimes work with live demos, technical review, clear timeframes, and mutual obligations. [review.firstround](https://review.firstround.com/sierra-design-partnership/)

**Historical precedent for staged access.** Waitlists have worked historically when tied to a broader rollout *system* rather than used as a standalone CTA. Tana used staged invitation logic and existing-user invites before a wider public release (going fully public in February 2025); Arc's Windows beta rollout was similarly tied to phased, technically justified access constraints rather than manufactured hype. [techcrunch](https://techcrunch.com/2023/12/11/arc-browser-launches-its-windows-client-in-beta/) The transferable principle is not exclusivity by default, but **credible sequencing** — an invitation system can, however, place social exclusivity above actual benefit if the sequencing logic isn't real, so this pattern only transfers well when the cohorting is genuinely capacity-driven.

# 3. Recommended Information Architecture

## Lean model

**Suitable for:** small team, focused MVP, low traffic, low regulatory complexity. One primary audience, one dominant workflow, limited internal bandwidth. The homepage carries most of the explanatory load; legal and trust depth lives on separate pages only where necessary.

```text
/
├── Hero + product promise
├── Product mechanism
├── 2–3 core use cases
├── Product status / beta expectation
├── Team or credibility module
├── FAQ
└── CTA

/beta or /early-access
/privacy
/imprint
/contact – optional as a module
```

A single page is sufficient when visitors essentially share the same target audience, the same use case, and the same action. This model works because **progressive disclosure** reduces cognitive load: the homepage handles first understanding, and deeper pages answer only the questions that remain important for action or trust. NN/g describes progressive disclosure as a way to defer advanced or secondary information so systems are easier to learn and less error-prone. [nngroup](https://www.nngroup.com/videos/progressive-disclosure/)

## Comprehensive model

**Suitable for:** ambitious B2B/AI product, multiple buying/stakeholder roles, an explanation-heavy workflow, or sensitive data. It is reasonable to split out product mechanics, use cases, security, privacy, and AI transparency into dedicated pages so the homepage stays concise without becoming shallow.

```text
/
├── /product or /how-it-works
├── /use-cases
│   ├── /use-case-a
│   └── /use-case-b
├── /for/[role-or-industry] – only for a genuinely different story
├── /beta or /design-partners
├── /security
├── /privacy
├── /ai-transparency or /responsible-ai
├── /about
├── /faq
├── /contact
├── /updates or /changelog
└── /imprint
```

## Page decisions

| Page / module | Purpose | Core content | Priority | Dependency |
|---|---|---|---|---|
| Homepage | First understanding and routing | Category, target audience, outcome, mechanics, status, CTA | P0 | Clear positioning |
| Beta / early access | Expectation and conversion | Value exchange, selection, timing, form, privacy | P0 for a waitlist | Defined beta process |
| How it works | Prove the mechanism | Input, processing, output, control | P0/P1 | Viable workflow |
| Use cases | Establish relevance | Starting situation, task, product role, outcome | P1 | Validated jobs-to-be-done |
| Role/industry pages | Different buyer journeys | Language, objections, processes per segment | P1/P2 | Genuinely different segments |
| Security / trust | Answer risk questions | Data flow, hosting, access, subprocessors, contact | P0 for sensitive B2B data | Verified measures |
| AI transparency | Explain AI's role | Models, data usage, control, limits | P0/P1 for AI | Technical facts |
| About / team | Make the sender credible | People, expertise, motivation, contact | P1 | Relevant credibility |
| FAQ | Reduce remaining uncertainty | Availability, price, data, platforms, selection | P0 as a module | Real objections |
| Changelog / updates | Show progress and activity | Dated, substantive changes | P2 | Continuous maintenance |
| Roadmap | Expectation management | Direction rather than binding feature promises | P2 | Consider high cost of change |
| Blog / resources | Expertise and acquisition | Only relevant, high-quality content | P2 | Editorial capacity |
| Contact | Capture high-intent leads | Email, calendar, or short form | P1 | Response process |
| Careers | Recruiting | Only if there are open roles | P2 | Actual positions |
| Privacy / imprint | Transparency and mandatory disclosures | Processing, responsible party, contact | P0 | Legal review |

**Don't inflate too early:** a common early-stage mistake is adding pages *because established SaaS sites have them*, not because visitors need them. Empty blogs, weak roadmap pages, or token careers sections usually hurt more than they help — they expose thinness rather than maturity, and a deliberately lean navigation looks more mature than an overloaded one.

## What must appear early in the journey

The first screen and immediate follow-on content should make the category, audience, benefit, mechanism, and current availability legible. Detailed integrations, long-form founder stories, or broader category education can usually come later unless the product depends on them for trust or differentiation. Visitors don't start by asking whether the company has a sophisticated information architecture — they start by deciding whether the page is relevant and credible enough to keep reading. Only once that threshold is crossed does the site earn the right to explain more.

# 4. Ideal Landing-Page Dramaturgy

## Narrative flow

The viable basic logic is:

> **Understand → Recognize relevance → Grasp the mechanism → Check evidence → Assess risk → Understand expectations → Act**

Problem and solution don't necessarily need to appear as two separate, long sections. If the hero precisely frames the problem and the product mechanics follow directly, an additional generic "the problem" section can be redundant.

The ideal narrative moves from **comprehension → confidence → commitment**. Repetition across sections is not about restating the same claim in different adjectives, but about restating it at different levels of detail: first as a promise (hero), then as a mechanism, then as a use case, then as a conversion rationale (final CTA).

**Litmus test:** a qualified visitor should be able to restate the site after one pass as — *"This is for people like me, it solves this specific task, it works roughly this way, and this is why the beta ask is reasonable."* If they can't, the page likely contains too much brand theater and not enough product communication.

## Wireframe sequence

| Section | Visitor question | Core message | UI pattern | Common mistake |
|---|---|---|---|---|
| 1. Header | Where am I, what can I do? | Clear product identity and one main path | Logo, 3–5 links, primary CTA | Enterprise navigation before product maturity |
| 2. Hero | What is this, for whom, why relevant? | Category + ICP + outcome + mechanism + status | Headline, subheadline, CTA, status label, product visual | Abstract slogan/poetic headline without a product category |
| 3. Relevance / pain | Do you recognize my work context? | Concrete friction in the existing workflow | Before-situation, short scenarios | Overdramatized generic problem without evidence |
| 4. Mechanism / How it works | How does the product create the benefit? | Input → core action → output | 3-step flow, annotated screenshot, or short demo | Feature labels instead of causal explanation |
| 5. Product evidence | Does a well-thought-out product exist? | Real interaction or viable prototype | Screenshot, click-through, short video, guided UI strip | Unreadable / decorative dashboard mockup |
| 6. Use cases | What can I concretely accomplish with this? | Jobs, triggers, and outcome per scenario | 3–4 cards or tabs, role-neutral scenario cards | Persona tiles with identical or undifferentiated content |
| 7. Differentiation | Why this solution instead of the status quo? | Different mechanism or trade-off | Comparison with previous workflow | Unsubstantiated "10x" claim |
| 8. Trust | Why should I believe you? | Verifiable expertise, pilots, references | Team, pilot status, quotes, sources, credibility module | "Trusted by" without relationship explanation |
| 9. Beta status | What do I get, and when? | Present state, limitations, selection, next step | Status box or timeline | Beta details buried in the FAQ or fine print |
| 10. Trust / data | What happens to my data? | Relevant short answers with deep links | Trust strip, data flow, security link | Generic "enterprise-grade" |
| 11. FAQ | What objections remain? | Concrete, plain-language answers | Accessible accordion or list | FAQ as a repetition of marketing copy |
| 12. Final CTA | Is the next step worth the effort? | Value exchange, effort, and expectation | Short CTA block or form | New CTA type with different logic at the page end |
| 13. Footer | Who is behind this? | Contact, legal, status, central links | Structured footer | Hiding legal information |

## Hero requirements

Above the fold, the following should be recognizable:

- **Category frame:** "AI research workspace," "CRM," "developer tool," or a similarly understandable classification.
- **Target audience:** specific enough to create relevance, but only in the headline if it differentiates.
- **Outcome:** a change in the workflow, not "innovation."
- **Mechanism:** a brief indication of how the result comes about.
- **Status:** e.g., "Private Beta," "MVP in development," or "Applications open."
- **Next step:** a dominant CTA.
- **Evidence:** product interface, workflow, or credible prototype depiction.

A second CTA makes sense when it serves a **different intent level**, e.g., primary "Apply for the beta" / secondary "Watch the 90-second demo." Two equally strongly designed conversion goals such as "join waitlist" and "book demo," on the other hand, create routing work for the visitor.

## Visual hero choice

| Visual | Use when … | Don't use when … |
|---|---|---|
| Real screenshot | UI and core benefit are already stable enough | UI signals the wrong maturity or is unreadable |
| Annotated mockup | Workflow is viable but details are still variable | Mockup suggests functions that are not planned |
| Short interface video | Motion or sequence explains the benefit | It plays sound unprompted or hurts LCP |
| Illustration | Concept, target state, or emotional brand matters | The product is already hard to understand |
| Abstract visual | Strong brand and clear copy already exist | It remains the only product depiction |
| Interactive demo | Benefit can be experienced within a few interactions | It is unstable, slow, or unusable on mobile |

Videos below the initial viewport should be loaded with a delay; `preload="none"`, poster images, and click-to-play reduce unnecessary initial load. [web](https://web.dev/articles/lazy-loading-video)

# 5. UI/UX State of the Art

## Design principle

State of the art before launch does not mean maximum visual complexity, but rather: a clear visual focal point, distinctive yet coherent brand traits, real or verifiable product depiction, clean responsive behavior, accessible interactions, low technical friction, and motion with an explainable function. A solid grid, spacing, grouping, clear headings, and contrast are sufficient for most of a professional structure; YC recommends testing wireframes with users early on. [ycombinator](https://www.ycombinator.com/library/7G-design-for-startups-part-1)

Current startup design trends are only helpful when they improve attention, legibility, or product understanding. Strong typography, spacing, hierarchy, real product visuals, restrained motion, and a coherent layout system all directly contribute to comprehension and trust. Aurora gradients, glass effects, animated particles, or ambient 3D can be visually appealing without adding explanation, and sometimes actively compete with the CTA or product proof.

## Must have

| Pattern | Primary benefit | Suitable for | Risk | Effort |
|---|---|---|---|---|
| Clear typography scale | Reading guidance and scannability | all websites | too many sizes or ultralight weights | low |
| Consistent grid | Order and credibility | all, especially B2B | uniform "template" feel | low |
| Visible hierarchy | Prioritize hero, evidence, and CTA | all | too many equally strong accents | low |
| Real product evidence | Increases trust and reduces abstraction | all | decorative mockups that can't be read | medium |
| Responsive product depiction | Show mechanics on desktop and mobile | SaaS, AI, dev tools | desktop UI unreadable on smartphone | medium |
| One dominant accent | Mark action and status | all | using the accent color everywhere | low |
| Accessible states and forms | Prevent avoidable drop-off | all | designing only the default state | medium |
| Performance budget | Fast first impression | all | removing expensive effects too late | medium |

## Should have

| Pattern | Benefit | Suitable for | Risk | Effort |
|---|---|---|---|---|
| Annotated screenshots | Connect features with outcomes | explanation-heavy products | labels too small | medium |
| Short workflow demo | Show sequence and speed | agentic or multi-step tools | idealized happy path | medium |
| Subtle microinteractions | Convey state and causality | interactive demos, forms | motion without informational value | medium |
| Distinct but restrained brand system | Recognizability without obscuring the product | low-differentiation SaaS categories | decorative motif crowds out the product | medium |
| Mobile-specific composition | Appropriate order and readability | practically all | mere vertical stacking | medium |
| Contextual trust modules | Reduce risk at the right point | B2B, AI, data products | logo graveyard | low |

## Nice to have

| Pattern | Benefit | Suitable for | Risk | Effort |
|---|---|---|---|---|
| Interactive product demo | Independent exploration | clearly bounded workflow | bugs become the first impression | high |
| Bespoke illustration system | Brand and story | emotional or abstract products | low explanatory power | high |
| Choreographed transitions | Premium perception | visually differentiated brands | performance and distraction | high |
| 3D product metaphor | Spatial or technical concepts | hardware, data infrastructure | interchangeable "tech" look | high |
| Dark/light theme | Preference and brand effect | developer tools | double QA cost | medium |
| Dynamic personalization | Segment-specific relevance | sufficient traffic and clear segments | wrong assignment, measurement complexity | high |

*Rule of thumb: advanced motion, 3D, and elaborate illustration systems help only if the fundamentals (typography, hierarchy, real product evidence, accessible forms, mobile clarity) are already strong.*

## Avoid or use carefully

- **Glassmorphism:** Can show layers but loses contrast on complex backgrounds.
- **Aurora gradients:** Create modernity, but by now barely differentiate AI products.
- **Endless logo marquees:** Motion makes verification harder and can mask weak evidence.
- **Scroll hijacking:** Takes control away from users and worsens orientation.
- **Auto-rotating hero content:** Important content can disappear before it's processed; NN/g often recommends a static alternative and advises against auto-forwarding on mobile. [nngroup](https://www.nngroup.com/articles/auto-forwarding/)
- **Cursor effects:** Meaningless on touch devices, often purely decorative.
- **Ambient video in the hero:** Only sensible when it carries product information and is understandable without sound.
- **Glass + gradient + 3D + noise simultaneously:** Leads to visual competition instead of brand character.

## B2B, consumer, and AI

| Context | Visual emphasis | Trust logic |
|---|---|---|
| B2B SaaS | Structure, product reality, integrations, low ambiguity | Process competence, security, points of contact |
| Consumer / prosumer | Outcome, identity, emotional resonance, fast activation | Experienceability, community, easy control |
| AI product | Mechanism, input/output, human control, limits | Transparency, data flows, reviewability |
| Developer tool | Technical artifacts, code, speed, docs | Proof of function, platform compatibility, APIs |

## Motion and microinteractions

Motion should explain state, causality, or product behavior. It becomes harmful when it is decorative, continuous, or impossible to reduce. WCAG 2.2's guidance on animation from interactions requires that motion triggered by interaction can be disabled unless it is essential. [w3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) Treat motion as a scarce resource: a short product walkthrough can be valuable; constant parallax, rotating testimonials, or animated background systems often lower clarity and can harm performance and accessibility at the same time.

## Mobile blind spots

- Desktop screenshots are shrunk instead of recomposed.
- Sticky CTA covers consent, form, or browser UI.
- Navigation requires multiple interactions to reach the primary CTA.
- Videos autoplay despite mobile bandwidth.
- Cards turn into long, monotonous stacks.
- Tap targets and spacing are too small.
- Forms open the wrong keyboards or zoom in because of small text.
- Trust and status information only appears after a lot of scrolling.

A mobile-ready pre-launch site should be checked for actual legibility of the product visual, scannable information density, tap-target sizing, form keyboard behavior, and whether the primary conversion path still feels obvious on a smaller screen. WCAG 2.2 generally requires pointer targets of at least 24 × 24 CSS pixels or sufficient spacing — a useful baseline, though for a more comfortable mobile UX a larger internal design target is often sensible. [w3](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

## Accessibility minimum

- Semantic landmarks and a sensible heading hierarchy
- Full keyboard operability
- Visible focus for every interactive element; without it, sighted keyboard users cannot reliably operate the page. [w3](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)
- Real labels instead of placeholders as field descriptions; instructions available before they are needed
- Textual, field-adjacent, and programmatically announced errors with guidance for correction
- Alt text for meaningful images
- Subtitles or transcripts for content videos
- No information conveyed through color alone
- Text contrast of at least 4.5:1, or 3:1 for large text. [w3](https://www.w3.org/TR/WCAG20/)
- Zoom and reflow without horizontal page scroll
- Respect `prefers-reduced-motion`
- Announce form and status messages for screen readers

This matters strategically, not only ethically: a poor form experience reduces completion, a weak focus indicator excludes keyboard users, and ambiguous errors create drop-off exactly at the moment of highest intent. Automated Lighthouse checks help with performance and accessibility issues but do not replace manual keyboard, screen-reader, zoom, and task testing. [developer.chrome](https://developer.chrome.com/docs/lighthouse/overview)

## Performance minimum

Performance is part of perceived quality. Google's Core Web Vitals "good" thresholds — LCP at or under 2.5 seconds, INP at or under 200 ms, and CLS at or under 0.1 — serve as operational targets, based on real usage rather than a single lab run. [support.nitropack](https://support.nitropack.io/en/articles/9502102-understanding-core-web-vitals-thresholds)

Priorities:

- Compress and correctly size the hero medium; don't lazy-load the LCP resource — deliver it early, discoverable, and prioritized
- Lazy-load media below the fold; reserve dimensions for images and videos
- Remove unnecessary JavaScript and third-party scripts
- Reduce and subset fonts and preload them sensibly
- Prefer animations via `transform` and `opacity`
- Include consent manager, chat, and tracking scripts in performance tests

Pre-launch sites often underperform because they overinvest in video, font variety, and animation libraries before validating whether those assets increase understanding. A faster site with one clear product demo usually outperforms a heavier site with more decorative ambition. [web](https://web.dev/articles/top-cwv)

## Pre-launch QA

| Area | P0 checks | P1 checks |
|---|---|---|
| Desktop | Hero/core message clear without scrolling; CTA visible; no overlapping/broken layout; 200% zoom | ultra-wide and small-laptop viewports |
| Mobile | No horizontal scroll; navigation, hero, and CTA obvious at 320–430 px; product visual/screenshots readable; menu usable | real iOS/Android devices and slow network |
| Forms | Labels attached; required fields indicated; submit, validation, success, duplicate, and retry all function; errors visible in text | autofill, copy/paste, multilingual support |
| Accessibility | Keyboard traversal works; focus visible; labels, contrast, heading structure correct; motion reducible | VoiceOver/NVDA/TalkBack short test |
| Performance | Hero medium optimized; no severe layout shift; limited third-party scripts; test LCP, CLS, video behavior | field monitoring after traffic builds up |
| Privacy / consent | Tracking respects consent logic; no non-essential trackers before consent; form purpose disclosed; privacy link visible | consent revocation and script inventory |
| Error handling | API failure, timeout, offline, duplicate submit, invalid/duplicate email all handled | rate limit, spam, expired links |
| Empty states | No social-proof or changelog placeholders | sensible fallbacks for external embeds |

# 6. Content, Messaging, and Beta Communication

## Value-proposition logic

A viable value proposition combines:

> **For [target audience] who need to accomplish [concrete job / problematic context], [product] is a [understandable category] that enables [outcome] by [mechanism]. Unlike [status quo], it relies on [relevant differentiation].**

Not every component needs to be in the hero, but category, target audience, outcome, and mechanism should be reconstructible in the first screen or immediately after.

## Three language layers

Pre-launch copy should be specific enough to create recognition but flexible enough to allow the product to evolve — narrow on the workflow problem, broader on secondary implementation details that may still change. The strongest early-stage copy usually combines three layers:

- **Problem language:** what is broken or costly in the current workflow.
- **Outcome language:** what the user can do faster, better, or with more confidence.
- **Mechanism language:** how the product creates that change.

Feature language alone is rarely sufficient because it forces visitors to infer the value themselves. Outcome-only language without a mechanism can sound aspirational but ungrounded — especially in AI categories, where skepticism is rising. NN/g's work on explainability argues that trust and explainability are inseparable: users need to understand *how and why* an output was reached, which means category language should make the user's mental model easier, not harder. [nngroup](https://www.nngroup.com/articles/eas-framework-simplify-forms/)

## Language levels (weak vs. precise)

| Level | Weak | More precise |
|---|---|---|
| Problem | "Knowledge work is broken" | "Decisions from interviews are spread across notes, transcripts, and tickets." |
| Feature | "AI-powered insights" | "The system links statements to the underlying interview passages." |
| Outcome | "Work smarter" | "Product teams can trace a decision back to the relevant user quotes." |
| Mechanism | "Intelligent automation" | "After upload, the system groups statements; users review and correct the assignment." |
| Status | "Coming soon" | "The upload and review workflow is currently being tested with five design partners." |
| CTA | "Join us" | "Apply for a guided beta test" |

The examples describe copy structures, not performance guarantees.

## Category framing for AI and SaaS

Many AI startup sites lose clarity by relying on generic labels such as "AI platform," "agentic workspace," or "intelligent automation" without grounding those terms in an observable workflow. A more effective pattern anchors the product in a familiar category and then explains the differentiator — Granola frames itself as an "AI notepad for people in back-to-back meetings," and Descript uses the concrete mechanism "edit video by editing text." Both reduce abstraction while still sounding differentiated. [granola](https://www.granola.ai/ai-note-taker) [descript](https://www.descript.com/)

## Precise pre-launch copy

- **Name the category**, unless the product demonstrably creates a new, explainable category.
- **Use verbs and objects:** "links interview statements to research questions" instead of "reimagines insights."
- **Separate capability and outcome:** the feature explains what happens; the outcome explains why it matters.
- **Show the causal mechanism:** visitors should understand what creates the benefit.
- **Write from the workflow outward:** trigger → action → result.
- **Mark uncertainty:** "planned," "being tested," "available in beta."
- **Avoid universal claims:** especially for AI, accuracy, completeness, and autonomy are context-dependent.
- **Frame limitations as product logic:** "Users confirm suggestions before export" is stronger than "AI can make mistakes."
- **Back up concrete numbers:** no time savings, accuracy, or user count without a verifiable basis.
- **Preserve strategic flexibility in secondary details, not in the core problem.**

## Weak patterns

| Weak pattern | Why it underperforms | Better principle |
|---|---|---|
| "The future of work" | No category, task, or relevance filter | Name the current workflow and the change |
| "Revolutionary AI platform" | Unprovable and interchangeable | Explain the AI's role and output |
| "Unlock your potential" | No observable benefit | Name a concrete change |
| "One platform for everything" | Overly broad promise | Prioritize the primary job |
| "10x productivity" | Unverifiable without a baseline | Name a measurable task or time period |
| "Seamless" | Claims frictionlessness | Make integration steps visible |
| "Secure by design" | Empty without controls | Name concrete measures or status |
| "Trusted by …" with weak proof | Inflates the relationship type | Use precise labels: pilot, advisor, design partner |
| "Limited spots" | Manipulative without a capacity reason | Explain the selection or support reason |
| "Coming soon" | No timing or benefit | Name status, next milestone, and follow-up |
| "Join the waitlist" | No value exchange | Specify access, updates, or co-creation |
| "For teams of all sizes" | Avoids positioning | Name the primary team type |

## AI communication

An AI product page should — depending on risk — answer: what task AI takes on; what stays with the human; what data forms the context; whether customer data is used for training; which model or subprocessors are involved; where data is stored; whether outputs can be checked, corrected, and deleted; which actions the system performs autonomously; which error classes or limits are relevant; how sensitive inputs are handled; and what is logged.

For certain AI applications, additional EU transparency obligations apply; systems that interact directly with people must, depending on use case, clearly indicate their AI nature. For high-risk systems, the AI Act requires information on capabilities, limitations, output interpretation, and human-oversight measures. [artificialintelligenceact](https://artificialintelligenceact.eu/article/13/) The safest pattern is to communicate what the AI does, what the human does, what data is used, what confidence/verification aids exist, and what limitations are known — written in plain language and paired with clear user action rather than abstract disclaimers.

## Beta status module

A trust-building status box follows this pattern:

> **Status:** Private beta
> **Already testable:** [concrete workflow]
> **Still in development:** [concrete areas]
> **Suitable for:** [target audience / requirements]
> **Participation:** [selection, effort, approximate contact logic]
> **Expectation:** [feedback, data, or conversations]
> **Not promised:** [relevant, still-open capability]

Avoid: an apologetic tone, a vague permanent beta without progress logic, fixed roadmap dates without sufficient planning certainty, "founding member" rhetoric without a real benefit, and scarcity without an operational reason. Beta communication should distinguish clearly between what already works, what is still being built, who fits the current phase, and what participants should expect after signup — people tolerate incompleteness if it's honest and well-framed, but react poorly to hidden constraints.

## Generic messaging framework

**Hero:** *[Concrete outcome] for [clear user context].*

**Subheadline:** *[Product] is a [category frame] that turns [input or task] into [usable output] — with [relevant control or differentiation].*

**Product description:** *Users begin with [input]. The product [core mechanic] and produces [output]. Before [critical step], they can [review, correct, or approve].*

**Use case:** *When [trigger], [role] uses the product to accomplish [job]. Instead of [status quo], they get [verifiable result].*

**CTA:** *[Action + value exchange]*, e.g. "Request beta access for your research team."

## Pre-launch FAQ

At minimum, check: what already works today; who can participate; how participants are selected; when a response or access can be expected; which platforms/integrations are supported; whether there are costs; what data is processed for sign-up and use; whether content is used for model training; how data can be deleted; how feedback is used; what support beta participants receive; how participation can be ended; and where security or technical questions can be clarified.

# 7. Conversion and Waitlist Strategy

## CTA principles

A pre-launch CTA is compelling when it conveys four elements: **action** (what happens on click), **value exchange** (what the person receives), **commitment** (how much effort follows), and **expectation** (access, selection, or a response).

Better CTA concepts: "Notify me when public beta launches," "Apply for the research beta," "Watch the 90-second workflow," "Request a design-partner conversation," "Get monthly build updates," "Check pilot fit for your team," "Discuss the use case with the team."

## Choosing the right conversion model / one or two CTAs

The correct conversion model depends on what signal the company actually needs — a broad waitlist for top-of-funnel reach, a beta application for fit and cohort quality, a design-partner inquiry for sustained collaboration with a small number of highly relevant users. The mistake is treating all three as equivalent or placing them side by side with equal visual emphasis: choice overload weakens routing.

**Only one primary CTA** when traffic comes from a focused campaign, a single ICP is addressed, conversion is low-friction, and no meaningful alternative intent exists.

**Two differentiated CTAs** when visitors have different maturity levels, self-serve and high-touch paths exist in parallel, or "understand the product" and "request access" are genuinely different tasks. The secondary CTA should be visually weaker and semantically different.

## Three conversion models

| Model | Best use case | Typical fields | Main benefit | Main downside |
|---|---|---|---|---|
| **A — Broad waitlist** | Prosumer, horizontal tools, already-clear product benefit | Email; optionally role or main interest | Low friction, more volume, wide reach | Weak qualification; high volume, low intent |
| **B — Qualified beta** | B2B SaaS or AI workflow product | Work email, role, team size, current workflow, main problem, willingness to participate | Better cohort quality | More drop-off; too much friction before sufficient motivation |
| **C — Design partner** | High-trust, complex, enterprise or workflow-heavy product | Company, role, problem, current process, urgency, sponsor, implementation capacity | Strongest learning signal | Highest friction; custom development risk for non-representative customer |

**Model A details:** Success state should confirm the sign-up, expected communication rhythm, and unsubscribe option. Metrics: view → start → submit, source, confirmed email, later activation.

**Model B details:** Use conditional questions instead of a uniformly long form; explain requirements and approximate effort in advance. Success state should cover the selection process, response window, test scope, and privacy. Metrics: qualified applications, ICP fit, interview rate, invite acceptance, activation. NN/g's form-simplification guidance and the UK Government Design System's "one thing per page" pattern both apply here: break large forms into logical steps, one question or coherent topic block per step, each explaining why the information is needed — this is especially helpful on mobile. [design-system.service.gov](https://design-system.service.gov.uk/patterns/question-pages/) [nngroup](https://www.nngroup.com/articles/eas-framework-simplify-forms/)

**Model C details:** Next step should be a 30-minute discovery call, not immediately a "sales demo." Value exchange: early access, influence, support, defined terms. Commitment: regular sessions, data/workflow access, a clear timeframe. Metrics: qualified conversations, problem strength, mutual commitment, pilot start, usage.

## Thank-you flow and follow-up

The conversion flow is not finished at submit. Immediately after submission, the page should provide:

- Visible confirmation not solely dependent on email
- A summary of the next step and realistic response/invitation logic
- A link to privacy information
- The ability to correct information or withdraw the request
- Optionally, a calendar booking (if conversations are actually offered) or one relevant question/demo — but no second mandatory form

A weak thank-you page wastes intent by offering only generic gratitude. Follow-up sequence: (1) immediate transactional confirmation, (2) qualification/scheduling request only if needed, (3) substantive product updates at an announced frequency, (4) invitation with concrete onboarding, (5) a message if access is not possible or significantly delayed.

## Gamification

| Mechanic | Sensible when … | Problematic when … |
|---|---|---|
| Referral | The product has a genuine network effect | Referral only generates ranking points |
| Invite system | Capacity increases in waves | Artificial scarcity without a reason |
| Queue position | Order is actually relevant | Position is changed arbitrarily |
| Progress bar | There are multiple necessary steps | A short flow is artificially extended |
| Quiz | Improves routing or eligibility | Entertaining data collection without purpose |
| Application | Lead quality is operationally necessary | Selection criteria remain hidden |
| Limited spots | Support or infrastructure is limited | The number is made up or permanently "almost full" |

## Measurement with low traffic

Don't adopt universal conversion benchmarks. Instead: define the hypothesis and desired signal before launch; consider traffic source and ICP fit separately; report absolute funnel steps; investigate drop-offs qualitatively; use a short on-page question or interviews; code application quality; observe response and appointment rates; track invite acceptance and actual usage; test messaging variants sequentially rather than with underpowered A/B tests.

A sensible **evidence ladder** ranges from a click and email, through completed qualification and interview, to pilot, time commitment, or payment. The higher the commitment, the smaller the volume typically may be without the signal becoming meaningless. **[X]**

# 8. Trust, Transparency, and Legal UX

## Legitimate pre-launch proof

Pre-launch companies often lack customer volume, case studies, or mature review ecosystems — that does not mean they lack trust assets, but that they need to use earlier-stage forms of proof honestly.

| Proof type | Good use | Disclosure |
|---|---|---|
| Founder credibility | Relevant domain, research, or product expertise | Concrete role and experience |
| Design partner | Active joint development | Explicitly "design partner" |
| Pilot customer | Real testing in a defined context | Pilot status, possibly an approved quote |
| Advisor | Domain-specific advice | Actual relationship and area |
| Research validation | Method or component was reviewed | Source, scope, and limitations |
| Technical validation | Benchmark, audit, or open-source artifact | Methodology and version |
| Waitlist dynamics | Demand is real and the number current | No confusion with active users |
| Community | Real members or contributions | Understandably defined metric |
| Media mention | Editorial mention is relevant | Link to the original |
| Team | Real people and contact options | No stock portraits |

Social proof works because people use others' behavior as a decision cue, but it should not be stated more strongly than the underlying relationship allows. [nngroup](https://www.nngroup.com/videos/social-proof-ux/) Baymard's research on perceived security shows that reassurance is highly contextual and sensitive to presentation: users feel more confident when trust cues sit near the moment of risk or submission, but self-made-up symbols are much weaker than real third-party verification. The practical implication is that trust copy must be both **specific and proximate** — privacy reassurance belongs near forms, and data claims should link to deeper explanations rather than staying abstract.

## Problematic trust claims

Avoid unless verifiable: "Enterprise-grade security," "GDPR compliant" as a blanket seal of approval, "100% secure," "No hallucinations," "Bias-free," "Fully autonomous," "Human-level accuracy," "SOC 2 compliant" before a completed matching certification, "Trusted by" for mere conversations, customer numbers mixing waitlist/test accounts/active usage, logos without approval, and testimonials from people without product experience. Phrases like "enterprise-grade security," "trusted by," or "AI-powered insights" are not inherently false, but without concrete anchors they become **trust debt** — users distinguish sharply between self-asserted signals and externally or concretely substantiated proof.

## Trust modules and AI trust

For an early AI/B2B product, a compact trust page is often sufficient, covering: responsible company and security contact; data categories and processing purposes; data flow and storage region; subprocessors; deletion and retention logic; encryption and access control (as far as implemented); training policy; incident contact; status of audits or certifications without faking them; and clear "not yet" statements.

For AI specifically, trust requires more than a polished page. NIST recommends integrating trustworthiness considerations — privacy, transparency, explainability, safety, accountability — directly into AI systems, and NN/g's current AI research names transparency, control, consistency, and support-when-the-system-fails as the practical trust fundamentals. AI explanations and disclaimers are most effective in plain language, paired with clear user action rather than abstract caveats. [nvlpubs.nist](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)

A complete trust center (bundling controls, subprocessors, and accessible security documents, as Vanta's model does) only becomes necessary once buyers are expected to run security reviews independently — for very early startups an empty trust center can simulate maturity instead of building trust. [vanta](https://www.vanta.com/collection/trust/what-is-a-trust-center)

## Germany and the EU

**Not legal advice:** the specific compliance obligations depend on legal form, target market, business model, data processing, and the actual service, and should be reviewed by a lawyer.

Practical minimum:

- **Imprint:** For commercial digital services, provider identification must be easily recognizable, directly accessible, and permanently available (§ 5 DDG). [bmjv](https://www.bmjv.de/SharedDocs/FAQ/DE/FAQ_Database/Onlineplattformen_Schutzregelungen/FAQ-Onlineplattformen_Schutzregelungen-008.html)
- **Privacy policy:** reflect the forms, newsletter, hosting, analytics, video, calendar, and CRM services actually used.
- **Data minimization:** GDPR principles require lawful, fair, and transparent processing — collect only data required for the stated purpose, and define retention periods. [commission.europa](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en)
- **Form transparency:** purpose, recipient/services used, and the relevant follow-up type must be understandable.
- **Newsletter separation:** don't merge product inquiries and marketing communication into one blanket consent.
- **Consent:** where required, must be freely given, specific, informed, unambiguous, and distinguishable from other matters, written in clear language; non-essential tracking/marketing technologies load only after effective opt-in, and declining must be as easy as consenting. [bfdi.bund](https://www.bfdi.bund.de/DE/Buerger/Inhalte/Telemedien/Cookie-Banner.html)
- **Withdrawal:** make consent and newsletter settings easily accessible and practically usable to refuse or later withdraw.
- **Third parties:** include video, calendar, chat, and form embeds in the script and privacy inventory.
- **Accessibility:** since June 28, 2025, the BFSG (German Accessibility Reinforcement Act) covers certain consumer-facing products/services; applicability to a pre-launch or purely B2B page must be reviewed separately. [fgvw](https://www.fgvw.de/en/news/digital-law-the-new-german-accessibility-reinforcement-act-how-will-this-affect-website-operators/)

## Privacy-friendly analytics

For low-traffic pre-launch sites, privacy-friendly analytics often provide more than enough signal while reducing consent burden. Plausible describes its standard model as cookieless, without persistent identifiers, and based on aggregated (not individually tracked) data; Matomo notes that a consent-free configuration depends on specific setup choices and jurisdictional context. [plausible](https://plausible.io/data-policy) The practical implication: simplify the analytics stack rather than loading multiple scripts whose compliance and performance cost is disproportionate to the insight gained.

## Vision and evidence

A responsible pre-launch page distinguishes: **Vision** (what is to be achieved long-term), **Hypothesis** (what the team currently assumes), **Capability** (what works today), **Evidence** (what has been tested or observed), **Commitment** (what participants actually receive), and **Unknown** (what is still open).

# 9. Benchmark Gallery

**As of:** September 2026. Most of the following pages are current product pages of already-launched companies, used explicitly as **reference patterns**, not as verified historical pre-launch snapshots. Observation and application to an earlier-stage startup are kept conceptually separate.

| Company / product | URL | Context / maturity phase | Notable pattern | Why it works or could work | Risk / limitation | Transferability |
|---|---|---|---|---|---|---|
| Linear | [linear.app](https://linear.app/) | Mature B2B product | Product-centered homepage, clear navigation into product/method/company, own product vocabulary | Connects category with concrete product-management workflows; strong hierarchy and workflow orientation make the product legible fast; about page makes position and history visible. [linear](https://linear.app/about) | Visual polish and brand recognition are hard for small teams to replicate | High for information hierarchy; low for production effort |
| Attio | [attio.com](https://attio.com/) | Mature CRM | Job-oriented / outcome-oriented structure: pipeline, deals, accounts | Capabilities are hung on real revenue workflows instead of isolated feature names. [attio](https://attio.com/) | "Agentic revenue" assumes category understanding; broad platform scope may exceed early-stage reality | High for job-based sections |
| Granola | [granola.ai](https://www.granola.ai/) | Launched AI product | Own category frame "AI notepad," human notes plus AI enrichment | Differentiates from pure transcription bots and keeps the human in the workflow; positioned by workflow, not just an AI label. [granola](https://www.granola.ai/ai-note-taker) | Strong category framing requires repeated explanation | Very high for AI messaging |
| Cursor | [cursor.com/product](https://cursor.com/product) | Launched developer tool | Real product interaction across multiple work environments; interactive demo | Shows where the agent works and what it does to a codebase instead of relying on promises. [cursor](https://cursor.com/product) | Hard to execute well without a stable product artifact; can be technically demanding | High for developer and agent products |
| Replit Agent | [replit.com/products/agent](https://replit.com/products/agent) | Launched AI-building product | Extremely direct input-output frame: describe an idea, build an app | Category and action are immediately understandable; chat is the mechanism. [replit](https://replit.com/products/agent) | Simplification can hide technical limits and quality risks | High for simple mechanism copy |
| v0 | [v0.dev](https://v0.dev/) | Launched AI web product | Product interface and entry point are nearly identical; immediate product-like interaction | Reduces the distance between marketing and product. [v0](https://v0.dev/) | Only feasible when the core workflow is immediately and safely testable | Medium to high for sandbox-capable products |
| Descript | [descript.com](https://www.descript.com/) | Mature AI media product | Category frame plus concise mechanism, "edit by editing text" | A clear mechanism doubles as differentiation, explaining benefit at once. [descript](https://www.descript.com/) | A broad feature portfolio is not a good structural model for early startups | Very high for mechanism-based positioning |
| Screen Studio | [screen.studio](https://screen.studio/) | Launched, focused product | Concrete output and tight platform positioning | "Professional screen recorder for macOS" minimizes category and audience ambiguity; high clarity from strong scope control. [screen](https://screen.studio/) | Platform focus only works with a deliberately narrow ICP | High for focused MVPs |
| Gamma | [gamma.app](https://gamma.app/) | Mature AI product | Outcome, broad category frame, immediate entry | Shows how an AI product combines generation and subsequent editing. [gamma](https://gamma.app/) | Broad category "presentations, websites and more" would be too diffuse for an unknown startup | Medium |
| Notion AI | [notion.com/product/ai](https://www.notion.com/product/ai) | AI within an established workspace platform | AI anchored in the existing work context | "Built-in teammate" operationalized via concrete objects: pages, tasks, databases. [notion](https://www.notion.com/product/ai) | Benefits massively from existing category/brand awareness | High for "AI inside workflow," low as proof |
| Tana | [tana.inc](https://tana.inc/) | Public since Feb 2025; previously waitlist/invite model | Waves of invitations plus existing users as an additional access channel | Instructive example of controlled access and community amplification. [x](https://x.com/tana_inc/status/1582462065066663938) | An invitation system can place social exclusivity above actual benefit | Medium; only for capacity-driven cohorting |
| Arc Browser | [arc.net](https://arc.net/) | Launched; Windows beta historically had a waitlist | Strong future product vision plus staged, platform-specific rollout | Invitations sent in limited batches for the Windows beta, technically justified. [techcrunch](https://techcrunch.com/2023/12/11/arc-browser-launches-its-windows-client-in-beta/) | Consumer hype and broad reach barely transfer to early B2B | Medium for platform betas |
| Vanta Trust Center | [vanta.com/products/trust-center](https://www.vanta.com/products/trust-center) | Mature B2B trust product | Security information as an independent buyer journey | Shows how compliance, controls, and evidence can be deepened from the marketing page; good model for buyers needing deeper validation. [vanta](https://www.vanta.com/products/trust-center) | For very early startups, an empty trust center can simulate maturity instead of building trust; too heavy without real security material | High for structure, low for early scope |

## Transferable patterns

- **Mechanism as differentiation:** Descript, Granola, Replit
- **Product interface as evidence:** Cursor, v0, Linear
- **Narrow category positioning:** Screen Studio
- **AI within an existing workflow:** Notion AI, Granola
- **Controlled rollout / credible sequencing:** Tana, Arc
- **Deepenable trust journey:** Vanta
- **Job-based navigation:** Attio

# 10. Anti-Pattern and Blind-Spot Catalog

The most common weakness in self-designed pre-launch sites is a **polished but low-information hero** — an abstract headline, decorative motion, and a generic waitlist CTA, while omitting category, use case, mechanism, and current status. The page looks current but forces the visitor to infer the business proposition. A second frequent issue is **borrowed SaaS credibility language** ("enterprise-grade security," "trusted by," "AI-powered insights") which is not inherently false but, without concrete anchors, becomes trust debt.

| Anti-pattern | Diagnosis | Risk | Justifiable exception | Improvement |
|---|---|---|---|---|
| Unclear product category | After the hero it's still unclear what the product is | High cognitive load, low relevance matching | Deliberately new category with explained comparison | Name a known category frame plus differentiation |
| Beautiful, empty hero | Strong visual identity, weak product explanation | Interest without understanding | Teaser campaign with an already-known brand | Add category, target audience, outcome, and mechanism |
| AI buzzwords | "Agentic," "intelligent," "next-gen" without examples/action | Interchangeability and distrust | Expert audience with established term meaning | Show the AI task, inputs, outputs, and limits |
| Feature list without benefit | Many features, no job context | Visitor must derive the benefit themselves | Technical evaluation page | Map feature → capability → outcome |
| Missing target audience | "For all teams" | Low identification | Horizontal consumer utility | Name the primary entry context |
| No product demonstration | Only illustrations or claims | Maturity and mechanism remain unclear | Product consists mainly of an invisible API | Show output, diagram, or example workflow |
| Premature social proof | Logos without relationship type | Loss of credibility | Publicly documented partnership | Cleanly separate pilot, advisor, investor, and customer |
| Worthless waitlist | CTA explains no value exchange | Low intent quality, low-quality leads | Very short teaser phase | Promise access, updates, or co-creation |
| Conflicting CTAs | Demo, waitlist, newsletter, contact all equally strong | Decision paralysis, diluted routing | Multiple clearly separated personas | One primary path, one secondary learning path |
| Effect overload | Multiple animations/effects compete | Attention pulled away from the message | Experimental brand installation | Require a functional justification for each motion |
| Weak mobile adaptation | UI screenshots/cards only scale down, unreadable | Major comprehension loss | Purely desktop-based enterprise acquisition, still not ideal | Recompose the mobile story |
| Missing beta transparency | Product looks available but ends in a waitlist | Feeling of deception / bait-and-switch | Short, explicitly announced launch campaign | State status in the hero and before the CTA |
| No privacy logic | Unclear what happens with email or product data | Legal and psychological risk | No data collection at all | Purpose notice, privacy link, deletion path |
| Overloaded navigation | Many empty or generic pages | Diluted main path, weak focus | Multiple validated segments / mature multi-stakeholder sales motion | Prioritize pages by real visitor questions |
| No follow-up plan | Submission ends at "Thanks" | Intent decays immediately | Purely anonymous survey | Confirmation, timeframe, and next step |
| Inaccessible form | Placeholder labels, invisible errors, no focus | Exclusion and abandonment | No sensible exception | Native controls, labels, text errors, keyboard test |
| Template SaaS aesthetic | Interchangeable gradient orbs, logo marquee | Low recognizability | Very early smoke test | An own brand principle and real product artifacts |
| Vision without problem-solving | Mission dominates, workflow is missing | Lack of relevance | Mission-led organization with a known activity | Anchor vision to a concrete problem and mechanism |
| Details without narrative | Technical feature density directly in the hero | No strategic framing | API/docs landing page | Job and outcome first, then technical depth |
| Fake roadmap precision | Exact dates despite high uncertainty | Later loss of trust | Contractually secured rollout | Communicate direction, status, and dependencies |
| Empty security language | "Secure by design" without substance | Increases rather than reduces skepticism | Short label with a direct deep link | Name concrete controls and open status |
| False scarcity | Permanent countdown or unjustified limited spots | Manipulative conversion | Real support or infrastructure limit | Explain the capacity reason and selection process |

# 11. Prioritized Master Checklist

**Priorities:** P0 = mandatory before publication, P1 = before active acquisition, P2 = after initial validated signals.

| Area | Check question | Priority | Expected benefit | Effort |
|---|---|---:|---|---|
| Strategy | Is the primary website job defined for the current maturity phase? | P0 | Focus and measurability | low |
| Strategy | Is a primary ICP or a primary usage context named? | P0 | Relevance | low |
| Strategy | Is it clear which behavior counts as a strong validation signal? | P0 | Better decisions | low |
| Strategy | Does conversion friction match the needed signal quality? | P0 | Lead quality | low |
| Strategy | Are vision, current capability, and planned functionality separated? | P0 | Credibility | medium |
| Information architecture | Is the homepage understandable without unnecessary page depth? | P0 | Lower orientation cost | medium |
| Information architecture | Does every navigation page answer a real visitor question? | P1 | Fewer empty pages | low |
| Information architecture | Are legal, privacy, and contact information permanently findable? | P0 | Trust and compliance | low |
| Information architecture | Is secondary detail progressively deepened? | P1 | Clarity without superficiality | medium |
| Information architecture | Are there no empty blog, careers, or changelog sections? | P1 | Higher credibility | low |
| UI/UX | Does the hero communicate category, benefit, mechanism, and status? | P0 | First understanding | medium |
| UI/UX | Is there only one visually dominant CTA? | P0 | Action focus | low |
| UI/UX | Does the page show a credible product artifact? | P0 | Product transparency | medium |
| UI/UX | Is the visual hierarchy understandable even without animation? | P0 | Robustness | medium |
| UI/UX | Are mobile hero, product visual, and CTA tested separately? | P0 | Mobile conversion | medium |
| UI/UX | Do text, controls, and states meet sufficient contrast? | P0 | Readability and accessibility | low |
| UI/UX | Do interactive elements have visible hover, focus, active, disabled states? | P0 | Usability | medium |
| UI/UX | Does motion respect `prefers-reduced-motion`? | P1 | Accessibility | low |
| UI/UX | Does every decorative pattern have a clear brand function? | P2 | Differentiation | medium |
| Content | Can a person correctly restate the product, target audience, and next step? | P0 | Messaging clarity | low |
| Content | Does copy describe outcomes and the underlying mechanism? | P0 | Credibility | medium |
| Content | Are generic AI and SaaS clichés removed? | P0 | Differentiation | low |
| Content | Are all numbers, logos, and testimonials verifiable? | P0 | Trust protection | medium |
| Content | Are use cases phrased as trigger, job, and outcome? | P1 | Situational relevance | medium |
| Content | Does beta communication explain availability, selection, and limits? | P0 | Expectation management | medium |
| Conversion | Does the CTA convey action, value exchange, and expectation? | P0 | More qualified conversions | low |
| Conversion | Does the form ask only for currently necessary data? | P0 | Less friction and data risk | low |
| Conversion | Are labels, help text, and error messages understandable? | P0 | Completion rate and accessibility | medium |
| Conversion | Does the success state work independently of email delivery? | P0 | Security and orientation | low |
| Conversion | Is there a defined follow-up process? | P0 | Activation | medium |
| Conversion | Are funnel and lead quality tracked by source? | P1 | Better interpretation | medium |
| Trust / legal | Are team, company, and contact real and findable? | P0 | Sender trust | low |
| Trust / legal | Does the privacy policy describe the actual tool stack? | P0 | Transparency | medium |
| Trust / legal | Are non-essential trackers blocked before consent? | P0 | Privacy | medium |
| Trust / legal | Are AI data usage, human control, and limits explained? | P0/P1 | Risk reduction | medium |
| Trust / legal | Are security claims limited to implemented measures? | P0 | No overpromising | low |
| Technical quality | Do the core paths work on desktop, mobile, and keyboard? | P0 | Usability | medium |
| Technical quality | Are images, videos, fonts, and third-party scripts optimized? | P0 | Load time | medium |
| Technical quality | Are timeout, API error, duplicate submit, and offline states handled? | P0 | Conversion robustness | medium |
| Technical quality | Are Lighthouse/lab checks supplemented by real device and task testing? | P1 | Fewer blind spots | medium |

# 12. Conclusion: A Pragmatic Pre-Launch Minimum

A small startup does not need a launch-grade marketing machine before launch. It does, however, need a site that is strategically honest and operationally complete enough to create understanding, trust, and a usable next step.

## Required before launch

1. **A clearly defined positioning:** understandable category, primary target audience, concrete job, and credible mechanism.
2. **A focused homepage:** hero, problem context, how it works, product evidence, use cases, status, trust, FAQ, and final CTA.
3. **A real product artifact:** screenshot, prototype flow, example output, or short demo.
4. **A fitting conversion flow:** broad waitlist, qualified beta, or design-partner path — not all at once.
5. **Honest expectation management:** what works, what doesn't, who gets access, and what happens afterward.
6. **Basic trust:** a real team or responsible company, contact option, and verifiable expertise.
7. **Legal and privacy foundations:** imprint, matching privacy policy, and technically correct consent behavior.
8. **Minimum technical quality:** usable on mobile, keyboard-operable, high-contrast, fast, and robust against form errors.
9. **A measurement and learning logic:** funnel events, traffic source, ICP fit, and qualitative follow-ups.
10. **An operational follow-up process:** a website should not collect leads that the team can neither answer nor activate.

## Only after validated interest

Elaborate resource hubs / extensive blog and SEO clusters, many role- or industry-specific landing pages, a complete trust center, advanced interactive product demos, referral and queue systems, complex personalization, a pronounced motion/3D system, a detailed public roadmap, public changelogs, an extensive customer-story library, A/B-testing infrastructure for low traffic volumes, and enterprise sales/pricing architecture. These elements become useful once meaningful demand, active beta usage, or multi-stakeholder sales complexity has been validated.

The right pre-launch standard is therefore **not "as small as possible,"** but rather **as small as possible while achieving complete understanding, an honest status, resilient trust, and a functioning learning path.** The state-of-the-art benchmark is not maximum surface sophistication — it is a disciplined combination of clarity, trust calibration, evidence, and readiness that matches the product's true stage while still making the future product feel concrete and worth following.
</content>