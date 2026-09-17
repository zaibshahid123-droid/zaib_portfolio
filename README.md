# Muhammad Zaib — Portfolio (Django + Tailwind CSS)

A dark-mode, dynamic portfolio site built with Django and Tailwind CSS (CDN).

## Features

- Hero / About / Skills / Projects / Blog / Resume / Contact — all on one flowing home page, plus dedicated pages for Projects, Blog and Resume
- `Project` model (title, description, image, tech_stack, github_url, live_demo_url, created_at)
- `Skill` model with progress bars, `BlogPost` model with slugs, `Resume` model for an uploadable PDF
- Class-based views: `ListView` for projects/blog, `DetailView` for project/blog detail pages
- Working `ContactForm` that emails you via Django's email backend (SMTP or console for local dev)
- Django admin for managing everything — no template edits needed to add a project or post
- Tailwind CSS via CDN, dark theme, responsive layout, no build step required

## Project layout

```
zaib_portfolio/
├── manage.py
├── portfolio_site/        # settings, root urls, wsgi/asgi
├── portfolio/              # the app: models, views, forms, admin, templates
│   └── management/commands/seed_portfolio.py   # optional demo data
├── templates/base.html     # site-wide layout (nav, footer)
├── static/css/custom.css
├── api/index.py            # Vercel serverless entry point
├── vercel.json
├── requirements.txt
└── .env.example
```

## 1. Run it locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env            # then edit values as needed
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_portfolio # optional: adds sample skills/project/post
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and `/admin/` to add real projects,
skills, blog posts, and upload your resume PDF.

Without SMTP credentials set, the contact form prints the email to your
terminal (the console email backend) — good enough to test the flow locally.

## 2. Set up the contact form email (Gmail example)

1. Turn on 2-Step Verification on your Google account.
2. Create an **App Password**: https://myaccount.google.com/apppasswords
3. In `.env` (or your host's environment variables), set:
   ```
   EMAIL_HOST_USER=zaibshahid123@gmail.com
   EMAIL_HOST_PASSWORD=<the 16-character app password>
   DEFAULT_FROM_EMAIL=zaibshahid123@gmail.com
   CONTACT_RECEIVER_EMAIL=zaibshahid123@gmail.com
   ```
   Once `EMAIL_HOST_USER` is set, `settings.py` automatically switches from the
   console backend to real SMTP.

## 3. Deploying

### ⚠️ A note on Vercel + Django

Vercel is built around serverless functions and static sites, not long-running
servers — so it works for Django, but with real trade-offs worth knowing before
you commit to it:

- **SQLite won't persist.** Vercel's filesystem is read-only/ephemeral per
  request, so you need an external database — a free Postgres instance from
  [Neon](https://neon.tech), [Supabase](https://supabase.com), or
  [Railway](https://railway.app) works well. Set its connection string as
  `DATABASE_URL`.
- **Uploaded media (project images, your resume PDF) won't persist either** —
  for the same reason. Use a service like Cloudinary, or an S3-compatible
  bucket, for `MEDIA` storage, or keep images as static files you check into
  the repo instead of uploading through the admin.
- Cold starts and request timeouts apply, as with any serverless function.

This repo includes `vercel.json` and `api/index.py`, which route all traffic
through Django's WSGI app as a serverless function — this is the same pattern
your existing e-commerce project on Vercel likely uses. Steps:

1. Push this repo to GitHub.
2. Import it in the Vercel dashboard, or run `vercel` from the project root.
3. In Vercel's Project Settings → Environment Variables, add everything from
   `.env.example` (`SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`,
   `CSRF_TRUSTED_ORIGINS` set to your `*.vercel.app` domain, `DATABASE_URL`,
   and the `EMAIL_*` variables).
4. Before your first deploy (or via a one-off script), run migrations against
   your external Postgres database — Vercel won't run `migrate` for you:
   ```bash
   DATABASE_URL=<your-neon-or-supabase-url> python manage.py migrate
   ```
5. Deploy. Static files are collected via `python manage.py collectstatic`
   (add this as part of your build, or run it locally and commit
   `staticfiles/` since `vercel.json` serves that folder directly).

### Simpler alternative: Render or Railway

If you'd rather avoid the serverless workarounds above, **Render** or
**Railway** both offer free tiers with a normal, persistent Django + Postgres
setup (no separate media/storage service needed to get started) — just point
Gunicorn at `portfolio_site.wsgi:application` and set the same environment
variables. Worth trying if you hit friction on Vercel.

### GitHub

You can absolutely host the *code* on GitHub (GitHub is free for any public
or private repo). GitHub Pages itself only serves static files, though — it
can't run Django. What your friend likely did is push the code to GitHub and
then deploy it *from* GitHub to a platform like Vercel/Render/Railway, which
build and run it from the connected repo. That's the same flow described
above.

## 4. Adding content

Everything is managed from `/admin/`:

- **Projects** — add title, description, image, comma-separated tech stack,
  GitHub URL, live demo URL. Mark one or more as "featured" to control what
  shows on the home page.
- **Skills** — name, category, and a 0–100 proficiency used for the progress
  bar width.
- **Blog posts** — title (slug is auto-generated), summary, content, optional
  cover image. Uncheck "published" to keep a draft hidden.
- **Resume** — upload a PDF; it's shown inline and offered as a download on
  the `/resume/` page.

## 5. Adding social links

`portfolio/context_processors.py` currently has empty placeholders for
`LINKEDIN_URL`, `TWITTER_URL`, `INSTAGRAM_URL`, and `FACEBOOK_URL`. Fill those
in (or move them to environment variables like `GITHUB_URL`) once your
accounts are ready, and they'll automatically appear in the footer.
