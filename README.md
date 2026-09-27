# BuildOdoo 2026 — Student Freelance/Gig Marketplace

**Track:** Track 3 — Open Innovation
**Event:** Odoo × HW Tech Club BuildOdoo 2026 Hackathon
**Repo:** https://github.com/NadaK110/T07-tech-larpers-odoo-hwud

## What we're building

A platform where students post small gigs (tutoring, design work, errands, etc.) and
other students apply to them. An AI feature auto-categorizes gig postings based on their
description, and (stretch goal) helps match applicants to relevant gigs.

## ⚡ Current Status (updated)

| Task | Owner(s) | Status |
|---|---|---|
| Task 1 — Backend: `gig.posting` model + module setup | Nada | ✅ Done |
| Task 2 — Backend: `gig.application` model + Applications tab | Nada | ✅ Done |
| Task 3 — Frontend/Views (list, kanban, search, form polish) | Zuha | 🔄 In progress (50%) |
| Task 4 — AI categorization integration | Shayaan, Irina, Madiha | 🔲  Started | Irina & Shayaan working 
| Presentation / demo prep | **OPEN — needs an owner** | 🔲 Presentation by Irina DONE ✅ | Nada will do Demo Video editing 

## Getting started (for teammates joining now)

1. Make sure Odoo is running locally on your own machine (setup guide from before the
   hackathon). This repo only holds our custom module code, not the Odoo core itself.

2. Clone this repo:
   ```bash
   git clone https://github.com/NadaK110/T07-tech-larpers-odoo-hwud.git
   ```

3. Pull the latest before you start working, every time:
   ```bash
   git pull --no-rebase
   ```

4. Our module lives in `gig_marketplace/` (alongside the `estate` and `estate_accounts`
   reference modules from the intro workshop — those are just examples, not our project).

5. **Don't commit straight to `main` without pulling first** — a few of us hit a
   divergent-branch issue already today. Always `git pull --no-rebase` before you start
   editing, and again before you push.

## What's already working

- You can create a "gig" (title, description, category, budget, deadline, status)
- Gigs show up in a Kanban board grouped by status, plus a list view with filters
- Opening a gig shows a status bar (Open → In Progress → Completed) and a polished form
- An **Applications tab** on each gig lets you add applicants, their message, and status
  (Pending/Accepted/Rejected) — tested and working

## What's NOT done yet — where to focus

**Task 4 (Shayaan, Irina, Madiha) — AI Categorization**
- Write a function that takes a gig's `description` text and returns a suggested
  `category` COMPLETE
- Hook it into `gig.posting` so the category auto-fills when a gig is created/saved
- Test it against several different gig descriptions (tutoring, design, errands) to make
  sure it's actually accurate
- Shayaan and Irina working on 2 more features


**Task 3 (Zuha) — remaining 50%**
- Check in with Zuha on what's left — likely refinements to existing views, and possibly
  the Applications tab UI could use polish (accept/reject buttons instead of manually
  editing the status dropdown, for example)

**Presentation / Demo Prep — OPEN ROLE**
Whoever picks this up should:
- Create realistic sample gigs and applications (8-10+) so the app looks like an active
  marketplace, not just test data
- Test the full user journey end-to-end (post a gig → apply → accept/reject) and flag any
  bugs to whoever owns that part
- Write a short demo script/walkthrough (aim for 2-3 minutes)
- Set up shared slides (problem, solution, how it works, tech stack, impact) — pull a
  couple of lines from each teammate about the part they built
- Note: this doesn't have to be one person — presenting itself is a team effort, everyone
  should be ready to speak to the part they built. This role is about coordinating and
  making sure it all comes together.

## Data model (for reference)

**`gig.posting`**
- `name`, `description`, `poster_id` (→ res.partner), `category`, `budget`, `deadline`
- `state`: Open / In Progress / Completed / Cancelled
- `application_ids` (One2many → gig.application)

**`gig.application`**
- `gig_id` (→ gig.posting), `applicant_id` (→ res.partner), `message`
- `status`: Pending / Accepted / Rejected

## Timeline reminders

- **Submission deadline:** Monday 28th September, 12 PM
- **Presentation:** Wednesday 30th September, 2–4 PM

## Questions or blockers?

Ping the group chat — don't spend more than ~20–30 minutes stuck alone on a setup issue,
just ask