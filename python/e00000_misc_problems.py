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


if __name__ == "__main__":
    print(f"Euler 36: {euler36()}")
    print(f"Euler 39: {euler39()}")
    print(f"Euler 40: {euler40()}")
