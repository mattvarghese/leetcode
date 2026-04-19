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
