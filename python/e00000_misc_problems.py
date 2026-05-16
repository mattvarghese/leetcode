import math
from collections import defaultdict
from collections.abc import Generator


# https://projecteuler.net/problem=36
def euler36() -> int:
    total_sum = 0
    # 2^10 = 1024. This covers up to 20-bit palindromes.
    for i in range(1, 1024):
        b = bin(i)[2:]

        # Pattern 1: Even length (e.g., 10 -> 1001)
        p_even = int(b + b[::-1], 2)
        if p_even < 1_000_000 and str(p_even) == str(p_even)[::-1]:
            total_sum += p_even

        # Pattern 2: Odd length (e.g., 10 -> 101)
        p_odd = int(b + b[:-1][::-1], 2)
        if p_odd < 1_000_000 and str(p_odd) == str(p_odd)[::-1]:
            total_sum += p_odd

    return total_sum


# https://projecteuler.net/problem=39

# If p is the perimeter of a right angle triangle with integral length sides, {a, b, c},
# there are exactly three solutions for p = 120.
# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}
# For which value of p ≤ 1000, is the number of solutions maximised?


def euler39_euclid_gcd(x: int, y: int):
    if x < y:
        x, y = y, x
    while y != 0:
        # print(f"euclid_gcd({x}, {y})")
        y, x = x % y, y
    return x


def euler39():
    pMax = 1000
    # Euclid's formula for primitive a^2 + b^2 = c^2 says
    # m > n > 0 and mod(m-n,2)!=0 and gcd(m,n)=1
    # a = m^2 - n^2, b = 2mn, c = m^2 + n^2
    # And so, p = 2m(m+n)
    map = defaultdict(int)
    limit = int(math.sqrt(pMax / 2))
    max, maxi = 0, 0
    for m in range(limit):
        for n in range(m):
            if ((m - n) % 2 == 0) or (euler39_euclid_gcd(m, n) > 1):
                continue
            i, p = 1, 2 * m * (m + n)
            if p > pMax:
                break
            while (i * p) <= pMax:
                map[i * p] += 1
                i += 1
                if map[i * p] > max:
                    max, maxi = map[i * p], i * p
    return maxi


# https://projecteuler.net/problem=40


def euler40_nth_digit(n: int) -> Generator[int, int, None]:
    num_digits = 1
    prev_digits = 0
    num_prev_digits = 0
    digit = 0
    while True:
        nums_with_num_digits = 9 * (10 ** (num_digits - 1))
        now_digits = prev_digits + num_digits * nums_with_num_digits
        # print(f"now_digits = {now_digits}")
        while n <= now_digits:
            num = (n - prev_digits) // num_digits
            rem = (n - prev_digits) % num_digits
            if rem == 0:
                digit = num_digits - 1
            else:
                num, digit = num + 1, rem - 1
            n = yield int(str(num_prev_digits + num)[digit], 10)
        prev_digits = now_digits
        num_prev_digits += nums_with_num_digits
        num_digits += 1


def euler40():
    n = 1
    gen = euler40_nth_digit(n)
    result = next(gen)
    for i in range(1, 7):
        n = n * 10
        result *= gen.send(n)
    return result


# https://projecteuler.net/problem=41


def euler41_sieve(searchMax: int) -> list[bool]:
    # Instantly allocates blocks of memory in C under the hood
    primes = [True] * searchMax
    primes[0] = primes[1] = False

    # Set all even numbers starting at 4 to False in a single bound slice
    for i in range(4, searchMax, 2):
        primes[i] = False

    iterLimit = int(math.sqrt(searchMax)) + 1
    for i in range(3, iterLimit, 2):
        if primes[i]:
            # Step by 2*i to only touch odd multiples (e.g., 9, 15, 21...)
            for j in range(i * i, searchMax, 2 * i):
                primes[j] = False

    return primes


# Narayana’s combinatorial algorithm
# itertools.permutations("7654321") is the library way
def euler41_permutations(digits: list[int]) -> Generator[int, None, None]:

    # 1. Yield the initial state first so we don't miss it
    yield int("".join([str(i) for i in digits]))

    while True:
        pivot, target = -1, -1

        # Find the first element that is greater than its successor
        for j in range(len(digits) - 2, -1, -1):
            if digits[j] > digits[j + 1]:
                pivot = j
                break

        if pivot == -1:
            break  # Completely sorted in ascending order (base case reached)

        # Find the largest element to the right of pivot that is smaller than digits[pivot]
        for j in range(len(digits) - 1, pivot, -1):
            if digits[j] < digits[pivot]:
                target = j
                break
        # Swap the pivot and target
        digits[pivot], digits[target] = digits[target], digits[pivot]

        # Reverse the suffix to get the next largest lexicographical step down
        digits[pivot + 1 :] = digits[pivot + 1 :][::-1]

        yield int("".join([str(i) for i in digits]))
    return


def euler41() -> int:
    searchMax = 7654321
    primes = euler41_sieve(searchMax + 1)
    for i in euler41_permutations([7, 6, 5, 4, 3, 2, 1]):
        if primes[i]:
            return i
    return -1


# https://projecteuler.net/problem=47


def euler47() -> dict[int, list[int]]:
    sieve = defaultdict(list[int])
    num, count = 2, 0
    while True:
        if num in sieve:
            # composite
            for step in sieve[num]:
                sieve[num + step].append(step)
            if len(sieve[num]) == 4:
                count += 1
            else:
                count = 0
            if count == 4:
                return {
                    num - 3: sieve[num - 3],
                    num - 2: sieve[num - 2],
                    num - 1: sieve[num - 1],
                    num: sieve[num],
                }
        else:
            # prime
            sieve[2 * num].append(num)
            count = 0
        num += 1


# https://projecteuler.net/problem=55


def is_lychrel(n: int) -> bool:
    current = n
    for _ in range(50):
        # Reverse and add
        current += int(str(current)[::-1])

        # Check if the freshly generated sum is a palindrome
        if str(current) == str(current)[::-1]:
            return False  # Not a Lychrel number

    return True  # Fell through 50 iterations without hitting a palindrome


def euler55() -> int:
    # Count how many numbers below 10,000 are Lychrel numbers
    return sum(1 for i in range(1, 10000) if is_lychrel(i))


if __name__ == "__main__":
    print(f"Euler 36: {euler36()}")
    print(f"Euler 39: {euler39()}")
    print(f"Euler 40: {euler40()}")
    print(f"Euler 41: {euler41()}")
    print(f"Euler 47: {euler47()}")
    print(f"Euler 55: {euler55()}")
