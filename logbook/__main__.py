from logbook.tui import LogBook
from logbook.database import Database


def main():
    app = LogBook(database=Database())
    app.run()


if __name__ == '__main__':
    main()
