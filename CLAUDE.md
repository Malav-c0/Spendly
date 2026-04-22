# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Spendly is a personal expense tracking web application built with Flask. It allows users to register, log in, record expenses by category, and visualize spending patterns.

## Commands

```bash
# Run the application
python app.py

# Install dependencies
pip install -r requirements.txt

# Run tests (pytest configured)
pytest
```

## Architecture

- **app.py** — Flask application entry point; defines all routes
- **database/db.py** — Database layer (SQLite); students implement `get_db()`, `init_db()`, `seed_db()`
- **templates/** — Jinja2 HTML templates (`base.html` extends for all pages)
- **static/** — CSS (`style.css`) and JavaScript (`main.js`)

## Tech Stack

- Flask 3.x with Werkzeug
- SQLite database
- Vanilla JavaScript (no framework)
- pytest for testing

## Current Implementation Status

Routes implemented: `/` (landing), `/register`, `/login`, `/terms`, `/privacy`

Placeholder routes (to be implemented): `/logout`, `/profile`, `/expenses/add`, `/expenses/:id/edit`, `/expenses/:id/delete`

The `database/db.py` file is a stub awaiting student implementation.
