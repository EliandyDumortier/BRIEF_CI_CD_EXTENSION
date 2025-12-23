# CI/CD Training — Semantic Release & GitHub Actions

This project was built as part of a CI/CD training program to implement a complete professional DevOps pipeline for a FastAPI application.

---

## 🚀 Project Features

- Python 3.13 FastAPI API with SQLModel + PostgreSQL
- Dependency management with **uv**
- Code quality with **Ruff**, **Mypy**
- Testing with **pytest + coverage**
- Security checks with:
  - **Bandit**
  - **Safety**
  - **detect-secrets**

---

## ⚙️ CI Pipeline (GitHub Actions)

Our CI workflow runs automatically on every **push** and **pull request** to `develop` and `main`.

### ✅ CI Jobs

| Job         | Purpose |
|--------------|----------|
| **lint**     | Ruff lint & formatting checks |
| **typecheck** | Mypy static typing checks |
| **security** | Bandit + Safety scanning |
| **tests**    | Pytest with PostgreSQL service & coverage |
| **pre-commit** | Executes all pre-commit hooks to prevent local bypass |

---

## 🧪 Pre-commit Hooks

The following hooks prevent bad code from ever reaching GitHub:

- Trailing whitespace removal
- End-of-file fixes
- YAML validation
- Merge conflict detection
- Ruff linting
- Ruff formatting
- Mypy validation
- detect-secrets scanning

Hooks are automatically installed via:

```bash
pre-commit install

🔐 Secret Detection

    All secrets are scanned using detect-secrets

    Baseline stored in .secrets.baseline

    .env files are ignored via .gitignore

    Docker & workflows contain no hard-coded credentials

📦 Semantic Release

Semantic versioning is fully automated using python-semantic-release.
🎯 Workflow

    Developers follow Conventional Commits:

        feat: → minor version bump

        fix: → patch bump

        BREAKING CHANGE: → major bump

    On merge to main:

        Version is computed automatically

        Git tag is created (example: v1.2.0)

        GitHub Release is published

⚙️ Configuration Summary

Located in pyproject.toml:

[tool.semantic_release]
version_source = "commit"
major_on_zero = false
tag_format = "v{version}"

[tool.semantic_release.branches]
main = true
develop = false

🐳 Docker & Registry

Docker images are built and pushed automatically to:

ghcr.io/<github-username>/fastapi-ci-cd

Triggered on:

    Push to develop

    Manual workflow dispatch

Accepted tags:

    latest

    Commit SHA

✅ Branch Protections

All important branches are protected:

    No direct pushes allowed

    PR required to merge

    Reviews required

    CI checks must pass

    Force pushes blocked

📊 Test Coverage

Coverage is measured with pytest-cov:

    Term output

    XML output for CI tracking

Example command:

uv run pytest --cov=app --cov-report=term --cov-report=xml

🛠️ Development Workflow

uv sync
pre-commit run --all-files
git commit
git push

✅ Final Result

At the end of this project we achieved:

✔️ Automated quality checks
✔️ Pre-commit enforcement locally and in CI
✔️ Secure secret detection
✔️ Python typing safety
✔️ CI/CD best practices
✔️ Automated versioning via Semantic Release
✔️ Docker image builds + registry publishing
