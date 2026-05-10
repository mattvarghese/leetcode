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
* Break the problem down into component pieces
* Think about critical insights and their complexities
* Sum (1 ... n) = `n(n+1)/2`
* Sum of Squares (1 ... n) = `n(n+1)(2n+1)/6`
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
* Combination: `c(n,k) = n! / k!(n-k)!`

