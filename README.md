# Bhakti Lounge — Playwright UI Tests

Portfolio-grade, non-destructive UI automation for the public [Bhakti Lounge](https://www.bhaktilounge.org.nz/) website, built with Python, Playwright and pytest.

> This is an independent educational project. It is not affiliated with Bhakti Lounge. Tests do not submit forms, create bookings or make purchases on the production website.
>
> The site owner has given permission to use the website materials in this portfolio project.

## What this project demonstrates

- readable Page Object Model;
- semantic, user-facing Playwright locators;
- smoke, regression, mobile and known-issue markers;
- cross-browser and parallel execution;
- traces, screenshots and videos retained on failure;
- pull-request and scheduled GitHub Actions workflows;
- responsible testing of a real production website.

## Current result

```text
30 passed, 1 xfailed
```

The portfolio suite is stable in Chromium locally. CI smoke checks pass in Chromium, Firefox and WebKit (the browser engine used by Safari). It includes 21 parameterized social-link journeys (seven main pages multiplied by three networks), validation of every visible Eventbrite booking link, and a real booking-navigation check. The expected failure documents a reproducible product defect rather than an automation failure. Educational examples are retained in the repository but excluded from CI through the `learning` marker.

## Project structure

```text
.
├── .github/workflows/     # PR smoke checks and nightly regression
├── docs/                  # test strategy, learning notes and LinkedIn draft
├── pages/                 # locators and page behaviour
├── tests/                 # user-focused test scenarios
├── pyproject.toml         # dependencies and tool configuration
└── README.md
```

The separation is intentional: tests describe *what* a user can do; page objects know *how* to interact with a page; fixtures assemble reusable dependencies.

## Quick start

Requirements: Python 3.11+ and Git.

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

Install the project and browser binaries:

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
playwright install chromium
```

Run the suite:

```bash
pytest -m "not learning"
```

Useful commands:

```bash
pytest -m smoke                         # fast critical checks
pytest -m regression                    # broader suite
pytest --browser firefox                # another browser
pytest -m "not learning" -n auto        # portfolio suite in parallel
pytest --headed --slowmo 300            # watch and learn
pytest --base-url https://staging.test  # pytest-playwright URL option
ruff check . && ruff format --check .   # static checks
```

To override the tested environment for these page objects, set `BASE_URL`:

```powershell
$env:BASE_URL = "https://www.bhaktilounge.org.nz"
pytest -m smoke
```

## Test design choices

Locators prefer accessible roles and names over brittle CSS/XPath. Playwright automatically waits for actionable elements, so the suite contains no fixed sleeps. Frequently changing event titles are intentionally not hard-coded.

The newsletter is checked without submission. A public production site is not the right place for tests that create bookings, send email or alter data; those belong on a staging environment.

The suite records a currently reproducible footer phone-number mismatch as a strict expected failure. Manual DOM inspection also revealed a broken newsletter label association and duplicated responsive markup. See the [bug reports](docs/bug-reports.md) and [test strategy](docs/test-plan.md).

## CI/CD options

The included GitHub Actions setup runs smoke checks on pushes and pull requests, and a broader regression suite on a weekday schedule. Public workflow results make the current project status easy to review alongside the code.

Alternative options:

- GitLab CI: strong choice when code, issues and runners already live in GitLab.
- Azure Pipelines: useful for Microsoft-centric teams and enterprise environments.
- Jenkins: maximum control and self-hosting, but requires maintenance and adds little value to a small portfolio project.
- Docker + any runner: improves environment parity later, but browser images are large; add it when the project needs reproducible local/CI containers.

This is continuous integration rather than deployment: a test repository has no application artifact to deploy. A future CD step could publish an Allure report or static test dashboard to GitHub Pages.

## Learning notes

Russian-language Playwright fundamentals are in [docs/playwright-basics-ru.md](docs/playwright-basics-ru.md). The test scope and risk model are in [docs/test-plan.md](docs/test-plan.md).

## Roadmap

- add accessibility scans with axe;
- run write scenarios against a dedicated staging environment;
- add API-level checks when a stable public API is available;
- publish a test report to GitHub Pages;
- add dependency updates and a security scan.

## License

MIT — see [LICENSE](LICENSE).
