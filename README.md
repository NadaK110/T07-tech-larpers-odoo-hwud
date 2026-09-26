# BuildOdoo 2026 — Student Freelance/Gig Marketplace

**Track:** Track 3 — Open Innovation
**Event:** Odoo × HW Tech Club BuildOdoo 2026 Hackathon

## What we're building

A platform where students post small gigs (tutoring, design work, errands, etc.) and
other students apply to them. An AI feature auto-categorizes gig postings based on their
description, and (stretch goal) helps match applicants to relevant gigs.

## Project status

- Odoo 19.0 set up and running locally by each team member (via the shared setup guide).
- The `estate` and `estate_accounts` folders in this repo are from the intro workshop —
  they're our **reference material** for Odoo module structure (models, views, security),
  **not** our actual project.
- Our custom marketplace module will live alongside them in this same folder.

## Getting started (for teammates joining the repo)

1. Make sure Odoo is running locally on your own machine (following the setup guide
   everyone used before the hackathon). This repo only contains our custom module code,
   not the Odoo core itself.

2. Clone this repo:
   ```bash
   git clone https://github.com/NadaK110/T07-tech-larpers-odoo-hwud.git
   ```
   Any folder on your machine works — it doesn't need to be inside `odoo-server`.

3. Look inside `estate/` and `estate_accounts/` to see how Odoo modules are structured
   (manifest files, models, views, security) before building our own.

4. **Don't commit directly to `main`.** Create your own branch for whatever you're working on:
   ```bash
   git checkout -b yourname-feature
   ```
   Commit your work there, then open a Pull Request on GitHub to merge into `main` once
   it's working. This avoids overwriting each other's changes.

## Data model (planned)

**`gig.posting`** — a job someone wants done
- `name` (Char) — title
- `description` (Text) — free text details
- `poster_id` (Many2one → res.partner) — who posted it
- `category` (Selection/Char) — auto-suggested by AI from the description
- `budget` (Float) — optional
- `deadline` (Date)
- `state` (Selection) — Open / In Progress / Completed / Cancelled
- `application_ids` (One2many → gig.application)

**`gig.application`** — someone applying to a gig
- `gig_id` (Many2one → gig.posting)
- `applicant_id` (Many2one → res.partner)
- `message` (Text) — pitch/cover note
- `status` (Selection) — Pending / Accepted / Rejected
- `match_score` (Float, optional) — for stretch-goal applicant matching

**AI feature (v1):** on creating a gig posting, send the description to an LLM API and
auto-fill the `category` field.

**AI feature (stretch):** score how well an applicant's message matches a gig's
description, and sort applications by that score.

## Team roles

| Person | Role | Responsibilities |
|---|---|---|
| Person 1 | Backend Lead (Gig Model) | Module skeleton (`__manifest__.py`, `__init__.py`), `gig.posting` model, basic security/access rules |
| Person 2 | Backend (Applications Model) | `gig.application` model, relationship to `gig.posting`, status transitions |
| Person 3 | Frontend/Views | List/form views for both models, Kanban board if time allows, menus/navigation |
| Person 4 | AI Integration | LLM API setup, category-suggestion function, hook it into `gig.posting` |
| Person 5 | Testing & Demo Prep | Sample data, end-to-end testing, coordinating the demo walkthrough |

*Note: confirm with organizers whether a 5-person team is allowed — the brief states team
size is 1–4 students.*

**Presentation:** everyone contributes — each person prepares to speak to the part they
built (their model, their views, the AI feature, testing/demo). Person 5 coordinates
pulling it together into one coherent script/slides, but the actual presenting and
content is a team effort.

## 48-hour timeline

**Day 1 AM**
- Finalize data model as a team
- Create module skeleton
- Build `gig.posting` model with basic views

**Day 1 PM**
- Build `gig.application` model
- Wire up the relationship between models
- Get a plain, ugly-but-working end-to-end flow: post a gig → apply → view it

**Day 2 AM**
- Add AI categorization feature
- Add basic access rules

**Day 2 PM**
- Polish UI (views, kanban board)
- Test full user journeys (poster + applicant)
- Prep demo: seed realistic sample data, script the walkthrough

**Submission deadline:** Monday 28th September, 12 PM
**Presentation:** Wednesday 30th September, 2–4 PM

## Questions or blockers?

Ping the group chat — don't spend more than ~20–30 minutes stuck alone on a setup issue,
just ask.
