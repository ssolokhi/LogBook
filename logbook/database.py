from pathlib import Path
import sqlite3

DATABASE_PATH = "/".join((Path.home(), "LogBook", "database", "log_entries.db"))


class Database:
    """Allows managing a database log entries using SQL queries.
    Provides access to all entries / last entry and enables adding/deleting new ones.
    """

    def __init__(self, database_path=DATABASE_PATH):
        self.database = sqlite3.connect(database_path)
        self.cursor = self.database.cursor()
        self._create_table()  # ensures database creation upon app start-up

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

    def _execute_query(self, query: str, *query_args: str):
        """Executes database query with an arbitrary number of query arguments.
        The arguments allow querying by id, adding strings with log texts, etc."""
        result = self.cursor.execute(query, [*query_args])
        self.database.commit()
        return result

    def get_all_log_entries(self):
        """Selects all log entries in the database for display in the GUI"""
        result = self._execute_query("SELECT * FROM logs;")
        return result.fetchall()

    def get_last_log_entry(self):
        """Returns last entry in the database for displaying latest work in the GUI.
        Entry will be fetched as first entry in a 'new database' where
        log entries appear in reverse order (descending ID).
        """
        result = self._execute_query("SELECT * FROM logs ORDER BY id DESC LIMIT 1;")
        return result.fetchone()

    def add_log_entry(self, log_entry: str):
        """Add log entry (an iterable consisting of title, body, text strings) to the database."""
        self._execute_query(
            "INSERT INTO logs VALUES (NULL,?,?,?);",
            *log_entry,
        )

    def delete_log_entry(self, _id: int):
        """Delete log entry based on its ID."""
        self._execute_query(
            "DELETE FROM logs WHERE id=(?);",
            _id,
        )
