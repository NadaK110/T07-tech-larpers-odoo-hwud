# BuildOdoo 2026 — Team Catch-Up Summary

## Where we are

- Odoo 19.0 is set up and running locally (via the setup script + VS Code).
- We're doing **Track 3 — Open Innovation**: a **Student Freelance/Gig Marketplace**.
  - Students post small gigs (tutoring, design, errands, etc.)
  - Other students apply to them
  - AI auto-categorizes gig postings from their description (planned feature)
- The `estate` and `estate_accounts` folders (from the intro workshop) are our starting
  point / reference for how Odoo modules are structured — **not** our actual project.
- Our custom modules will live alongside those, in the same `workshop/Workshop` folder.

## What's been done so far

1. Odoo server installed and running locally, confirmed working at `localhost:8069`.
2. Logged into Odoo with our own admin login (database name: `admin`).
3. Created a shared GitHub repo for the project:
   **https://github.com/NadaK110/T07-tech-larpers-odoo-hwud**
4. Pushed the existing `estate` and `estate_accounts` folders to that repo as a starting commit.
5. You should each be getting (or have gotten) a **GitHub collaborator invite** to this repo — accept it.

## What you need to do after accepting the GitHub invite

1. **Make sure Odoo is already running on your own Mac** (following the same setup guide
   everyone used) — this repo doesn't include the Odoo core itself, only our custom module code.

2. **Clone the repo** onto your Mac. Open Terminal and run:
   ```bash
   git clone https://github.com/NadaK110/T07-tech-larpers-odoo-hwud.git
   ```
   You can run this in any folder you like — it doesn't need to be inside `odoo-server`.

3. This will download a folder called `T07-tech-larpers-odoo-hwud/` containing `estate/`
   and `estate_accounts/`. Take a look inside — that's the reference module structure
   (models, views, security files) we'll be copying the pattern from for our own module.

4. **Don't edit directly on the `main` branch.** When you start building your part, create
   your own branch first:
   ```bash
   git checkout -b yourname-feature
   ```
   Work there, commit as you go, then open a Pull Request on GitHub when it's ready to merge
   into `main`. This avoids overwriting each other's work.

5. Wait for the actual gig-marketplace module skeleton (models, views, manifest) — coming
   next, will be added to the repo so everyone can pull it and start building their piece.

## Data model (planned)

- **`gig.posting`** — a job someone wants done (title, description, category, budget,
  deadline, status, linked applications)
- **`gig.application`** — someone applying to a gig (linked gig, applicant, message, status)
- AI feature: auto-suggest a gig's category from its description text (LLM API call)

## Questions / blockers?

Ping the group chat — don't struggle alone for more than ~20-30 min on a setup issue,
just ask.
