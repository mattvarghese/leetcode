import pymongo
from tabulate import tabulate

def run_cli():
    # Context manager handles connection cleanup
    with pymongo.MongoClient("mongodb://admin:password@localhost:27017/") as client:
        db = client["practice_db"]
        users_col = db["users"]
        
        while True:
            print("\n=== MONGODB DOCUMENT CONTROL ===")
            print("1. Create User (Empty Inventory)")
            print("2. Add Item to User (Nested Push)")
            print("3. List All Users & Inventories")
            print("4. Find Users with specific Item (Querying Arrays)")
            print("5. Delete User")
            print("0. Exit")
            
            choice = input("\nSelect: ")

            try:
                if choice == '1':
                    name = input("Name: ")
                    users_col.insert_one({"username": name, "items": [], "active": True})
                    print(f"✔ User '{name}' created.")

                elif choice == '2':
                    name = input("User to update (Case Sensitive): ")
                    item_name = input("Item name: ")
                    qty = int(input("Quantity: "))

                    result = users_col.update_one(
                        {"username": name},
                        {"$push": {"items": {"name": item_name, "qty": qty, "done": False}}}
                    )

                    if result.matched_count > 0:
                        print(f"✔ Item added to {name}'s nested document.")
                    else:
                        print(f"✖ Error: No user found with username '{name}'.")

                elif choice == '3':
                    users = list(users_col.find())
                    if not users:
                        print("\nDatabase is currently empty.")
                    else:
                        table_data = []
                        for u in users:
                            username = u.get("username", "N/A")
                            items = u.get("items", [])
                            if not items:
                                table_data.append([username, "---", "---", "---"])
                            else:
                                for item in items:
                                    table_data.append([
                                        username, 
                                        item.get("name", "N/A"), 
                                        item.get("qty", 0), 
                                        "✔" if item.get("done") else " "
                                    ])
                        
                        headers = ["Username", "Item Name", "Qty", "Done"]
                        print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))

                elif choice == '5':
                    name = input("User to delete (Case Sensitive): ")
                    # Verification check
                    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ")
                    if confirm.lower() == 'y':
                        result = users_col.delete_one({"username": name})
                        
                        if result.deleted_count > 0:
                            print(f"✔ User '{name}' successfully deleted.")
                        else:
                            print(f"✖ Error: No user found with username '{name}'.")
                    else:
                        print("Operation cancelled.")

                elif choice == '0':
                    print("Exiting...")
                    break
                
                else:
                    print(f"Invalid selection: {choice}")

            except ValueError:
                print("✖ Input Error: Invalid numeric value provided.")
            except Exception as e:
                print(f"✖ System Error: {e}")

if __name__ == "__main__":
    run_cli()