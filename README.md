# LogBook

A logbook app for keeping logs of completed work in case Nikhef logbook is unavailable/when entry is for personal uses only.
The logbook uses [Textual](https://textual.textualize.io/) - a python framework for *rapid application development*.

## Dependencies

The app is python3-based, dependencies are listed in *uv.lock* and in *pyproject.toml*.

## Installation 

Installation via PyPI is not supported.

Installation is easiest with [uv](https://github.com/astral-sh/uv). Follow the README instructions to install it if not already.

Clone the GitHub repository to your computer. Navigate to the projet's top folder. To install required dependencies, run 

```bash
uv sync
```

This will automatically install all required dependencies and create a virtual environment. Activate it using

```bash
source .venv/bin/activate
```

Alternatively, use the *pyproject.toml* configuration file (requires a activated virtual environment):

```bash
pip3 install -r pyproject.toml
```

To install the logbook as a local package, run

```bash
pip3 install .
```

It is advised to create a virtual environment beforehand o avoid potential conflicts.

## Usage

To run the notebook, use the following command:

```bash
python3 -m logbook
```

This will start a *graphical user interface* (GUI)

## Project Structure

```txt
.
├── .gitignore
├── README.md
├── LICENSE
├── uv.lock
├── database
    ├── log_entries.db  <-  database with log entries (ignored by git)
├── logbook
    ├── __init__.py     <-  turns directory into an executable module
    ├── __main__.py     <-  start-up of logbook
    ├── database.py     <-  functions for manipulating the logbook database
    ├── tui.py          <-  builing block for the logbook GUI
    ├── logbook.tcss    <-  Textual CSS that makes the GUI fancy
```

## Versioning

The project follows pride versioning, i.e. (Releases that I am pround of).(OK releases).(Embarassing releases).
