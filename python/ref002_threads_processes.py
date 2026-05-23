import multiprocessing
import os
import threading
import time


def cpu_heavy_bound_task(task_id, operations=15_000_000):
    """
    A pure CPU-bound mathematical calculation (summing increments).
    This function requires raw CPU clock cycles and zero I/O operations.
    """
    print(
        f"[Worker {task_id}] Started execution. PID: {os.getpid()}, Thread Name: {threading.current_thread().name}"
    )
    start_time = time.time()

    accumulator = 0
    for i in range(operations):
        accumulator += i

    duration = time.time() - start_time
    print(f"[Worker {task_id}] Finished calculation in {duration:.4f} seconds.")
    return accumulator


# =====================================================================
# THREADS CONTEXT
# =====================================================================
def run_threads_demo():
    print("\n--- Launching 2 Concurrent Threads ---")
    print(f"Parent Process PID: {os.getpid()}")
    print("Architectural Note: Due to Python's GIL, these threads cannot utilize")
    print(
        "multiple CPU cores simultaneously. They will be serialized, taking ~2x longer."
    )

    start_total = time.time()

    # Initialize two distinct threads within the SAME memory context
    t1 = threading.Thread(
        target=cpu_heavy_bound_task, args=(1,), name="Thread-Worker-1"
    )
    t2 = threading.Thread(
        target=cpu_heavy_bound_task, args=(2,), name="Thread-Worker-2"
    )

    # Spawning executions
    t1.start()
    t2.start()

    # Barrier Sync: Parent thread blocks until both child threads complete execution
    t1.join()
    t2.join()

    total_duration = time.time() - start_total
    print(f"Total Threaded Execution Time: {total_duration:.4f} seconds.")


# =====================================================================
# PROCESSES CONTEXT
# =====================================================================
def run_processes_demo():
    print("\n--- Launching 2 Concurrent Processes ---")
    print(f"Parent Process PID: {os.getpid()}")
    print("Architectural Note: This creates entirely distinct OS processes.")
    print("Each process gets its own separate Python Interpreter instance and GIL.")
    print(
        "They will run simultaneously on separate CPU cores (True Hardware Parallelism)."
    )

    start_total = time.time()

    # Initialize two separate OS processes with completely isolated memory layouts
    p1 = multiprocessing.Process(target=cpu_heavy_bound_task, args=(1,))
    p2 = multiprocessing.Process(target=cpu_heavy_bound_task, args=(2,))

    # Spawning execution vectors at the OS Kernel level
    p1.start()
    p2.start()

    # Barrier Sync: Parent process blocks until both child processes complete execution
    p1.join()
    p2.join()

    total_duration = time.time() - start_total
    print(f"Total Process Parallel Execution Time: {total_duration:.4f} seconds.")


# =====================================================================
# UI LOOP MENU
# =====================================================================
def main():
    # Defensive guard required for Python multiprocessing initialization across platforms
    multiprocessing.freeze_support()

    while True:
        print("\n==============================================")
        print("       THREADS VS PROCESSES EXECUTION MENU")
        print("==============================================")
        print("1. Run 2 Worker Functions via Threads (GIL Constrained)")
        print("2. Run 2 Worker Functions via Processes (True Hardware Parallelism)")
        print("3. Quit")

        choice = input("\nSelect execution strategy (1-3): ").strip()
        if choice == "1":
            run_threads_demo()
        elif choice == "2":
            run_processes_demo()
        elif choice == "3":
            print("Terminating testing harness. Goodbye!")
            break
        else:
            print("Invalid input choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
