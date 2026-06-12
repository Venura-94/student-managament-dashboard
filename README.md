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
