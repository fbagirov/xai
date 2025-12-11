import os
import sqlite3
from datetime import datetime

from flask import (
    Flask,
    g,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

# Configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "data.db")

app = Flask(__name__)

# Database helpers

def get_db():
    """Return SQLite connection for the current request."""
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Create tables if they do not exist."""
    db = get_db()
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            created_at TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        );
        """
    )
    db.commit()


# Routes

@app.route("/", methods=["GET"])
def index():
    """List all tasks."""
    db = get_db()
    tasks = db.execute(
        "SELECT id, title, description, created_at, completed "
        "FROM tasks ORDER BY created_at DESC"
    ).fetchall()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    """Create a new task."""
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()

    if not title:
        flash("Title is required.", "error")
        return redirect(url_for("index"))

    db = get_db()
    db.execute(
        "INSERT INTO tasks (title, description, created_at, completed) "
        "VALUES (?, ?, ?, ?)",
        (title, description, datetime.utcnow().isoformat(timespec="seconds"), 0),
    )
    db.commit()

    flash("Task created.", "success")
    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    """Toggle completion flag on a task."""
    db = get_db()
    task = db.execute(
        "SELECT id, completed FROM tasks WHERE id = ?",
        (task_id,),
    ).fetchone()

    if task is None:
        flash("Task not found.", "error")
        return redirect(url_for("index"))

    new_val = 0 if task["completed"] else 1
    db.execute(
        "UPDATE tasks SET completed = ? WHERE id = ?",
        (new_val, task_id),
    )
    db.commit()

    flash("Task updated.", "success")
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    """Delete a task."""
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()

    flash("Task deleted.", "success")
    return redirect(url_for("index"))


# entry point
if __name__ == "__main__":
    # Ensure the database exists
    if not os.path.exists(DB_PATH):
        with app.app_context():
            init_db()
    else:
        # Still run migrations if needed in the future
        with app.app_context():
            init_db()

    app.run(debug=True)
