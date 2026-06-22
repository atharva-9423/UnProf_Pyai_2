# UnProf_Pyai_2

# Contact Management System

A Python CLI tool built as part of Day 2 of a Python Intermediate internship — File Handling & JSON.

## Features

- Add new contacts (name, phone, email)
- Save contacts to a JSON file automatically
- Load contacts from JSON on every startup (data persists between sessions)
- Search contacts by name, phone, or email

## Concepts Used

- Opening files with `open()` in read (`"r"`) and write (`"w"`) modes
- Reading JSON files using `json.load()`
- Writing JSON files using `json.dump()`
- Checking file existence with `os.path.exists()`

## How to Run

```bash
python3 contact_manager.py
```

No extra libraries needed — uses Python's built-in `json` and `os` modules.

## Example Menu

```
1. Add Contact
2. Search Contact
3. View All Contacts
4. Exit
```

## Data Storage

Contacts are saved in a `contacts.json` file in the same directory. The file is created automatically on first run and updated every time a new contact is added.

## Author

**Atharva Phatangare**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/atharva-phatangare)
