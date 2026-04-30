import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError
from tabulate import tabulate  # Use 'pip install tabulate'

# --- 1. SETUP ---
DATABASE_URL = "postgresql://user:password@localhost:5432/practice_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# --- 2. MODELS ---
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    team_id = Column(Integer)
    items = relationship("UserItem", back_populates="owner", cascade="all, delete-orphan")

class UserItem(Base):
    __tablename__ = "user_items"
    item_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, default=1)
    done = Column(Boolean, default=False)
    owner = relationship("User", back_populates="items")

# --- 3. THE MENU INTERFACE ---
def main_menu():
    print("\n" + "═"*40)
    print("      DATABASE CONTROL CENTER")
    print("═"*40)
    print("1. Add User")
    print("2. Change User (Username/Team)")
    print("3. Deactivate User (Atomic Cleanup)")
    print("4. Provision Welcome Kits (Stored Proc)")
    print("5. Add Item to User")
    print("6. Mark Item as Done / Delete Item")
    print("-" * 10 + " VIEWING OPTIONS " + "-" * 10)
    print("7. List Users (Optional Team Filter)")
    print("8. View Items for a Specific User")
    print("9. View All Items for a Specific Team")
    print("0. Exit")
    return input("\nSelect an option: ")

def run_cli():
    # Only creates tables if they don't exist
    Base.metadata.create_all(engine)
    session = SessionLocal()

    while True:
        choice = main_menu()
        try:
            if choice == '1':
                name = input("Username: ")
                tid = int(input("Team ID: "))
                session.add(User(username=name, password=name, team_id=tid))
                session.commit()
                print(f"✔ User {name} created.")

            elif choice == '2':
                uid = int(input("User ID to update: "))
                user = session.get(User, uid)
                if user:
                    user.username = input(f"New username [{user.username}]: ") or user.username
                    tid_in = input(f"New Team ID [{user.team_id}]: ")
                    user.team_id = int(tid_in) if tid_in else user.team_id
                    session.commit()
                    print("✔ User updated.")

            elif choice == '3':
                uid = int(input("User ID to deactivate: "))
                user = session.get(User, uid)
                if user:
                    user.active = False
                    session.query(UserItem).filter_by(user_id=uid).delete()
                    session.commit()
                    print(f"✔ User {user.username} deactivated.")

            elif choice == '4':
                tid = int(input("Provision kits for Team ID: "))
                session.execute(text("CALL provision_active_welcome_kits(:t_id)"), {"t_id": tid})
                session.commit()
                print(f"✔ Kits provisioned via Postgres for Team {tid}.")

            elif choice == '5':
                uid = int(input("User ID: "))
                iname = input("Item Name: ")
                iqty = int(input("Quantity: ") or 1)
                session.add(UserItem(user_id=uid, item_name=iname, quantity=iqty))
                session.commit()
                print("✔ Item added.")

            elif choice == '6':
                iid = int(input("Item ID: "))
                item = session.get(UserItem, iid)
                if item:
                    action = input("Mark (D)one or (R)emove? ").upper()
                    if action == 'D':
                        item.done = True
                    elif action == 'R':
                        session.delete(item)
                    session.commit()
                    print("✔ Action completed.")

            elif choice == '7':
                tid_in = input("Filter by Team ID? (Leave blank for all): ")
                query = session.query(User)
                if tid_in:
                    query = query.filter(User.team_id == int(tid_in))
                
                table_data = [[u.user_id, u.username, u.team_id, "Active" if u.active else "Inactive"] for u in query.all()]
                print("\n" + tabulate(table_data, headers=["ID", "Username", "Team", "Status"], tablefmt="grid"))

            elif choice == '8':
                uid = int(input("Enter User ID: "))
                user = session.get(User, uid)
                if user:
                    table_data = [[i.item_id, i.item_name, i.quantity, "✔" if i.done else " "] for i in user.items]
                    print(f"\nINVENTORY FOR: {user.username}")
                    print(tabulate(table_data, headers=["Item ID", "Name", "Qty", "Done"], tablefmt="fancy_grid"))

            elif choice == '9':
                tid = int(input("Enter Team ID: "))
                results = (session.query(User.username, UserItem)
                          .join(UserItem).filter(User.team_id == tid).all())
                
                table_data = [[r[0], r[1].item_id, r[1].item_name, r[1].quantity, "✔" if r[1].done else " "] for r in results]
                print(f"\nTEAM {tid} SHARED INVENTORY")
                print(tabulate(table_data, headers=["Owner", "ID", "Item", "Qty", "Done"], tablefmt="presto"))

            elif choice == '0':
                break

        except SQLAlchemyError as e:
            session.rollback()
            print(f"\n❌ Transaction Error: {e}")
        except ValueError:
            print("\n❌ Input Error: Please enter numbers where required.")

    session.close()

if __name__ == "__main__":
    run_cli()
