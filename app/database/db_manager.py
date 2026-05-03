import os
import sqlite3

from app.config import DATABASE_PATH


class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_PATH) -> None:
        self.db_path = db_path
        self._ensure_database()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _ensure_database(self) -> None:
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    category TEXT NOT NULL,
                    priority TEXT NOT NULL,
                    due_date TEXT NOT NULL,
                    status TEXT NOT NULL,
                    notes TEXT NOT NULL
                )
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS finances (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    record_date TEXT NOT NULL,
                    record_type TEXT NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL,
                    payment_method TEXT NOT NULL,
                    notes TEXT NOT NULL
                )
                """
            )
            connection.commit()

    def fetch_todos(self) -> list[dict]:
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM todos ORDER BY due_date ASC, id DESC")
            rows = cursor.fetchall()
            todo_list = []
            for row in rows:
                todo_list.append(
                    {
                        "id": row[0],
                        "title": row[1],
                        "category": row[2],
                        "priority": row[3],
                        "due_date": row[4],
                        "status": row[5],
                        "notes": row[6],
                    }
                )
            return todo_list

    def get_todo_by_id(self, item_id: int) -> dict | None:
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM todos WHERE id = ?", (item_id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return {
                "id": row[0],
                "title": row[1],
                "category": row[2],
                "priority": row[3],
                "due_date": row[4],
                "status": row[5],
                "notes": row[6],
            }

    def add_todo(self, data: dict) -> None:
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO todos (title, category, priority, due_date, status, notes)
                VALUES (:title, :category, :priority, :due_date, :status, :notes)
                """,
                data,
            )
            connection.commit()

    def update_todo(self, item_id: int, data: dict) -> None:
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                UPDATE todos
                SET title = :title,
                    category = :category,
                    priority = :priority,
                    due_date = :due_date,
                    status = :status,
                    notes = :notes
                WHERE id = :id
                """,
                {
                    "id": item_id,
                    "title": data["title"],
                    "category": data["category"],
                    "priority": data["priority"],
                    "due_date": data["due_date"],
                    "status": data["status"],
                    "notes": data["notes"],
                },
            )
            connection.commit()

    def delete_todo(self, item_id: int) -> None:
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM todos WHERE id = ?", (item_id,))
            connection.commit()

    def fetch_finances(self) -> list[dict]:
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM finances ORDER BY record_date DESC, id DESC")
            rows = cursor.fetchall()
            finance_list = []
            for row in rows:
                finance_list.append(
                    {
                        "id": row[0],
                        "record_date": row[1],
                        "record_type": row[2],
                        "category": row[3],
                        "amount": row[4],
                        "payment_method": row[5],
                        "notes": row[6],
                    }
                )
            return finance_list

    def get_finance_by_id(self, item_id: int) -> dict | None:
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM finances WHERE id = ?", (item_id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return {
                "id": row[0],
                "record_date": row[1],
                "record_type": row[2],
                "category": row[3],
                "amount": row[4],
                "payment_method": row[5],
                "notes": row[6],
            }

    def add_finance(self, data: dict) -> None:
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO finances (
                    record_date,
                    record_type,
                    category,
                    amount,
                    payment_method,
                    notes
                )
                VALUES (
                    :record_date,
                    :record_type,
                    :category,
                    :amount,
                    :payment_method,
                    :notes
                )
                """,
                data,
            )
            connection.commit()

    def update_finance(self, item_id: int, data: dict) -> None:
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                UPDATE finances
                SET record_date = :record_date,
                    record_type = :record_type,
                    category = :category,
                    amount = :amount,
                    payment_method = :payment_method,
                    notes = :notes
                WHERE id = :id
                """,
                {
                    "id": item_id,
                    "record_date": data["record_date"],
                    "record_type": data["record_type"],
                    "category": data["category"],
                    "amount": data["amount"],
                    "payment_method": data["payment_method"],
                    "notes": data["notes"],
                },
            )
            connection.commit()

    def delete_finance(self, item_id: int) -> None:
        with self._connect() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM finances WHERE id = ?", (item_id,))
            connection.commit()
