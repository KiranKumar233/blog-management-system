# kiran-kumar-blog

**Welcome!**  
This repository contains the source code for the *Django Blogging System* by **Kiran Kumar**. This is a real-world, feature-rich blogging system built to teach practical Django — from models, templates and forms to permissions, dashboards and deployment.

---

## What you’ll learn
- Project structure & real-world folder layout  
- Models: Blog, Category, Comment, User relations, slugs, media handling  
- Forms: Create/Edit posts, user registration, comments  
- Authentication & Authorization: Login, logout, Groups, Permissions, decorators  
- Admin customizations & listings  
- Dashboards for Editors / Managers with role checks  
- Search, pagination, featured & recent posts  
- File uploads (media), static files, and templates  
- Deployment checklist and steps

This course focuses on **practical features** used in production blogging systems and how to structure code for clarity and maintainability.

---

## Features implemented
- Multi-role system (Admin / Manager / Editor / Author)  
- Create / Read / Update / Delete (CRUD) for posts & categories  
- Unique slug generation & prepopulation  
- Media (image) upload & configuration  
- Comment system (only authenticated users can comment)  
- Manager & Editor dashboards with counts and tables  
- Granular permission checks (using Django Groups & Permissions + custom checks)  
- Search feature with retained search term in textbox  
- Deployment on PythonAnywhere

---

## Requirements
- Python 3.10+ (recommended)  
- Django 4.x (see `requirements.txt`) - always use latest version 
- A virtual environment tool (`venv` / `virtualenv`)  
- PostgreSQL / MySQL or SQLite for development
- (Optional) nginx / gunicorn for production — [contact me](https://techwithrathan.com/contact/) for advanced deployments.

## 🚀 Join My 8-Week Backend Developer Program  
Become industry-ready in 8 weeks!  
👉 [Enroll here](https://techwithrathan.com/django-live/)

## ❤️ Support My Work

<a href="https://www.youtube.com/@rathankumar">
  <img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg" width="120">
</a>

If you like this project, please support me by subscribing to my channel:  
👉 **Kiran Kumar** — https://www.youtube.com/@rathankumar

All the best.

---

## Project Overview

`kiran-kumar-blog` is a production-style Django blogging system focused on real-world features needed for content-driven sites: multi-role access control, media handling, friendly URLs, dashboards for editors/managers, search and pagination, and an approachable template system based on Bootstrap.

This repository is intended as a learning reference and a starting point for building a small-to-medium blogging platform.

## Implemented Features

- **User roles & permissions**: Admin, Manager, Editor, Author roles implemented with Django Groups and fine-grained permission checks for dashboards and content actions.
- **Posts & Categories**: Full CRUD for posts and categories with unique slug generation and human-friendly URLs.
- **Media uploads**: Image uploads supported for posts (`MEDIA` configured; uploaded files stored under `media/uploads/`).
- **Comment system**: Authenticated users can comment on posts with a simple moderation flow.
- **Search & Pagination**: Search across posts with retained search term; paginated lists for recent posts.
- **Dashboards**: Simple editor/manager dashboards with counts and management actions implemented as Django views and templates.
- **Responsive templates**: Clean Bootstrap-based templates with custom CSS in `static/css/blog.css`.
- **Forms & validation**: `ModelForm` usage for create/edit flows and server-side validation.
- **Basic tests**: A few unit tests included under app `tests.py` for critical parts (models/views).

## How It's Implemented (short)

- **Models**: Core models live inside app modules (e.g., `blogs.models`) — `Blog`, `Category`, `Comment`, and auxiliary models like `About` and `SocialLink`.
- **Views**: Combination of function-based views for simple pages and class-based patterns for CRUD where helpful; dashboard views apply role checks.
- **Templates**: Stored in `templates/` and use Django template language + Bootstrap. Shared layout is `templates/base.html` and content pages extend that base.
- **Static & CSS**: Custom styles are under `static/css/blog.css`. Static files served via Django `staticfiles` during development; run `collectstatic` for production.
- **Slugs**: Unique slug generation is implemented using slugify logic in model save signals or model `save` override to ensure uniqueness.
- **Authentication**: Uses Django's built-in `auth` system; registration, login, logout flows are implemented with views and forms.
- **Search**: Implemented by filtering `QuerySet` on title/description and returning results to the search template with the search term in the input field.

## Quick start (development)

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install requirements and run migrations:

```powershell
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
```

3. Collect static files (optional for production-like testing) and run the server:

```powershell
py manage.py collectstatic --noinput
py manage.py runserver
```

Open http://127.0.0.1:8000 in your browser.

## Notes & Next steps

- The repository keeps some external links and references (e.g., video/course links) unchanged. If you'd like those updated, tell me which URLs to replace.
- If you want a full package rename (project module, app names, and imports) so the repository name is unique at the package level, I can perform that but it is more invasive and will require local testing.

If you'd like, I can also add a short `CONTRIBUTING.md`, setup a `requirements.txt` pin file, or prepare a deployment checklist for a specific host (Heroku, PythonAnywhere, DigitalOcean).