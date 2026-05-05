import datetime

# 1. THE PARENT CLASS (Inheritance)
class LibraryItem:
    def __init__(self, title, identifier):
        self.title = title
        self.identifier = identifier
        self.is_checked_out = False
        self.due_date = None

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"[{self.identifier}] {self.title} - {status}"

# 2. CHILD CLASSES (Inheritance in action)
class Book(LibraryItem):
    def __init__(self, title, identifier, author, pages):
        super().__init__(title, identifier)
        self.author = author
        self.pages = pages

class Magazine(LibraryItem):
    def __init__(self, title, identifier, issue_number):
        super().__init__(title, identifier)
        self.issue_number = issue_number

# 3. THE MANAGER CLASS
class Library:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    # 4. LOOPS & LOGIC
    def find_item(self, search_title):
        for item in self.inventory:
            # Case-insensitive comparison
            if item.title.lower() == search_title.lower():
                return item
        return None

    def show_catalog(self):
        print(f"\n--- Welcome to {self.name} ---")
        if not self.inventory:
            print("The library is currently empty.")
        else:
            for item in self.inventory:
                print(item)

# 5. FUNCTIONS & MAIN EXECUTION
def main():
    # Setup our library
    my_library = Library("Madison Community Vault")

    # Add some data
    my_library.add_item(Book("The Great Gatsby", "B001", "F. Scott Fitzgerald", 180))
    my_library.add_item(Book("Clean Code", "B002", "Robert Martin", 464))
    my_library.add_item(Magazine("Wired", "M101", 2026))

    # Simple User Loop
    active = True
    while active:
        my_library.show_catalog()
        
        print("\nOptions: [1] Check Out  [2] Return  [3] Exit")
        choice = input("Select an option: ")

        if choice == "3":
            print("Goodbye!")
            active = False
            
        elif choice == "1":
            title = input("Enter title to check out: ")
            item = my_library.find_item(title)
            
            # IF/ELSE Conditions
            if item:
                if item.is_checked_out:
                    print(f"Sorry, {item.title} is already out.")
                else:
                    item.is_checked_out = True
                    print(f"Success! You checked out {item.title}.")
            else:
                print("Item not found in catalog.")
        
        elif choice == "2":
            title = input("Enter title to return: ")
            item = my_library.find_item(title)
            if item and item.is_checked_out:
                item.is_checked_out = False
                print(f"Thank you for returning {item.title}.")
            else:
                print("That item isn't checked out.")
        
        else:
            print("Invalid selection, try again.")

if __name__ == "__main__":
    main()