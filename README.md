# DemoQA Selenium Automation

UI test automation for [demoqa.com](https://demoqa.com) using Selenium, PyTest, and the Page Object Model.

## Project structure

| Directory | Purpose |
|-----------|---------|
| `pages/` | Page objects (actions per page) |
| `locators/` | CSS/XPath locators |
| `tests/` | PyTest test suites |
| `generator/` | Faker data and temp file generators |
| `data/` | Data models (e.g. `Person`, checkbox tree) |
| `URLs/` | Page URLs |
| `conftest.py` | Shared fixtures (Chrome `driver`) |

## Setup

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Requires Chrome browser (WebDriver is managed by Selenium 4.x).

## Run tests

```bash
python3 -m pytest -v
```

By module:

```bash
python3 -m pytest tests/elements_test.py -v
python3 -m pytest tests/forms_test.py -v
python3 -m pytest tests/alerts_frame_windows_test.py -v
```

## Branches

- `main` — stable, merged fixes
- `onboarding` — working branch for course / practice

## Backlog

Planned improvements: [`BACKLOG.md`](BACKLOG.md)

## CI

GitHub Actions runs `pytest` on push and pull requests (headless Chrome on Ubuntu).

## Known issues (expected xfail)

These reflect demoqa.com limitations, not test bugs:

- **Radio Button** — `No` option is disabled (`DemoQA: 'No' radio button is disabled`)
- **Links** — seven API-style links have missing or invalid href (`DemoQA: link href not provided or invalid`)
