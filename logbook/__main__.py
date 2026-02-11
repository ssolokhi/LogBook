from logbook.tui import LogBook
from logbook.database import Database


def main():
    """Main entry point for starting the LogBook app.
    Instatiates a LogBook with a database created in a separate subfolder.
    Moved to a separate function to follow the standard C++ modular approach.
    """
    app = LogBook(database=Database())
    app.run()


if __name__ == "__main__":
    main()
