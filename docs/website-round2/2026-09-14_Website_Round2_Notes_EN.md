# Website Round 2 — Notes and Open Decisions

**As of:** September 14, 2026
**Reviewed version:** Commit `58abbc4` (merge of `rework/design-2026`, September 12)
**Staging:** https://stage.weltvorstellung.de

All figures below were recounted against the current state, not estimated.

---

## 1. The one rule almost everything else follows from

**Images either serve a function or they go.**

Concretely, that means three things:

1. **At most one to two AI images per page.**
2. **No image without a caption or a recognizable content anchor.** An image that is neither named nor anchored reads as decoration and drags down the page's credibility.
3. **Mood and thematic images belong on the homepage and the Philosophy page.** They have no place on any other page.

The current state sits well above that:

| Page | AI images now | Target |
|---|---:|---:|
| Homepage | 5 | 1–2 |
| Philosophy | 4 | see point 3 |
| Team | 1 | 0 |
| Development Status | 1 | 0 |
| Beta (new) | 1 | open |

---

## 2. Page-specific consequences

### Homepage

In the section "A clear path, not a vocabulary list", **two images with no caption whatsoever** sit side by side, directly before the dark quote band. Both are marked up as `<figure>` but have no `<figcaption>`. **Please remove them without replacement.**

For context: that leaves three more AI images on the homepage (arena motif in the hero, corridor insert, palm causeway in the closing band). If the "one to two per page" rule is to hold, at least one of those has to go as well. **Decision needed: which of the three stays?**

### Philosophy

Same pattern, same problem: **two disconnected images** immediately after the table of contents, also uncaptioned. On top of that, two more AI images sit in bands of their own across the page — four in total.

The counter-proposal: **one header image per essay section.** This is not a cutback but a different structure. The page has eight sections, so eight header images, each locked to its heading instead of floating freely between paragraphs. **Decision needed: do we take this route, and who produces the eight motifs?** Until then, the four existing images should be removed, since they appear in neither target state.

### Development Status

One AI image sits without motivation in the section "Funding phase: June 2026 to May 2027". **Remove it for now.**

The **DACH map** in the long-term outlook section is explicitly not affected. It is not an AI image but the map asset that had been requested, and it carries information.

### Team

All five portraits are still placeholder graphics. The goal is **information parity**: either everyone has a photo or no one does.

**Please collect portrait photos of all team members in time for the StromGold meeting.** I am coordinating the meeting itself and will communicate the exact deadline in good time. If the photos are not complete by then, we remove the image column entirely and switch the cards to plain text. A team where three people have a photo and two don't looks less finished than a team with no photos at all.

The band with the antlers-and-city motif on the Team page also falls under point 1 and should go.

---

## 3. What we need from you

**Partner logos from your Berlin network.** The logo ticker on the homepage currently shows three confirmed logos: StromGold, Potsdam Transfer Startup Service, and Gründen in Brandenburg. The six placeholder tiles have been removed, so the ticker is honest but thin. For a credible impression we need more logos with cleared usage rights.

**Portrait photos of all team members**, as above. Collecting them within the team makes most sense through you; the date and deadline sit with me.

---

## 4. Structure

### Mailing list reference on every page

The footer of every page should carry an element that guides visitors to the waitlist. The existing closing band from Development Status serves as the template.

Verified: the band currently exists **only on Homepage and Development Status**. It is missing on **Philosophy, Team, Imprint, Privacy Policy, and the new Beta page**.

For Imprint and Privacy Policy, a moment's thought, please: a promotional element on a legally required page is permissible but looks sloppy. Proposal: leave it out there, add it to the other three. **Your decision.**

### Waitlist

The page is still in the old blog layout and technically decoupled from everything else: **its own stylesheet instead of the shared one**, and **its own language switcher** that is not the same component as on the other pages. It is the only page outside the design system.

This is the page where personal data is collected — in other words, the one that should look the least improvised. It needs a rework into the new format. One of the images removed above can be meaningfully reused there.

---

## 5. Noticed while reviewing, not covered in the notes

**There is a new page `beta.html`**, created during the design rework. It is **not linked from any other page** and therefore practically unreachable. Intention or leftover? If it is to stay, it belongs in the navigation; if not, it should be removed.

**The `sitemap.xml` names `weltvorstellung.de` as the production domain.** That implicitly settles something that was still open. Whether we own `disce.de` and which domain becomes the primary one remains unresolved. As long as that is the case, the sitemap cements a decision nobody made. Only five pages are listed; Imprint, Privacy Policy, and Beta are missing.

**Indexing is still fully blocked**, via `robots.txt` and additionally via a `noindex` on every single page. For staging this is correct. Before launch, both blocks must be deliberately lifted, otherwise the site goes online and stays invisible to search engines.

**Two different language switchers in circulation**, see point 4. As soon as the waitlist page is reworked, it should adopt the shared component.

---

## 6. Not touched

On this basis, **nothing has been changed**. This text is an inventory and a decision template.

**Open decisions, in the order in which they block:**

1. Portrait photos of all team members, or the decision to remove the image column entirely
2. Which of the three remaining homepage images stays
3. Header images for Philosophy: confirm the structure and resolve production
4. Mailing list band on Imprint and Privacy Policy as well, yes or no
5. `beta.html`: link it or remove it
6. Primary domain, and with it the sitemap
