from __future__ import annotations


import sqlite3


def make_db() -> sqlite3.Connection:
    conn = sqlite3.connect("./session_one/db.sqlite")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS Student (stu_id INTEGER PRIMARY KEY, stu_name TEXT, stu_age INTEGER)"
    )

    conn.execute(
        "CREATE TABLE IF NOT EXISTS Course (cou_id INTEGER PRIMARY KEY, cou_name TEXT)"
    )

    conn.execute(
        """CREATE TABLE IF NOT EXISTS study (stu_id INTEGER, cou_id INTEGER, PRIMARY KEY (stu_id, cou_id))"""
    )

    # Insert 300 rows
    for i in range(300):
        conn.execute("INSERT INTO my_table (name) VALUES (?)", (f"Name {i}",))

    conn.commit()

    return conn


def main() -> int:

    conn = make_db()

    conn.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
