# Student Dashboard

## Running the dev server

```powershell
env\Scripts\activate
python manage.py runserver
```

## Stopping the dev server

**If running in foreground (you see the terminal):**

Press `Ctrl+C` in that terminal window.

**If running in background / you lost the terminal:**

1. Find what's using the port (e.g. 8000):

```powershell
netstat -ano | findstr :8000
```

This shows a line like `TCP 127.0.0.1:8000 ... LISTENING <PID>` — note the PID (last column).

2. Kill it by PID:

```powershell
Stop-Process -Id <PID> -Force
```

**Shortcut (find + kill in one go) for port 8000:**

```powershell
Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess | Stop-Process -Force
```

**If you know it's a Django dev server and want to kill all python processes (careful — kills ALL python):**

```powershell
Stop-Process -Name python -Force
```

> Note: `taskkill` works too, but in Git-Bash-flavored shells `taskkill /PID 1234 /F` can fail due to path translation — `Stop-Process -Id 1234 -Force` in PowerShell is more reliable.

## Development workflow for new modules

The `student` app (model, views, urls, templates) is the reference implementation.
Follow this same pattern for each new module (Teachers, Departments, Subjects, Accounts, etc.):

1. **Model first** — define fields in `[app]/models.py` to match what the existing UI
   form (`templates/[module]/_form.html` or `add.html`) already collects.
2. **Migrate** — `python manage.py makemigrations` then `python manage.py migrate`.
3. **Views** — a list view (`Model.objects.all()` passed to the template) and an add
   view (GET renders the form, POST validates/saves, then `redirect()` to the list —
   never `render()` to a URL name).
4. **URLs** — create `[app]/urls.py`, include it in `home/urls.py` **before**
   `school.urls`, and remove/adjust the matching placeholder route + view in
   `school/urls.py` / `school/views.py`. (Top-level `include()`s are matched in order —
   a leftover placeholder route in `school.urls` for the same path will silently
   shadow the real one. This bit us with the Student Add form.)
5. **Align templates** — make sure form field `name=` attributes and list-page
   `{{ var.field }}` references match the model field names exactly.
6. **Test end-to-end** — submit the form and confirm the record saves and appears
   in the list page before moving on to the next module.

`school/views.py` currently passes empty lists (`{"teachers": []}` etc.) for all
not-yet-built modules — replace these with real querysets as each model is built.

## models.py vs views.py

- **`models.py`** defines the **data structure** — e.g. `Parent` and `Student` in
  `student/models.py` describe what gets stored in the database (fields like
  `first_name`, `student_class`, `addmission_number`, and the `OneToOneField` link
  between `Student` and `Parent`). This is the schema/table definition, independent
  of any web request.

- **`views.py`** contains the **request-handling logic** — functions like
  `add_student`, `student_list`, `edit_student`, `view_student` in
  `student/views.py` that:
  - receive an HTTP request,
  - read submitted data (`request.POST`, `request.FILES`),
  - use the models to query/create/update database records (e.g.
    `Student.objects.create(...)`),
  - pick a template and return an HTML response.

Rule of thumb: **models = "what data looks like and how it's stored"**,
**views = "what happens when a user hits a URL"**. A view almost always touches a
model to read or write data, but the model itself has no idea views exist.

## Project architecture (file map)

```
home/
  settings.py   -> global config: installed apps, middleware order, database,
                    templates, static/media paths
  urls.py       -> top-level URL table (ROOT_URLCONF) — decides which app
                    handles which URL prefix
  wsgi.py       -> the entry point the web server talks to

student/        -> the "real" app (DB-backed)
  models.py     -> Student & Parent table definitions
  views.py      -> add_student, student_list, edit_student, view_student
  urls.py       -> /student/ and /student/add/

school/         -> legacy/demo app, still serves dashboards, teachers,
  views.py         departments, etc. (not yet backed by real models)
  urls.py

templates/
  Home/base.html      -> shared page shell (sidebar, header, messages, footer)
  partials/           -> reusable chunks (sidebar.html, header.html, ...)
  students/           -> add.html, list.html, edit.html, view.html, _form.html

static/           -> CSS/JS served as-is
media/            -> user-uploaded files (e.g. student profile photos)
db.sqlite3        -> the actual database file
```

## Request lifecycle: from browser click to database and back

Walking through **"fill in the Add Student form and click Save"** end-to-end:

