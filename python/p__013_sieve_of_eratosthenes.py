from collections import defaultdict
from collections.abc import Generator, Iterator


class Eratosthenes:
    def __init__(self) -> None:
        # One persistent generator instance to maintain state
        self._generator: Generator[int, None, None] = self._create_infinite_sieve()
        # Cache for already discovered primes
        self.primes: list[int] = []

    def _get_next_prime(self) -> int:
        """Fetches the next prime from the generator and caches it."""
        p = next(self._generator)
        self.primes.append(p)
        return p

    def isPrime(self, num: int) -> bool:
        if num < 2:
            return False
        # Expand cache until we reach or pass the number
        while not self.primes or self.primes[-1] < num:
            self._get_next_prime()

        # Use binary search (or 'in' for small lists) to check presence
        # For large caches, 'num in set(self.primes)' or bisect is better
        return num in self.primes

    def nthPrime(self, n: int) -> int:
        if n < 1:
            return 0
        while len(self.primes) < n:
            self._get_next_prime()
        return self.primes[n - 1]

    def __iter__(self) -> Iterator[int]:
        """Yields from cache first, then generates new primes."""
        # First, yield what we already know
        yield from self.primes

        # Then, keep generating new ones forever
        while True:
            yield self._get_next_prime()

    def _create_infinite_sieve(self) -> Generator[int, None, None]:
        yield 2
        composites: dict[int, list[int]] = defaultdict(list)
        q = 3
        while True:
            if q not in composites:
                print(f"Generated: {q}")
                yield q
                composites[q * q].append(2 * q)
            else:
                for step in composites[q]:
                    composites[q + step].append(step)
                del composites[q]
            q += 2


def main(et: Eratosthenes, max: int):
    count = 0
    for i in et:
        count += 1
        print(f"primes[{count}] = {i}")
        if i > max:
            return


et = Eratosthenes()
main(et, 10)
print("==============")
main(et, 100)
