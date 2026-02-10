# LogBook

Logbook for keeping logs of completed work in case Nikhef logbook is unavailable/when entry is for personal uses only.
The logbook uses [Textual](https://textual.textualize.io/) - a python framework for *rapid application development*.

## Installation 

To install required dependencies, run 

```bash
pip3 install -r requirements.txt
```

It is advised to create a virtual environment beforehand o avoid potential conflicts.

## Usage

To run the notebook, use the following command:

```bash
python3 -m logbook
```

## Project Structure

```txt
.
|-- .gitignore
|-- README.md
|-- LICENSE
|-- requirements.txt
|-- database
    |-- log_entries.db  <-  database with log entries (ignored by git)
|-- logbook
    |-- __init__.py     <-  turns directory into an executable module
    |-- __main__.py     <-  start-up of logbook
    |-- database.py     <-  functions for manipulating the logbook database
    |-- tui.py          <-  builing block for the logbook GUI
    |-- logbook.tcss    <-  Textual CSS that makes the GUI fancy
```

