import threading
import time
from collections import deque

# =====================================================================
# 1. MUTEX (Mutual Exclusion) DEMONSTRATION
# =====================================================================
shared_balance = 100
balance_mutex = threading.Lock()


def deposit_worker(amount, iterations):
    """
    Demonstrates using a Mutex to protect a shared variable from a
    Race Condition. Without the lock, concurrent modifications to
    shared_balance would result in lost updates.
    """
    global shared_balance
    for _ in range(iterations):
        # acquire() blocks until the lock is available.
        balance_mutex.acquire()
        try:
            # Critical Section: Only ONE thread can execute this at a time.
            current = shared_balance
            time.sleep(0.0001)  # Artificially force a context switch
            shared_balance = current + amount
        finally:
            # Always release in a finally block to prevent permanent deadlocks
            balance_mutex.release()


def run_mutex_demo():
    global shared_balance
    shared_balance = 100
    print("\n--- Mutex Demo: Preventing Race Conditions ---")
    print(f"Starting Balance: ${shared_balance}")

    # Spawn two concurrent threads modifying the exact same memory
    t1 = threading.Thread(target=deposit_worker, args=(10, 500))
    t2 = threading.Thread(target=deposit_worker, args=(20, 500))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # Expected: 100 + (10 * 500) + (20 * 500) = 15100
    print(f"Final Balance (Should be exactly $15100): ${shared_balance}")


# =====================================================================
# 2. CONDITION VARIABLE DEMONSTRATION
# =====================================================================
queue = deque()
queue_condition = threading.Condition()  # Implicitly creates an underlying Mutex


def consumer_worker():
    """
    Demonstrates coordination using a Condition Variable.
    The consumer sleeps efficiently without spinning/busy-waiting.
    """
    print("[Consumer] Thread started. Waiting for data...")

    # The 'with' statement acquires the condition variable's underlying lock.
    with queue_condition:
        # MANDATORY ARCHITECTURE: Always check conditions in a WHILE loop,
        # never an IF statement, to guard against 'Spurious Wakeups'.
        while len(queue) == 0:
            print("[Consumer] Queue empty. Going to sleep (releasing lock)...")
            # wait() atomically releases the lock and blocks the thread.
            queue_condition.wait()
            # When wait() returns, this thread has automatically RE-ACQUIRED the lock.
            print("[Consumer] Woken up! Re-checking queue condition...")

        item = queue.popleft()
        print(f"[Consumer] Successfully consumed item: {item}")


def producer_worker():
    """Generates an item and signals the waiting consumer thread."""
    print("[Producer] Thread started. Preparing item...")
    time.sleep(2)  # Simulate work

    with queue_condition:
        queue.append("Google Interview Syllabus")
        print("[Producer] Added item to queue. Signaling consumer...")
        # notify() wakes up exactly ONE thread waiting on this condition.
        queue_condition.notify()


def run_cv_demo():
    print("\n--- Condition Variable Demo: Inter-Thread Coordination ---")
    queue.clear()

    # Start consumer first so it is guaranteed to go to sleep waiting for data
    c = threading.Thread(target=consumer_worker)
    p = threading.Thread(target=producer_worker)

    c.start()
    time.sleep(0.5)  # Ensure consumer settles into its wait state
    p.start()

    c.join()
    p.join()


# =====================================================================
# 3. SEMAPHORE DEMONSTRATION
# =====================================================================
# A semaphore initialized to 2 acts as a rate-limiter, allowing max 2 concurrent workers.
api_semaphore = threading.Semaphore(2)


def api_throttled_worker(worker_id):
    """
    Demonstrates resource throttling. Even if 5 threads execute,
    only 2 can enter the critical bounded zone simultaneously.
    """
    print(f"[Worker {worker_id}] Waiting to access rate-limited API...")

    # acquire() decrements the counter. If counter == 0, blocks until a release occurs.
    with api_semaphore:
        print(f" >>> [Worker {worker_id}] ACQUIRED slot. Executing API call...")
        time.sleep(1.5)  # Simulate a high-latency network fetch
        print(f" <<< [Worker {worker_id}] RELEASING slot.")
    # Exiting the 'with' block automatically calls semaphore.release(), incrementing the counter.


def run_semaphore_demo():
    print("\n--- Semaphore Demo: Resource Bounding/Throttling ---")
    print("Spawning 5 threads. Watch how they pass through only 2 at a time:")

    threads = [
        threading.Thread(target=api_throttled_worker, args=(i,)) for i in range(1, 6)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# =====================================================================
# 4. MONITOR DEMONSTRATION (Language-Level Structure)
# =====================================================================
class ThreadSafeQueueMonitor:
    """
    Implements a classic 'Monitor'. The class encapsulates data, the
    mutex (lock), and state coordination internally. The calling code
    never manually interacts with synchronization primitives.
    """

    def __init__(self):
        self._internal_lock = threading.Lock()
        self._has_data_cv = threading.Condition(self._internal_lock)
        self._storage = []

    def push(self, data):
        # Python's 'with' statement on a lock functions as a structural Monitor scope.
        # It guarantees mutual exclusion and safe lock release upon exit.
        with self._internal_lock:
            self._storage.append(data)
            # Signal any waiting readers inside the monitor scope
            self._has_data_cv.notify_all()

    def pop(self):
        with self._has_data_cv:
            while len(self._storage) == 0:
                self._has_data_cv.wait()
            return self._storage.pop(0)


def monitor_producer(monitor_obj):
    for i in range(3):
        time.sleep(0.8)
        print(f"[Monitor Producer] Pushing Data Point {i}")
        monitor_obj.push(f"Packet-{i}")


def monitor_consumer(monitor_obj):
    for _ in range(3):
        data = monitor_obj.pop()
        print(f"[Monitor Consumer] Popped and processed: {data}")


def run_monitor_demo():
    print("\n--- Monitor Demo: Encapsulated Thread Safety ---")
    monitor_instance = ThreadSafeQueueMonitor()

    t_prod = threading.Thread(target=monitor_producer, args=(monitor_instance,))
    t_cons = threading.Thread(target=monitor_consumer, args=(monitor_instance,))

    t_cons.start()
    t_prod.start()
    t_prod.join()
    t_cons.join()


# =====================================================================
# UI LOOP MENU
# =====================================================================
def main():
    while True:
        print("\n==============================================")
        print("    PRIMITIVE SYNCHRONIZATION CONSTRUCTS MENU")
        print("==============================================")
        print("1. Demonstrate Mutex (Mutual Exclusion Lock)")
        print("2. Demonstrate Condition Variable (Signaling)")
        print("3. Demonstrate Semaphore (Resource Throttling)")
        print("4. Demonstrate Monitor (Structured Object Lock)")
        print("5. Quit")

        choice = input("\nSelect an option (1-5): ").strip()
        if choice == "1":
            run_mutex_demo()
        elif choice == "2":
            run_cv_demo()
        elif choice == "3":
            run_semaphore_demo()
        elif choice == "4":
            run_monitor_demo()
        elif choice == "5":
            print("Exiting execution framework. Goodbye!")
            break
        else:
            print("Invalid choice. Please input a number from 1 to 5.")


if __name__ == "__main__":
    main()
