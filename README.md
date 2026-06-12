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
