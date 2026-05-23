from contextlib import contextmanager


# =====================================================================
# MODEL 1: THE CLASS-BASED CONTEXT MANAGER (The Dunder Method Protocol)
# =====================================================================
class NetworkSocketManager:
    """
    Simulates a low-level network socket manager.
    Implements raw __enter__ and __exit__ methods to handle lifecycle safety.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.is_connected = False

    def __enter__(self):
        """Executes when entering the 'with' block context."""
        print(
            f"\n[Socket __enter__] Initializing handshake to {self.host}:{self.port}..."
        )
        self.is_connected = True
        print("[Socket __enter__] Connection established successfully.")
        return self  # This value is bound to the target variable after the 'as' keyword

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Executes when exiting the 'with' block.
        Guarantees cleanup regardless of internal execution errors.
        """
        print("[Socket __exit__] Closing network buffer and flushing packets...")
        self.is_connected = False
        print("[Socket __exit__] Socket safely disconnected.")

        # Exception handling logic
        if exc_type is not None:
            print("[Socket __exit__] Caught an active exception inside the block!")
            print(f"  -> Type: {exc_type.__name__}")
            print(f"  -> Message: {exc_value}")

            # Architecture Rule: Returning True suppresses/swallows the exception.
            # Returning False (or None) allows the exception to bubble up and crash.
            if exc_type is ConnectionResetError:
                print(
                    "[Socket __exit__] Handled known network reset. Suppressing error to keep app alive."
                )
                return True

            print("[Socket __exit__] Unknown exception type. Letting it bubble up...")
            return False

        return True  # Clean exit without exceptions

    def send_data(self, payload):
        if not self.is_connected:
            raise RuntimeError("Cannot send payload; socket is closed.")
        print(f"[Socket Data] Transmitting payload: '{payload}'")


def run_class_based_demo(simulate_error_type):
    print(
        f"\n--- Model 1 Demo: Class-Based Protocol (Error Mode: {simulate_error_type}) ---"
    )

    try:
        # Initializing the context manager instance
        with NetworkSocketManager("127.0.0.1", 8080) as socket:
            socket.send_data("GET /index.html HTTP/1.1")

            if simulate_error_type == "suppressed":
                # Simulating an exception that __exit__ is designed to handle and swallow
                print("[Block Body] Simulating a sudden remote peer disconnection...")
                raise ConnectionResetError("Connection dropped by remote server peer.")

            elif simulate_error_type == "bubbled":
                # Simulating a random operational error that should escape the context manager
                print(
                    "[Block Body] Simulating an unexpected logical memory corruption..."
                )
                raise IndexError("Array boundary overrun.")

            print("[Block Body] Block completed smoothly with zero execution issues.")

    except Exception as e:
        print(
            f"[Outer Catch] Caught bubbled exception in main runtime loop: {type(e).__name__} -> {e}"
        )


# =====================================================================
# MODEL 2: THE GENERATOR-BASED CONTEXT MANAGER (The Functional Protocol)
# =====================================================================
@contextmanager
def managed_file_stream(filename, mode="r"):
    """
    Simulates a file stream manager using a generator function.
    The @contextmanager decorator handles the underlying class wrapper transformation.
    """
    # --- Everything before the yield acts as '__enter__' ---
    print(
        f"\n[Generator Stream] Allocating file system handles for '{filename}' in '{mode}' mode."
    )
    file_handle = f"STREAM_REF_FOR_{filename}"  # Mocking a stream resource

    try:
        # yield suspends execution and returns control to the interior of the 'with' block
        yield file_handle
    except Exception as e:
        # If an error happens inside the 'with' block, it is injected directly right here
        print(
            f"[Generator Stream] Intercepted internal block exception inside generator: {type(e).__name__}"
        )
        print("[Generator Stream] Performing critical emergency resource flushes...")
        raise e  # Pass it along to let the parent caller handle the crash
    finally:
        # --- The finally block acts as '__exit__' ---
        # This block is structurally guaranteed by the Python runtime to execute
        print(
            f"[Generator Stream] Closing hardware file handles for '{filename}'. Done."
        )


def run_generator_based_demo(trigger_error):
    print(
        f"\n--- Model 2 Demo: Generator-Based Protocol (Trigger Error: {trigger_error}) ---"
    )

    try:
        with managed_file_stream("user_profile.json", "w") as file_ref:
            print(f"[Block Body] Writing metrics to file handle reference: {file_ref}")

            if trigger_error:
                print("[Block Body] Crashing mid-write execution...")
                raise ValueError("Disk volume ran out of space allocation.")

            print("[Block Body] Stream modifications successfully serialized.")

    except Exception as e:
        print(
            f"[Outer Catch] Caught bubbled exception in main runtime loop: {type(e).__name__} -> {e}"
        )


# =====================================================================
# UI MENU LOOP
# =====================================================================
def main():
    while True:
        print("\n==============================================")
        print("          CONTEXT MANAGERS PROTOCOL MENU")
        print("==============================================")
        print("1. Class Model: Clean Run (No Errors)")
        print("2. Class Model: Suppressed Error (Swallowed by __exit__)")
        print("3. Class Model: Bubbled Error (Passed up through __exit__)")
        print("4. Generator Model: Clean Run (No Errors)")
        print("5. Generator Model: Bubbled Error (Handled by finally)")
        print("6. Quit")

        choice = input("\nSelect custom context behavior (1-6): ").strip()

        if choice == "1":
            run_class_based_demo(simulate_error_type="none")
        elif choice == "2":
            run_class_based_demo(simulate_error_type="suppressed")
        elif choice == "3":
            run_class_based_demo(simulate_error_type="bubbled")
        elif choice == "4":
            run_generator_based_demo(trigger_error=False)
        elif choice == "5":
            run_generator_based_demo(trigger_error=True)
        elif choice == "6":
            print("Terminating execution harness. Goodbye!")
            break
        else:
            print("Invalid verification target. Select a number between 1 and 6.")


if __name__ == "__main__":
    main()
