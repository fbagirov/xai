# Antigravity Demo 

This is a small Flask + SQLite app that is using an AI "vibe coding" agent
(e.g., Google Antigravity / Gemini).

The frontend is implemented with Python (Flask + Jinja templates) and CSS.

Please be aware that Google Antigravity is known to format hard drives when in Turbo Mode (https://www.reddit.com/r/google_antigravity/comments/1p82or6/google_antigravity_just_deleted_the_contents_of/). 


## Features

- Create simple tasks (e.g., "Restart dev server", "Clear cache")
- Mark tasks as done / not done
- Delete tasks
- Data stored in a local SQLite database (`data.db`)

## Running the app

### Install GNU Make
```bash
[choco|scoop] install make

#### Restart PowerShell and then run: 
```bash
make docker-build

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
