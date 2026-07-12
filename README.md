# DjangoCC

trying cookiecutter django

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Settings

Moved to [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      uv run python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    uv run mypy core

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    uv run coverage run -m pytest
    uv run coverage html
    uv run open htmlcov/index.html

#### Running tests with pytest

    uv run pytest

### Tailwind CSS

This project uses Tailwind CSS, configured inside the [`theme/static_src`](file:///d:/Projects/DjangoCC/core/theme/static_src) directory.

#### Installation
Before compiling CSS for the first time, you must install the Node.js dependencies:

1. Navigate to the Tailwind theme directory:
   ```bash
   cd theme/static_src
   ```
2. Install the packages:
   ```bash
   npm install
   ```

#### Running Tailwind in Development (Watch Mode)
To compile and automatically rebuild your CSS when templates change:

* **Using `just`**:
  ```bash
  just tailwind
  ```
* **Manually**:
  Navigate to the theme directory and run the dev server:
  ```bash
  cd theme/static_src
  npm run dev
  ```

#### Building for Production (Minified)
To compile a production-ready, minified stylesheet:

Navigate to the theme directory and run the build script:
```bash
cd theme/static_src
npm run build
```

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd core
uv run celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd core
uv run celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd core
uv run celery -A config.celery_app worker -B -l info
```

## Docker Setup & Local Development

This project supports local development using Docker and Docker Compose. Environment configurations are already defined in the [`.envs/.local/`](file:///d:/Projects/DjangoCC/core/.envs/.local) directory.

### Quick Start with `just`

A [`justfile`](file:///d:/Projects/DjangoCC/core/justfile) is provided for convenience. If you have [just](https://github.com/casey/just) installed:

1. **Build the containers**:
   ```bash
   just build
   ```
2. **Start the containers** (runs in background):
   ```bash
   just up
   ```
3. **Create a superuser**:
   ```bash
   just manage createsuperuser
   ```
4. **Start Tailwind compiler / watcher**:
   ```bash
   just tailwind
   ```
5. **Run tests**:
   ```bash
   just pytest
   ```
6. **Stop containers**:
   ```bash
   just down
   ```
7. **Prune/Reset environment** (destroys containers and database volumes):
   ```bash
   just prune
   ```

### Alternative: Using Docker Compose directly

If you don't have `just` installed, you can run raw `docker compose` commands directly:

1. **Build the images**:
   ```bash
   docker compose -f docker-compose.local.yml build
   ```
2. **Start the application**:
   ```bash
   docker compose -f docker-compose.local.yml up
   ```
   To run in the background (detached mode):
   ```bash
   docker compose -f docker-compose.local.yml up -d
   ```
3. **Create a superuser**:
   ```bash
   docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser
   ```
4. **Start Tailwind compiler / watcher**:
   ```bash
   cd theme/static_src
   npm run dev
   ```
5. **Run tests**:
   ```bash
   docker compose -f docker-compose.local.yml run --rm django pytest
   ```
6. **Stop containers**:
   ```bash
   docker compose -f docker-compose.local.yml down
   ```

> [!TIP]
> **PowerShell/Bash Alias Helper**
>
> To simplify typing, you can define a shell helper alias like `dcl`.
>
> In **PowerShell**:
> ```powershell
> function dcl { docker compose -f docker-compose.local.yml $args }
> ```
> In **Bash / Zsh**:
> ```bash
> alias dcl="docker compose -f docker-compose.local.yml"
> ```
> Once defined, run commands with the shorter prefix `dcl`:
> ```bash
> dcl build
> dcl up -d
> dcl run --rm django python manage.py tailwind start
> ```

### Accessing Services

Once the containers are running:
* **Django Application**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* **Mailpit (Local SMTP Webmail)**: [http://127.0.0.1:8025](http://127.0.0.1:8025) (to view outgoing emails)
* **Flower (Celery Monitoring)**: [http://127.0.0.1:5555](http://127.0.0.1:5555)

---

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-with-docker.html).
