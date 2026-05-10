# https://projecteuler.net/problem=7
# Sieve of Eratosthenes

import math


class Solution:
    def get_nth_prime(self, n: int):
        if n < 1:
            return None
        if n == 1:
            return 2
        if n == 2:
            return 3

        # Proven upper bound for p_n for n >= 6
        # For smaller n, we can just use a hardcoded small limit
        if n < 6:
            limit = 15
        else:
            # p_n < n * (ln(n) + ln(ln(n)))
            ln_n = math.log(n)
            ln_ln_n = math.log(ln_n)
            limit = int(n * (ln_n + ln_ln_n)) + 1

        sieve = [True] * limit
        sieve[0] = sieve[1] = False

        count = 0
        for p in range(2, limit):
            if sieve[p]:
                count += 1
                if count == n:
                    return p
                # Optimization: start marking at p*p
                # Only mark if p*p is within our current limit
                if p * p < limit:
                    for i in range(p * p, limit, p):
                        sieve[i] = False
        return None
