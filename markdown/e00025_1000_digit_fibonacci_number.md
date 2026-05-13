# Fibonacci Sequence: Closed-Form Derivation and Application

This document outlines the architectural transition from an iterative recurrence to an analytical $O(1)$ solution for the Fibonacci sequence.

Ref: [https://projecteuler.net/problem=25](https://projecteuler.net/problem=25)

## 1. Finding the Growth Rates ($r$)
We begin with the standard Fibonacci recurrence:
$$F_n = F_{n-1} + F_{n-2}$$

To find a closed-form solution, we assume the solution takes the form of a geometric growth $F_n = r^n$. Substituting this into the recurrence gives:
$$r^n = r^{n-1} + r^{n-2}$$

Dividing both sides by $r^{n-2}$ (assuming $r \neq 0$), we obtain the **characteristic equation**:
$$r^2 - r - 1 = 0$$

Using the quadratic formula, we solve for the two roots ($r_1$ and $r_2$):
*   **$\phi$ (The Golden Ratio):** $\frac{1 + \sqrt{5}}{2} \approx 1.618$
*   **$\psi$:** $\frac{1 - \sqrt{5}}{2} \approx -0.618$

## 2. Deriving the Coefficients ($A$ and $B$)
Since the recurrence is linear, the general solution is a weighted sum (linear combination) of our two roots:
$$F_n = A\phi^n + B\psi^n$$

We determine the constants $A$ and $B$ using the initial boundary conditions of the Fibonacci sequence ($F_0 = 0, F_1 = 1$).

**At $n = 0$:**
$$A\phi^0 + B\psi^0 = 0 \implies A + B = 0 \implies B = -A$$

**At $n = 1$:**
$$A\phi^1 + B\psi^1 = 1$$

Substitute $B = -A$ into the $n=1$ equation:
$$A\phi - A\psi = 1 \implies A(\phi - \psi) = 1$$

Given that $\phi - \psi = \sqrt{5}$, we find our constants:
*   **$A = \frac{1}{\sqrt{5}}$**
*   **$B = -\frac{1}{\sqrt{5}}$**

## 3. The Superposition Principle
Because the system is linear, if $\phi^n$ and $\psi^n$ both satisfy the recurrence, any weighted sum $G_n = A\phi^n + B\psi^n$ must also satisfy it.

**Proof:**
Substitute $G_n$ into the recurrence $G_n - G_{n-1} - G_{n-2}$:
$$(A\phi^n + B\psi^n) - (A\phi^{n-1} + B\psi^{n-1}) - (A\phi^{n-2} + B\psi^{n-2})$$

Group terms by coefficients:
$$A(\phi^n - \phi^{n-1} - \phi^{n-2}) + B(\psi^n - \psi^{n-1} - \psi^{n-2})$$

Since the expressions inside the parentheses are the characteristic equations for the roots (which equal zero), the entire expression becomes:
$$A(0) + B(0) = 0$$

Thus, **Binet's Formula** is established:
$$F_n = \frac{\phi^n - \psi^n}{\sqrt{5}}$$

## 4. Solving for 1,000 Digits
To find the first index $n$ where $F_n$ has 1,000 digits, we require $F_n \ge 10^{999}$. Using the property that $\psi^n$ approaches zero as $n$ grows, we approximate:
$$\frac{\phi^n}{\sqrt{5}} \ge 10^{999}$$

Taking the $\log_{10}$ of both sides:
$$n \log_{10}(\phi) - \log_{10}(\sqrt{5}) \ge 999$$

Solving for $n$:
$$n \ge \frac{999 + \log_{10}(\sqrt{5})}{\log_{10}(\phi)}$$

Using $\log_{10}(\phi) \approx 0.20898$ and $\log_{10}(\sqrt{5}) \approx 0.34948$:
$$n \ge \frac{999 + 0.34948}{0.20898} \approx 4781.85$$

Rounding up to the nearest integer, the first term with 1,000 digits is at index **4782**.


