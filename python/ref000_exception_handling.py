"""
Python Exception Reference & Demonstration Tool
================================================
This script serves as a living documentation tool for common Python exceptions.
It maps error situations to their corresponding built-in exceptions and provides
isolated, safe environments to trigger, raise, and catch them.

QUICK REFERENCE TABLE:
--------------------------------------------------------------------------------
| Error Situation                               | Best Python Exception        |
|-----------------------------------------------|------------------------------|
| Absolute catch-all / prototyping              | Exception                    |
| Wrong data value (e.g., age -5)               | ValueError                   |
| Wrong data type (e.g., string instead of int) | TypeError                    |
| Generic internal failure                      | RuntimeError                 |
| Missing dictionary key                        | KeyError                     |
| Out-of-bounds list index                      | IndexError                   |
| Missing file or directory                     | FileNotFoundError            |
| Division by zero                              | ZeroDivisionError            |
| Missing object property or method             | AttributeError               |
| App-specific business logic failure           | Custom Exception             |
--------------------------------------------------------------------------------
"""


# --- Custom Exception Definition ---
class BusinessRuleViolationError(Exception):
    """
    Custom exception used for application-specific business logic failures.
    Always inherit from the base 'Exception' class.
    """

    pass


# =====================================================================
# DEMONSTRATION FUNCTIONS
# =====================================================================


def demo_base_exception():
    print("\n--- Scenario: Base Exception (Generic Catch-All) ---")
    print("How it's raised: Explicitly (as a baseline fallback or placeholder).")

    try:
        # Explicitly throwing a completely generic error
        raise Exception("A completely non-specific generic error occurred.")
    except Exception as e:
        print(f"[CAUGHT] Successfully intercepted: {type(e).__name__} -> '{e}'")


def demo_value_error():
    print("\n--- Scenario: ValueError ---")
    print("How it's raised: BOTH. Programmatically by built-ins, or Explicitly by you.")

    # 1. Programmatic Trigger
    try:
        print("1. Trying programmatic trigger (int('banana'))...")
        _ = int("banana")
    except ValueError as e:
        print(f"   [CAUGHT] {type(e).__name__}: {e}")

    # 2. Explicit Trigger
    try:
        print("2. Trying explicit trigger (age validation)...")
        age = -12
        if age < 0:
            raise ValueError(f"Age cannot be negative! Got: {age}")
    except ValueError as e:
        print(f"   [CAUGHT] {type(e).__name__}: {e}")


def demo_type_error():
    print("\n--- Scenario: TypeError ---")
    print(
        "How it's raised: BOTH. Programmatically by bad operations, or Explicitly for type-guards."
    )

    # 1. Programmatic Trigger
    try:
        print("1. Trying programmatic trigger ('abc' + 5)...")
        _ = "abc" + 5
    except TypeError as e:
        print(f"   [CAUGHT] {type(e).__name__}: {e}")

    # 2. Explicit Trigger
    try:
        print("2. Trying explicit trigger (strict configuration block)...")
        api_key = 12345  # Oops, should be a string
        if not isinstance(api_key, str):
            raise TypeError(f"API Key must be a string, not {type(api_key).__name__}")
    except TypeError as e:
        print(f"   [CAUGHT] {type(e).__name__}: {e}")


def demo_runtime_error():
    print("\n--- Scenario: RuntimeError ---")
    print(
        "How it's raised: Explicitly (by design, to signal unclassified internal state failures)."
    )

    try:
        # This is almost always raised explicitly when no other specific error fits
        system_status = "STUCK_IN_LIMIT_STATE"
        if system_status == "STUCK_IN_LIMIT_STATE":
            raise RuntimeError(
                "The system hardware is locked and cannot cycle. Manual override required."
            )
    except RuntimeError as e:
        print(f"[CAUGHT] Successfully intercepted: {type(e).__name__} -> '{e}'")


def demo_key_error():
    print("\n--- Scenario: KeyError ---")
    print("How it's raised: Programmatically (when accessing missing dictionary keys).")

    try:
        user_profile = {"username": "jdoe123"}
        print("Trying to access missing dictionary key ['email']...")
        _ = user_profile["email"]
    except KeyError as e:
        # Note: KeyError prints just the missing key string when cast to string, e.g., 'email'
        print(
            f"[CAUGHT] Successfully intercepted: {type(e).__name__} -> Missing key: {e}"
        )


