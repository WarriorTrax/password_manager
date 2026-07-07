# Password Manager 🔐

A simple command-line password manager built with Python.

This project generates random passwords and stores account information using a local SQLite database. It was created as a learning project to practice Python programming, databases, and CRUD operations.

## Features

- Generate secure random passwords
- Store passwords locally with SQLite
- Add saved passwords
- View saved passwords
- Edit saved passwords
- Delete saved passwords
- Simple command-line interface

## Built With

- Python 3
- SQLite
- sqlite3
- secrets
- string

## How It Works

The program creates a local SQLite database called:

passwords.db

The database stores:

- Website name
- Username
- Generated password

## Installation

1. Make sure Python is installed.

Check your Python version:

python --version

2. Clone this repository:

git clone https://github.com/WarriorTrax/password_manager.git

3. Open the project folder:

cd password_manager

4. Run the program:

python password_manager.py

## Usage

When the program starts, choose an option:

1. Add a password
2. View a password
3. Delete password
4. Edit password
5. Exit

## Adding a Password

The program asks for:

- Website
- Username
- Password length

It then generates a random password and stores it in the database.

## Viewing a Password

Enter a saved website name to retrieve:

- Username
- Password

## Editing a Password

Select a saved website and create a new password or update the username.

## Deleting a Password

Select a saved website to remove it from the database.

## Project Structure

password_manager/

├── password_manager.py
├── passwords.db (created when the program runs)
├── README.md
├── LICENSE
└── .gitignore

## Security Notice

This project is for educational purposes only.

It is not recommended to store real passwords with this application because it does not currently include encryption or a master password system.

A production password manager would require additional security features such as:

- Encryption
- Master password protection
- Secure password storage
- Security testing

## Future Improvements

Possible future features:

- Add encryption
- Add a master password
- Add a graphical user interface
- Add password strength checking
- Add password search
- Add clipboard support
- Improve database security

## License

This project uses the MIT License.

See the LICENSE file for more information.