```
Browser                Middleware            URL routing           View (student/views.py)        Database / Template
   |                        |                      |                        |                              |
   | POST /student/add/     |                      |                        |                              |
   |----------------------->|                      |                        |                              |
   |                        | Security, Session,   |                        |                              |
   |                        | Common, CSRF check,  |                        |                              |
   |                        | Auth, Messages,      |                        |                              |
   |                        | XFrameOptions        |                        |                              |
   |                        |--------------------->|                        |                              |
   |                        |                      | home/urls.py           |                              |
   |                        |                      |  -> student/urls.py    |                              |
   |                        |                      |  -> add_student()      |                              |
   |                        |                      |----------------------->|                              |
   |                        |                      |                        | request.method == 'POST'    |
   |                        |                      |                        | Parent.objects.create(...)  |
   |                        |                      |                        | Student.objects.create(...) |---> INSERT rows
   |                        |                      |                        | messages.success(...)       |---> saved in session
   |                        |                      |                        | return redirect('student_list')
   |<---------------------- 302 Found, Location: /student/ ----------------|                              |
   |                        |                      |                        |                              |
   | GET /student/          |                      |                        |                              |
   |----------------------->|--------------------->| -> student_list()      |                              |
   |                        |                      |----------------------->| Student.objects.all()       |---> SELECT rows
   |                        |                      |                        | render('list.html', {...})  |
   |                        |                      |                        |  - extends Home/base.html   |
   |                        |                      |                        |  - {% if messages %} shows  |
   |                        |                      |                        |    "Student added           |
   |                        |                      |                        |    successfully!"           |
   |<---------------------- 200 OK, full HTML page ------------------------|                              |
```

**What each middleware (in [settings.py](home/settings.py) `MIDDLEWARE`, run top-to-bottom on the way in, bottom-to-top on the way out) actually does:**

| Middleware | Role |
|---|---|
| `SecurityMiddleware` | adds security-related response headers |
| `SessionMiddleware` | loads the user's session (cookie-based) so views can read/write `request.session` |
| `CommonMiddleware` | general request normalization (e.g. URL handling) |
| `CsrfViewMiddleware` | on POST, checks the `csrfmiddlewaretoken` in the form matches the cookie — rejects with 403 if missing/invalid |
| `AuthenticationMiddleware` | attaches `request.user` |
| `MessageMiddleware` | gives views access to `messages.success(...)`, and stores queued messages in the session until the *next* page render consumes them — this is how the success message survives the redirect from step 1 to step 2 above |
| `XFrameOptionsMiddleware` | adds clickjacking-protection header |

**Key takeaway on messages**: `messages.success()` doesn't render anything immediately — it queues a message in the session. The *next* request that renders a template containing `{% if messages %}` (which we added to `Home/base.html`) pops the queue and displays it. That's why the message appears on the list page after the redirect, not on the add page itself.

## How the server starts up (WSGI boot sequence)

When you run `python manage.py runserver`:

1. **`manage.py`** sets the environment variable `DJANGO_SETTINGS_MODULE=home.settings` and hands control to Django's management command runner.
2. Django imports **`home/settings.py`** — this is the single source of truth for:
   - `INSTALLED_APPS` (which apps, including `school` and `student`, are active)
   - `MIDDLEWARE` (the ordered list above)
   - `DATABASES` (points at `db.sqlite3`)
   - `TEMPLATES` (where to look for `.html` files, plus context processors that make `messages`, `request`, and `{% url %}` available everywhere)
   - `ROOT_URLCONF = 'home.urls'` (the top-level URL table)
   - `STATIC_URL`/`MEDIA_URL` (where CSS/JS/uploaded files are served from)
3. Django runs **system checks** (`python manage.py check`) — validates that models, settings, and URL config are internally consistent. If this fails (e.g. a broken `INSTALLED_APPS` entry or invalid setting), the server won't start.
4. Django builds the **URL resolver tree** from `ROOT_URLCONF` (`home/urls.py`) — this is where it discovers `path('student/', include("student.urls"))` etc., so every URL pattern is known *before* the first request arrives.
5. **`home/wsgi.py`** creates the `application` callable (`get_wsgi_application()`) — this is the object the dev server (or a production server like gunicorn) actually calls for every incoming HTTP request.
6. The **`StatReloader`** starts watching all `.py` files — if you edit and save a file, it restarts step 1–5 automatically so changes take effect without manually stopping/starting the server.
7. The server starts listening (default `http://127.0.0.1:8000/`). Each incoming request then follows the **Request lifecycle** described above, starting from "Middleware".

If any step 1–4 fails (bad import, syntax error, misconfigured setting), the server exits immediately with a traceback *before* it ever starts listening — so a broken `runserver` startup is always a config/import problem, not a per-request bug.
