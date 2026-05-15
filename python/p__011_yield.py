# Demonstrates using iterables


from collections.abc import Generator


def test_yield() -> Generator[int, None, None]:
    """
    Type parameters for Generator are:
    1. YieldType: The type of values yielded (int)
    2. SendType: The type of values sent via .send() (None)
    3. ReturnType: The type of the value returned at the end (None)
    """
    for i in range(100):
        print(f"Generated: {i}")
        yield i
        if i == 64:
            return  # This stops the generator
    return


def main_yield() -> None:
    # Python's type checkers understand that a Generator[int, ...]
    # can be iterated over to get ints.
    for i in test_yield():
        print(f"Received: {i}")


# Generator[YieldType, SendType, ReturnType]
def average_calculator() -> Generator[
    float, float, int
]:  # Generator[YieldType, SendType, ReturnType]
    total = 0.0
    count = 0
    avg = 0.0

    while True:
        # The variable that is "resumed" from yield is of type SendType
        # The value given to yield is of type YieldType
        # 1. YIELD the current average
        # 2. RECEIVE the new value via .send()
        new_value = yield avg  # This causes a pause and resume,
        #                        and in the process the upstream can send a value

        # Check if the consumer wants to stop (by sending None or a sentinel)
        if new_value is None:
            break

        total += new_value
        count += 1
        avg = total / count

    # 3. RETURN the final count when the loop breaks
    return count  # This value must be of ReturnType


def main_average():
    # Initialize the generator
    gen = average_calculator()

    # Prime the generator to reach the first yield
    next(gen)

    # Send values and get yields
    print(f"Current Avg: {gen.send(10)}")  # Yields 10.0
    print(f"Current Avg: {gen.send(20)}")  # Yields 15.0
    print(f"Current Avg: {gen.send(30)}")  # Yields 20.0

    # To get the ReturnType, we must catch the StopIteration exception
    try:
        gen.send(None)  # Breaks the loop
    except StopIteration as e:
        final_count = e.value
        print(f"--- Processed {final_count} numbers total ---")


if __name__ == "__main__":
    main_yield()
    main_average()
