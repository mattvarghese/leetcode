# shell.py
import sys
from sqlalchemy import text
from database import SessionLocal

def start_repl():
    print("--- Professional SQL REPL ---")
    print("Commands: \\l (DBs), \\dt (Tables), \\d [table] (Schema), \\q (Quit)")
    print("Type Ctrl+D or \\q to stop.\n")

    session = SessionLocal()

    # Mapping Postgres commands to SQLite metadata queries
    COMMAND_MAP = {
        "\\l": "PRAGMA database_list;",
        "\\dt": "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';",
        "\\q": "EXIT" # Special flag for the loop
    }

    while True:
        try:
            query = input("sql> ").strip()

            # Handle standard exit keywords or the new \q command
            if query.lower() in ('exit', 'quit', '') or query == "\\q":
                break

            # Handle other Backslash Commands
            if query.startswith("\\"):
                if query in COMMAND_MAP:
                    stmt = text(COMMAND_MAP[query])
                elif query.startswith("\\d "):
                    table_name = query.split(" ")[1].replace(";", "")
                    stmt = text(f"PRAGMA table_info({table_name});")
                else:
                    print(f"Command '{query}' not recognized.")
                    continue
            else:
                # Standard SQL (ensure it ends with a semicolon for safety if preferred)
                stmt = text(query)

            result = session.execute(stmt)

            if result.returns_rows:
                print(f"\n{ ' | '.join(result.keys()) }")
                print("-" * 40)
                for row in result:
                    print(" | ".join(str(v) for v in row))
                print("")
            else:
                session.commit()
                print(f"Success: {result.rowcount} row(s) affected.\n")

        except EOFError: # Handles Ctrl+D
            break
        except Exception as e:
            print(f"Error: {e}\n")
            session.rollback()

    session.close()
    print("\nShell closed.")

if __name__ == "__main__":
    start_repl()