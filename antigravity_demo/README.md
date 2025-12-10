# Antigravity Demo – Python Task Board

This is a small Flask + SQLite app that is using an AI "vibe coding" agent
(e.g., Google Antigravity / Gemini).

The frontend is implemented with Python (Flask + Jinja templates) and CSS.

## Features

- Create simple tasks (e.g., "Restart dev server", "Clear cache")
- Mark tasks as done / not done
- Delete tasks
- Data stored in a local SQLite database (`data.db`)

## Running the app

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
