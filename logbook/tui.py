from datetime import datetime
from textual.app import App, on
from textual.widgets import (
    Footer,
    Header,
    Button,
    Input,
    Label,
    DataTable,
    Static,
)
from textual.containers import Grid, Horizontal, Vertical
from textual.screen import Screen


class LogBook(App):
    """A top-level class responsible for Creating the basis of the GUI."""

    CSS_PATH = "logbook.tcss"
    BINDINGS = [
        ("a", "add_entry", "Add entry to logbook"),
        ("d", "delete_entry", "Delete entry to logbook"),
        ("q", "request_quit", "Quit"),
    ]

    def __init__(self, database):
        super().__init__()
        self.database = database

    def compose(self):
        """Automatically called when app is running to create general outline of the GUI."""
        yield Header()
        entries_list = DataTable(classes="logbook-entries")
        entries_list.focus()
        entries_list.add_columns("ID", "Title", "Body", "Date")
        entries_list.cursor_type = "row"  # will highlight selected row
        entries_list.zebra_stripes = True
        add_button = Button("Add", variant="success", id="add_entry")
        add_button.focus()
        buttons_panel = Vertical(
            add_button,
            Button("Delete", variant="warning", id="delete_entry"),
            Static(classes="separator"),
            classes="buttons-panel",
        )
        yield Horizontal(entries_list, buttons_panel)
        yield Footer()

    def on_mount(self):
        """Set (sub)titles of main screen."""
        self.title = "Log Book"
        self.sub_title = "A log book for keeping track of completed work"
        self._load_enries()

    def _load_enries(self):
        """Add entries for display horizontally."""
        entries_list = self.query_one(DataTable)
        for entry_data in self.database.get_all_log_entries():
            _id, *log_entry = entry_data
            entries_list.add_row(*log_entry, key=_id)

    @on(Button.Pressed, "#add_entry")
    def action_add_entry(self):
        """Display dialog window for adding a log entry."""

        def check_entry(entry_data):
            if entry_data:
                self.database.add_log_entry(entry_data)
                _id, *log_entry = self.database.get_last_log_entry()
                self.query_one(DataTable).add_row(*log_entry, key=_id)

        self.push_screen(InputDialog(), check_entry)

    @on(Button.Pressed, "#delete_entry")
    def action_delete_entry(self):
        """Display dialog window for deleting a log entry."""
        entries_list = self.query_one(DataTable)
        row_key, _ = entries_list.coordinate_to_cell_key(entries_list.cursor_coordinate)

        def check_answer(accepted):
            if accepted and row_key:
                self.database.delete_log_entry(_id=row_key.value)
                entries_list.remove_row(row_key)

        self.push_screen(
            QuestionDialog("Do you want to delete entry?"),
            check_answer,
        )

    def action_request_quit(self):
        """Display dialog window for quitting the app."""

        def check_answer(accepted):
            if accepted:
                self.exit()

        self.push_screen(QuestionDialog("Do you want to quit?"), check_answer)


class QuestionDialog(Screen):
    """Allows creating dialog windows with a custom message and yes/no answer buttons."""

    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message

    def compose(self):
        """Add two yes/no answer buttons to the dialog window"""
        no_button = Button("No", variant="primary", id="no")
        no_button.focus()

        yield Grid(
            Label(self.message, id="question"),
            Button("Yes", variant="error", id="yes"),
            no_button,
            id="question_dialog",
        )

    def on_button_pressed(self, event):
        """Convert pushed button to a stored binary value."""
        if event.button.id == "yes":
            self.dismiss(True)
        else:
            self.dismiss(False)


class InputDialog(Screen):
    """Allows creating dialog window for creating log entries.
    The entry will be automatically timestamped later on.
    """

    def compose(self):
        """Create a dialog window for inputing a log entry title and body."""
        yield Grid(
            Label("Add Entry", id="title"),
            Label("Title:", classes="label"),
            Input(
                placeholder="Entry Title",
                classes="input",
                id="entry_title",
            ),
            Label("Body:", classes="label"),
            Input(
                placeholder="Entry body",
                classes="input",
                id="entry_body",
            ),
            Static(),
            Button("Cancel", variant="warning", id="cancel"),
            Button("OK", variant="success", id="ok"),
            id="input-dialog",
        )

    def on_button_pressed(self, event):
        """Monitore button pushes for adding the log entry (or discarding it).
        A timestamp is added to the user' input.
        """
        if event.button.id == "ok":
            title = self.query_one("#entry_title", Input).value
            body = self.query_one("#entry_body", Input).value
            date_raw = datetime.now()
            date = date_raw.strftime("%d/%m/%Y, %H:%M:%S")
            self.dismiss((title, body, date))
        else:
            self.dismiss(())
