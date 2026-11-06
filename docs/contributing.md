
# Contributing

This repository is an independent QA automation portfolio built with Python, Pytest, and Playwright.

## Development workflow

1. Create a feature branch from `main`.
2. Make focused changes relevant to the intended task.
3. Run the affected tests locally.
4. Commit changes with a descriptive message.
5. Push the branch and open a pull request targeting `main`.
6. Review the changes, test results, and GitHub Actions artifacts before merging.

## Local setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies and Playwright browsers:

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Running tests

Run the current CI test suite:

```bash
python -m pytest test_final_project/ -v
```

Pytest generates `report.html` in the repository root. Failure screenshots are saved under the relevant test project's `screenshots/` directory.

## Pull requests

Use the repository's pull request template to summarize changes and document verification.

For this independently maintained portfolio, reviewing my own pull requests is a self-review process, not an independent or collaborative code review.
