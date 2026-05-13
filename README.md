# LeetCode Solutions

A collection of LeetCode problems solved across multiple programming languages.

## 🏗️ Repository Architecture

The repository will be organized by language to ensure environment isolation and optimal IDE support.

Current plan for the structure: 

```text
.
├── python/          # Python 3.13+ (venv-based, Type Hints, Ruff)
├── typescript/      # Node.js 20+, Vitest for unit testing
├── cpp/             # Modern C++ (C++20), CMake build system
├── rust/            # Cargo-managed crates
└── .github/         # CI/CD workflows for automated solution verification
```

## 📊 Progress Dashboard

| #   | Problem | Difficulty | Python | TypeScript | C++ | Rust |
| :-- | :--- | :--- | :---: | :---: | :---: | :---: |
| 001 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | ✅ | ❌ | ❌ | ❌ |
| 002 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | ❌ | ❌ | ✅ | ❌ |
| 003 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | ✅ | ❌ | ❌ | ❌ |
| 004 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | ❌ | ❌ | ✅ | ❌ |

**Legend:** ✅ Solved | 🏗️ In Progress | ❌ Not Started

---

## 🛠️ Local Development Setup

### Python
```bash
cd python
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

### C++
```bash
cd cpp
mkdir build && cd build
cmake ..
make
./run_tests
```

### TypeScript
```bash
cd typescript
npm install
npm test
```


# Other Notes:

* Always ask,
  * What is the current power of n for `big O`?
  * Can I do it in one fewer power of n?
  * Should you convert `float`s to `int`s to avoid precision errors?
* Break the problem down into component pieces
* Think about critical insights and their complexities
* Sum (1 ... n) = `n(n+1)/2`
* Sum of Squares (1 ... n) = `n(n+1)(2n+1)/6`
* To find smallest bit set, `x = val&-val` then `x.bit_length() - 1` (bit  indices start at 0. 2^0 = 1)
  * `bit_length()` returns number of bits required to represent in binary. 
  * For powers of 2, this is the highest bit. 
  * The lowest bit set, our result of `val & -val` is always a power of 2
* To see if something is a power of two: `x BitwiseAND (x-1) == 0`
  * `is_power_of_two = (x > 0) and (x & (x - 1) == 0)`
  * To count number of bits set (**Brian Kernighan’s Algorithm**):
  * Because every call to `x & (x - 1)` removes exactly one set bit, you simply count how many times you can perform the operation before the number becomes zero.
    ```python
    def count_set_bits(n):
      count = 0
      while n > 0:
          n &= (n - 1)
          count += 1
      return count
    ```
* If a number N can be prime factorized as p1<sup>e1</sup> * p2<sup>e2</sup> * ... * pk<sup>ek</sup>
  * Total number of factors of N is `(e1+1)(e2+1)...(ek+1)`
* For max or min in a sliding window, use a deque like in `p__009`
* **Sieve of Eratosthenes** for primes, see `e00007`
* **Euclid's formula** to find pythagorean triplets (`a*a+b*b=c*c` or a<sup>2</sup>+b<sup>2</sup>=c<sup>2</sup>) :
  * `a = m*m - n*n`  (m<sup>2</sup> - n<sup>2</sup>)
  * `b = 2mn`
  * `c = m*m + n*n`  (m<sup>2</sup> + n<sup>2</sup>)
  * Also, if `a*a + b*b = c*c`, then multiplying with a scaling factor, `ka*ka + kb*kb = kc*kc`
  * Triplets where scaling factor is 1 are **Primitive Pythagorean Triplets**
* Permutation: `p(n,k) = n! / (n-k)!`
* Combination: `c(n,k) = n! / k!(n-k)!` without repetitions
  * With repetitions: = `c(n+k-1,k) = (n+k-1)! / k! (n-1)!`  (or k items into n bins)



# Analytical Derivation of Power Sums

The general strategy for deriving the formula for the sum of $p$-th powers relies on the **Method of Differences** (telescoping sums) and the **Binomial Theorem**.

# 1. The Binomial Expansion
To derive the sum of powers up to $k$, we utilize the expansion of $(n+1)^{k+1}$:
$$(n+1)^k = \sum_{r=0}^{k} \binom{k}{r} n^{k-r}$$

# 2. The Method of Differences
By shifting the $n^k$ term to the left side, we create a difference identity:
$$(n+1)^k - n^k = \binom{k}{1}n^{k-1} + \binom{k}{2}n^{k-2} + \dots + \binom{k}{k}$$

When we sum both sides from $1$ to $N$, the left side "telescopes," meaning all intermediate terms cancel out except for the boundaries:
$$\sum_{n=1}^N ((n+1)^k - n^k) = (N+1)^k - 1^k$$

# 3. Solving for the $k$-th Power
The right side of the summation becomes a combination of lower-order power sums:
$$(N+1)^k - 1 = \binom{k}{1}\sum n^{k-1} + \binom{k}{2}\sum n^{k-2} + \dots + \binom{k}{k}\sum 1$$

To find the formula for the sum of $k-1$ powers, you simply isolate the $\sum n^{k-1}$ term and substitute the known formulas for all lower-order sums.

# 4. Summary of Common Results
*   **Sum of Integers ($k=2$):** $\sum_{n=1}^N n = \frac{N(N+1)}{2}$
*   **Sum of Squares ($k=3$):** $\sum_{n=1}^N n^2 = \frac{N(N+1)(2N+1)}{6}$
*   **Sum of Cubes ($k=4$):** $\sum_{n=1}^N n^3 = \left[ \frac{N(N+1)}{2} \right]^2$
