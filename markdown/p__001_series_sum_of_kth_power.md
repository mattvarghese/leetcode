# Analytical Derivation of Power Sums

The general strategy for deriving the formula for the sum of $k$-th powers relies on the **Method of Differences** (telescoping sums) and the **Binomial Theorem**. By looking at a power one degree higher than our target, we create an algebraic chain reaction where all intermediate terms cancel out, leaving a solvable equation for the desired sum.

---

## 1. Concrete Derivation: Sum of Integers ($k=1$)

To find the sum of first powers ($\sum_{n=1}^N n^1$), we begin with the binomial expansion of the power one degree higher: $(n+1)^2$.

### Step A: Establish the Difference Identity

Using basic algebra:


$$(n+1)^2 = n^2 + 2n + 1$$

Isolate the difference by moving $n^2$ to the left side:


$$(n+1)^2 - n^2 = 2n + 1$$

### Step B: Apply the Summation

Sum both sides of this identity from $n=1$ to $N$:


$$\sum_{n=1}^N \left((n+1)^2 - n^2\right) = \sum_{n=1}^N (2n + 1)$$

### Step C: Telescope the Left Side

If we expand the left side sequentially, adjacent terms cancel out symmetrically:


$$\left(2^2 - 1^2\right) + \left(3^2 - 2^2\right) + \left(4^2 - 3^2\right) + \dots + \left((N+1)^2 - N^2\right)$$

Every intermediate square disappears, collapsing the entire left side down to its boundaries:


$$\text{Left Side} = (N+1)^2 - 1^2 = N^2 + 2N$$

### Step D: Isolate the Target Sum ($S_1$)

Split the right side summation into individual parts and pull out constant factors. Let $S_1 = \sum_{n=1}^N n$:


$$\sum_{n=1}^N (2n + 1) = 2\left(\sum_{n=1}^N n\right) + \sum_{n=1}^N 1 = 2S_1 + N$$

Set the simplified Left Side equal to the Right Side:


$$N^2 + 2N = 2S_1 + N$$

$$N^2 + N = 2S_1$$

$$N(N+1) = 2S_1$$

$$S_1 = \frac{N(N+1)}{2}$$

---

## 2. Concrete Derivation: Sum of Squares ($k=2$)

To find the sum of squares ($\sum_{n=1}^N n^2$), we shift up one degree higher and expand $(n+1)^3$.

### Step A: Establish the Difference Identity

$$(n+1)^3 = n^3 + 3n^2 + 3n + 1$$

$$(n+1)^3 - n^3 = 3n^2 + 3n + 1$$

### Step B: Apply Summation and Telescope

Summing from $1$ to $N$ causes the left side to telescope identical to before:


$$(N+1)^3 - 1^3 = \sum_{n=1}^N (3n^2 + 3n + 1)$$

Expand the left side polynomial:


$$N^3 + 3N^2 + 3N = 3\left(\sum_{n=1}^N n^2\right) + 3\left(\sum_{n=1}^N n\right) + \sum_{n=1}^N 1$$

### Step C: Substitute Known Lower-Order Sums

Let $S_2 = \sum_{n=1}^N n^2$. Substitute our previously derived formula for $\sum n$:


$$N^3 + 3N^2 + 3N = 3S_2 + 3\left[\frac{N(N+1)}{2}\right] + N$$

### Step D: Algebraic Optimization

Multiply the entire equation by 2 to eliminate fractions:


$$2N^3 + 6N^2 + 6N = 6S_2 + 3N(N+1) + 2N$$

$$2N^3 + 6N^2 + 6N = 6S_2 + 3N^2 + 3N + 2N$$

$$2N^3 + 3N^2 + N = 6S_2$$

Factor out $N$ from the left polynomial:


$$N(2N^2 + 3N + 1) = 6S_2$$

$$N(N+1)(2N+1) = 6S_2$$

$$S_2 = \frac{N(N+1)(2N+1)}{6}$$

---

## 3. Concrete Derivation: Sum of Cubes ($k=3$)

To isolate the sum of cubes ($\sum_{n=1}^N n^3$), we expand $(n+1)^4$.

### Step A: Establish the Difference Identity

$$(n+1)^4 = n^4 + 4n^3 + 6n^2 + 4n + 1$$

$$(n+1)^4 - n^4 = 4n^3 + 6n^2 + 4n + 1$$

### Step B: Apply Summation and Telescope

$$(N+1)^4 - 1^4 = 4\left(\sum_{n=1}^N n^3\right) + 6\left(\sum_{n=1}^N n^2\right) + 4\left(\sum_{n=1}^N n\right) + \sum_{n=1}^N 1$$

Expand the left side polynomial:


$$N^4 + 4N^3 + 6N^2 + 4N = 4S_3 + 6S_2 + 4S_1 + N$$

### Step C: Substitute Known Values ($S_1, S_2$)

$$N^4 + 4N^3 + 6N^2 + 4N = 4S_3 + 6\left[\frac{N(N+1)(2N+1)}{6}\right] + 4\left[\frac{N(N+1)}{2}\right] + N$$

$$N^4 + 4N^3 + 6N^2 + 4N = 4S_3 + N(N+1)(2N+1) + 2N(N+1) + N$$

Expand out the lower-order terms on the right side:


$$N^4 + 4N^3 + 6N^2 + 4N = 4S_3 + (2N^3 + 3N^2 + N) + (2N^2 + 2N) + N$$

$$N^4 + 4N^3 + 6N^2 + 4N = 4S_3 + 2N^3 + 5N^2 + 4N$$

### Step D: Solve for $S_3$

Subtract the polynomial terms from both sides:


$$N^4 + 2N^3 + N^2 = 4S_3$$

Factor the left side completely:


$$N^2(N^2 + 2N + 1) = 4S_3$$

$$N^2(N+1)^2 = 4S_3$$

$$S_3 = \left[\frac{N(N+1)}{2}\right]^2$$

---

## 4. The General Framework

The pattern demonstrated above scales to any arbitrary integer power using the formal tools of the **Binomial Theorem**.

### The General Binomial Expansion

To derive the power sum formula up to power $k$, we use the expansion of $(n+1)^{k+1}$:


$$(n+1)^{k+1} = \sum_{r=0}^{k+1} \binom{k+1}{r} n^{(k+1)-r}$$

### The General Difference Identity

Extract the leading $n^{k+1}$ term ($r=0$) and shift it to the left to construct the telescoping core:


$$(n+1)^{k+1} - n^{k+1} = \sum_{r=1}^{k+1} \binom{k+1}{r} n^{(k+1)-r}$$

### The Telescoping System Equation

Summing both sides from $1$ to $N$ completely reduces the left side to its boundaries, creating a system of interconnected recursive sums:


$$(N+1)^{k+1} - 1 = \binom{k+1}{1}\sum n^k + \binom{k+1}{2}\sum n^{k-1} + \dots + \binom{k+1}{k+1}\sum 1$$

To find the explicit closed-form formula for any arbitrary $k$-th power sum, you isolate the $\sum n^k$ term and substitute the known, pre-calculated polynomial formulas of all lower-order sums.

---

## 5. Summary of Core Polynomial Formulas

* **Sum of Integers ($k=1$):** 
$$\sum_{n=1}^N n = \frac{N(N+1)}{2}$$


* **Sum of Squares ($k=2$):** 
$$\sum_{n=1}^N n^2 = \frac{N(N+1)(2N+1)}{6}$$


* **Sum of Cubes ($k=3$):** 
$$\sum_{n=1}^N n^3 = \left[ \frac{N(N+1)}{2} \right]^2$$