def demo_index_error():
    print("\n--- Scenario: IndexError ---")
    print(
        "How it's raised: Programmatically (when index is out of bounds of a sequence)."
    )

    try:
        items = ["apple", "banana"]
        print("Trying to grab index 5 from a 2-item list...")
        _ = items[5]
    except IndexError as e:
        print(f"[CAUGHT] Successfully intercepted: {type(e).__name__} -> '{e}'")


def demo_file_not_found():
    print("\n--- Scenario: FileNotFoundError ---")
    print(
        "How it's raised: Programmatically (by the OS file system via Python built-ins)."
    )

    try:
        print("Trying to open an imaginary text file...")
        with open("this_file_does_not_exist_anywhere_12345.txt", "r") as f:
            _ = f.read()
    except FileNotFoundError as e:
        print(f"[CAUGHT] Successfully intercepted: {type(e).__name__} -> '{e}'")


def demo_zero_division():
    print("\n--- Scenario: ZeroDivisionError ---")
    print("How it's raised: Programmatically (by Python's internal math evaluator).")

    try:
        print("Trying to divide 42 by 0...")
        _ = 42 / 0
    except ZeroDivisionError as e:
        print(f"[CAUGHT] Successfully intercepted: {type(e).__name__} -> '{e}'")


def demo_attribute_error():
    print("\n--- Scenario: AttributeError ---")
    print(
        "How it's raised: Programmatically (when an object lacks a called method or property)."
    )

    try:
        number = 99
        print("Trying to treat an Integer like a string by calling .lower()...")
        _ = number.lower()
    except AttributeError as e:
        print(f"[CAUGHT] Successfully intercepted: {type(e).__name__} -> '{e}'")


def demo_custom_exception():
    print("\n--- Scenario: Custom Exception (App Business Logic) ---")
    print(
        "How it's raised: Explicitly (manually triggered to enforce specific domain rules)."
    )

    try:
        coupon_code = "WINTER_DISCOUNT"
        # Business logic rule: all codes must end in a digit sequence
        if not coupon_code[-1].isdigit():
            raise BusinessRuleViolationError(
                f"Invalid Coupon: '{coupon_code}' must end with a discount number (e.g., WINTER10)."
            )
    except BusinessRuleViolationError as e:
        print(f"[CAUGHT] Successfully intercepted custom error: {type(e).__name__}")
        print(f"         Message: '{e}'")


# =====================================================================
# MAIN MENU LOOP
# =====================================================================


def main():
    # Map menu numbers to display labels and functions
    menu_options = {
        "1": ("Exception (Generic/Base)", demo_base_exception),
        "2": ("ValueError (Wrong Value)", demo_value_error),
        "3": ("TypeError (Wrong Data Type)", demo_type_error),
        "4": ("RuntimeError (System State)", demo_runtime_error),
        "5": ("KeyError (Missing Dict Key)", demo_key_error),
        "6": ("IndexError (Sequence Out-of-Bounds)", demo_index_error),
        "7": ("FileNotFoundError (I/O Failure)", demo_file_not_found),
        "8": ("ZeroDivisionError (Math Error)", demo_zero_division),
        "9": ("AttributeError (Invalid Property)", demo_attribute_error),
        "10": ("Custom Exception (Domain/Business Logic)", demo_custom_exception),
    }

    while True:
        print("\n" + "=" * 50)
        print("       PYTHON EXCEPTION DEMONSTRATION MENU")
        print("=" * 50)

        for key, (label, _) in menu_options.items():
            print(f" {key:2}. Demonstrate {label}")

        print(" Q. Quit Program")
        print("-" * 50)

        choice = input("Select an option to run: ").strip().upper()

        if choice == "Q":
            print("\nExiting exception reference program. Happy coding!")
            break
        elif choice in menu_options:
            # Dynamically grab and run the demo function
            _, demo_function = menu_options[choice]
            demo_function()

            input("\nPress [Enter] to return to the menu...")
        else:
            print("\n[!] Invalid choice. Please select a valid number or 'Q'.")


if __name__ == "__main__":
    main()
