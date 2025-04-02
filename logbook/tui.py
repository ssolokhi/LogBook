from textual.app import App
from textual.widgets import (
        Footer, Header, Button, Label, DataTable, Label, Static)
from textual.containers import Grid, Horizontal, Vertical
from textual.screen import Screen

class LogBook(App):
    CSS_PATH = 'logbook.tcss'
    BINDINGS = [
        ('a', 'add_entry', 'Add entry to logbook'),
        ('d', 'delete_entry', 'Delete entry to logbook'),
        ('q', 'request_quit', 'Quit'),
    ]
    
    def compose(self):
        'Automatically called when app is running'
        yield Header()
        entries_list = DataTable(classes='logbook-entries')
        entries_list.focus()
        entries_list.add_columns('ID', 'Title', 'Date')
        entries_list.cursor_type = 'row' # will highlight selected row
        entries_list.zebra_stripes = True
        add_button = Button('Add', variant='success', id='add_entry')
        add_button.focus()
        buttons_panel = Vertical(
                add_button,
                Button('Delete', variant='warning', id='delete_entry'),
                Static(classes='separator'),
                classes='buttons-panel',
        )
        yield Horizontal(entries_list, buttons_panel)
        yield Footer()

    def on_mount(self):
        'Set properties of main screen'
        self.title = 'Log Book'
        self.sub_title = 'A log book for keeping track of completed work'

    def action_add_entry(self):
        pass

    def action_request_quit(self):
        def check_answer(accepted):
            if accepted:
                self.exit()

        self.push_screen(QuestionDialog('Do you want to quit?'), check_answer)

class QuestionDialog(Screen):
    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message

    def compose(self):
        no_button = Button('No', variant='primary', id='no')
        no_button.focus()

        yield Grid(
                Label(self.message, id='question'),
                Button('Yes', variant='error', id='yes'),
                no_button,
                id='question_dialog')

    def on_button_pressed(self, event):
        if event.button.id == 'yes':
            self.dismiss(True)
        else:
            self.dismiss(False)
