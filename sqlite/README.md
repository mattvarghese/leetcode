# SQLite Practice Sandbox - User Inventory System

This project is a production-grade Python/SQL practice environment designed for CodeSandbox.io or local Ubuntu 25.10 systems. It demonstrates State Reconstruction using Window Functions, Atomic Transactions, and a custom SQL REPL.

## 1. System Requirements (Ubuntu 25.10)

Ensure your system is updated and has Python 3.13+ and the Venv module installed:

    sudo apt update
    sudo apt install python3-venv python3-pip sqlite3 -y

## 2. Environment Setup

Clone or copy the files into your project directory, then execute the following to set up the virtual environment and dependencies:

    # Create the virtual environment
    python3 -m venv venv

    # Activate the environment
    source venv/bin/activate

    # Install required packages
    pip install -r requirements.txt

## 3. Database Initialization

Before running the main application or the shell, you must initialize the SQLite database and seed it with initial data (Barbie and Ken):

    python3 seed.py
    python3 main.py

This will create 'practice.db' in your current directory and populate the 'users' and 'user_items' tables.

## 4. Usage

### A. Professional SQL REPL (shell.py)
Use this to interact directly with the database using standard SQL or Postgres-style shortcuts.

    python3 shell.py

Commands available in the REPL:
  \l          - List all connected databases (SQLite Pragma)
  \dt         - List all user tables
  \d [table]  - Describe table schema/columns
  \q          - Quit the shell

### B. State & Logic Demo (main.py)
Run the main script to see advanced SQLAlchemy usage in action:

    python3 main.py

The main script demonstrates:
1. State Reconstruction: Uses a SQL Window Function (ROW_NUMBER) to find the most recently added item for every user.
2. Complex Boolean Logic: Filters the ORM objects based on multi-condition logical exclusions (Active Users with items not done OR quantity > 10).

## 5. Project Structure

- database.py: Configures the SQLAlchemy engine and session.
- models.py: Defines the User and UserItem relational schema.
- seed.py: Utility to wipe and reset the database state.
- shell.py: An interactive SQL interface with metadata command mapping.
- main.py: High-level business logic and state reconstruction drills.

## 6. Troubleshooting

- Persistence: In CodeSandbox, ensure you are writing to the project root so 'practice.db' persists between container restarts.
- Errors: If you encounter a 'Transaction Error', the shell.py will automatically issue a rollback to keep the session stable.