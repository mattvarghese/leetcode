# Reciprocal Cycles: Long Division to Modular Order

This document outlines the optimization of finding the longest recurring cycle in unit fractions for d < 1000 by shifting from iterative long division to modular arithmetic.

Ref: https://projecteuler.net/problem=26

## 1. The Long Division State Machine
The cycle length of a unit fraction 1/d is determined by the sequence of remainders in the long division process. 
*   State Repetition: A cycle begins as soon as a remainder repeats.
*   Termination: If a remainder becomes 0, the decimal terminates (occurs when prime factors of d are only 2 or 5).
*   Maximum Length: For any denominator d, there are at most d-1 possible non-zero remainders. Therefore, the maximum cycle length is d-1.

## 2. Full Reptend Primes
A Full Reptend Prime (p) is a prime where the period of 1/p is exactly p-1.
*   This represents the "worst-case" scenario for cycle length.
*   Primitive Root: Mathematically, this occurs when 10 is a primitive root modulo p.
*   Constraint: For d < 1000, the theoretical maximum cycle length is 996 (from the prime 997).

## 3. The Power Test (Primitive Root Verification)
To verify if a prime p is a full reptend prime without performing long division, we use the property of Multiplicative Order. p is a full reptend prime if and only if:
1. 10^(p-1) mod p = 1 (Guaranteed by Fermat's Little Theorem).
2. 10^((p-1)/q) mod p != 1 for all prime factors q of p-1.

This "short-circuit" ensures that p-1 is the *smallest* exponent that results in a remainder of 1, confirming a full-length cycle.

## 4. Optimized Search Algorithm
As a systems architecture choice, we utilize a downward search strategy to minimize computation:

1.  Sieve: Generate all primes up to 1000 using the Sieve of Eratosthenes.
2.  Downward Iteration: Begin at the largest prime (p = 997) and move backwards.
3.  Factorization: For each prime, find the unique prime factors of p-1.
4.  Verification: Perform the Power Test:
    * Check if any factor results in a collapse
    * if all(pow(10, (p-1)//q, p) != 1 for q in prime_factors_of_p_minus_1):
    *    return p # Global maximum found
    
5.  Termination: The first prime that passes this test is the answer, as no d smaller than the current p can produce a cycle length >= p.

## 5. Critical Technical Insights
*   Precision: Using pow(base, exp, mod) avoids integer overflow and floating-point precision errors.
*   Complexity: This transforms an O(N^2) simulation into a targeted search of the prime space near the upper bound.
*   Coprimality: Factors of 2 and 5 in d do not affect the length of the recurring cycle; they only affect the non-repeating prefix.