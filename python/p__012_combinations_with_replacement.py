from collections.abc import Generator, Iterable  # Behavioral interfaces
from typing import TypeVar  # Type-system meta-logic

# Using a TypeVar allows the method to be generic.
# If you pass a list of strings, it yields tuples of strings.
# If you pass ints, it yields tuples of ints.
T = TypeVar("T")


class Combinations:
    @staticmethod
    def WithReplacement(
        iterable: Iterable[T], r: int
    ) -> Generator[tuple[T, ...], None, None]:
        """
        Mimics itertools.combinations_with_replacement(iterable, r).

        Args:
            iterable: An iterable collection of items.
            r: The number of items to choose.

        Yields:
            Tuples representing combinations with replacement.
        """
        pool: tuple[T, ...] = tuple(iterable)
        n: int = len(pool)

        if not n and r:
            return

        # Initial state: all indices start at 0
        indices: list[int] = [0] * r
        yield tuple(pool[i] for i in indices)

        while True:
            # Step 3: Find the rightmost index that can be incremented
            for i in reversed(range(r)):
                if indices[i] != n - 1:
                    break
            else:
                return  # All indices are at max

            # Step 4: Increment pivot and update everything to the right
            indices[i:] = [indices[i] + 1] * (r - i)
            yield tuple(pool[i] for i in indices)
