from collections import defaultdict
from collections.abc import Generator


class IntegerMetadata:
    def __init__(self):
        self.isPrime: bool = True
        self.primeFactors: list[int] = []


class SieveOfEratosthenes:
    def __init__(self):
        self._index = 2
        self._intMetadata = defaultdict(IntegerMetadata)
        self._generator = self._infinite_sieve(2)
        next(self._generator)
        pass

    def _infinite_sieve(self, target: int) -> Generator[None, int, None]:
        self._intMetadata[0].isPrime = False
        self._intMetadata[1].isPrime = False
        while True:
            if self._intMetadata[self._index].isPrime:
                self._intMetadata[2 * self._index].isPrime = False
                self._intMetadata[2 * self._index].primeFactors.append(self._index)
            else:
                for step in self._intMetadata[self._index].primeFactors:
                    self._intMetadata[self._index + step].isPrime = False
                    self._intMetadata[self._index + step].primeFactors.append(step)
            if self._index == target:
                target = yield
            self._index += 1

    def isPrime(self, num: int) -> bool:
        if num > self._index:
            self._generator.send(num)
        return self._intMetadata[num].isPrime

    def getFactors(self, num: int) -> list[int]:
        if num > self._index:
            self._generator.send(num)
        return self._intMetadata[num].primeFactors


if __name__ == "__main__":
    sieve = SieveOfEratosthenes()
    for i in range(1000, 0, -1):
        isPrime = sieve.isPrime(i)
        print(f"Is {i} prime?: {isPrime}")
        if not isPrime:
            print(f"Prime factors of {i} are: {sieve.getFactors(i)}")
