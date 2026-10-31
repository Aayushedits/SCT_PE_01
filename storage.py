
import json
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path(__file__).resolve().parent / "interview_history.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH, timeout=10)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS interviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                completed_at TEXT NOT NULL,
                candidate TEXT NOT NULL,
                role TEXT NOT NULL,
                average_score REAL,
                evaluated_count INTEGER NOT NULL DEFAULT 0,
                total_questions INTEGER NOT NULL DEFAULT 0,
                report_json TEXT NOT NULL
            )
        """)


def save_interview(report):
    candidate = str(report.get("candidate", "")).strip()
    role = str(
        report.get("target_role", report.get("role", ""))
    ).strip()

    if not candidate or not role:
        raise ValueError("Candidate name and target role are required.")

    results = report.get("results", [])
    if not isinstance(results, list):
        raise ValueError("Interview results must be a list.")

    scores = []
    for item in results:
        if not isinstance(item, dict):
            continue

        score = item.get("score")
        if isinstance(score, (int, float)) and not isinstance(score, bool):
            if 0 <= score <= 10:
                scores.append(float(score))

    average_score = (
        round(sum(scores) / len(scores), 2) if scores else None
    )

    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO interviews (
                completed_at, candidate, role, average_score,
                evaluated_count, total_questions, report_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.now(timezone.utc).isoformat(),
                candidate,
                role,
                average_score,
                len(scores),
                len(results),
                json.dumps(report, ensure_ascii=False),
            ),
        )
        return cursor.lastrowid


def get_interview_history(limit=100):
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT id, completed_at, candidate, role,
                   average_score, evaluated_count, total_questions
            FROM interviews
            ORDER BY id DESC
            LIMIT ?
            """,
            (max(1, min(int(limit), 500)),),
        ).fetchall()

    return [dict(row) for row in rows]


def get_interview(interview_id):
    with get_connection() as connection:
        row = connection.execute(
            "SELECT report_json FROM interviews WHERE id = ?",
            (int(interview_id),),
        ).fetchone()

    return json.loads(row["report_json"]) if row else None


def delete_interview(interview_id):
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM interviews WHERE id = ?",
            (int(interview_id),),
        )
        return cursor.rowcount > 0


initialize_database()
