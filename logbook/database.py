import pathlib
import sqlite3

DATABASE_PATH = pathlib.Path.home() / "LogBook/log_entries.db"


class Database:
    def __init__(self, database_path=DATABASE_PATH):
        self.database = sqlite3.connect(database_path)
        self.cursor = self.database.cursor()
        self._create_table()

    def _create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS logs(
                id INTEGER PRIMARY KEY,
                title TEXT,
                body TEXT,
                date TEXT
            );
        """
        self._execute_query(query)

    def _execute_query(self, query, *query_args):
        result = self.cursor.execute(query, [*query_args])
        self.database.commit()
        return result

    def get_all_log_entries(self):
        result = self._execute_query("SELECT * FROM logs;")
        return result.fetchall()

    def get_last_log_entry(self):
        result = self._execute_query("SELECT * FROM logs ORDER BY id DESC LIMIT 1;")
        return result.fetchone()

    def add_log_entry(self, log_entry):
        self._execute_query(
            "INSERT INTO logs VALUES (NULL,?,?,?);",
            *log_entry,
        )

    def delete_log_entry(self, id):
        self._execute_query(
            "DELETE FROM logs WHERE id=(?);",
            id,
        )
