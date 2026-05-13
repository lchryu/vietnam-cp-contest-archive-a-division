# Problem: Row and Column Sum

**Time Limit:** 1.0s  |  **Memory Limit:** 1G

## Problem Statement

Given a natural number $N$. We create a square table of size $N \times N$ containing the natural numbers from $1$ to $N^2$. The numbers are filled into the table according to the pattern shown below.

For $N=3$:

```text
1 2 3
7 8 9
4 5 6
```

For $N=4$:

```text
1 2 3 4
9 10 11 12
13 14 15 16
5 6 7 8
```

**Task:** Given two natural numbers $X$ and $Y$, compute the sum of all numbers in row $X$ and all numbers in column $Y$ of the table.

**Note:** If a number is at the intersection of row $X$ and column $Y$, it is counted only once.

## Input

The input consists of three lines. Each line contains one natural number, respectively $N$, $X$, and $Y$ ($1 \le X, Y \le N \le 10^8$).

## Output

Print one natural number: the required sum modulo **2026**.

## Example

**Input 1**
```text
4
2
3
```

**Output 1**
```text
67
```

---

# Detailed Explanation

## 1. Finding the Filling Pattern

Observe the table:

* The numbers from $1$ to $N^2$ are divided into $N$ groups, each containing $N$ consecutive numbers. Group $k$ contains the numbers from $(k-1)N+1$ to $kN$.
* Group 1 is placed in row 1.
* Group 2 is placed in the last possible row among the even-indexed original rows.
* Group 3 is placed in row 2.
* And so on.

The actual pattern is: odd-numbered original rows are placed in the upper half of the new table in increasing order, then even-numbered original rows are placed in the lower half of the new table in decreasing order.

**Row mapping:** Let $p(r)$ be the original row index placed at physical row $r$ in the new table.

* If $r \le (N+1)/2$: $p(r) = 2r - 1$.
* If $r > (N+1)/2$: $p(r) = \text{largest even row} - 2 \times (r - \frac{N+1}{2} - 1)$.

For $N=4$:

* $r=1 \rightarrow p(1)=1$.
* $r=2 \rightarrow p(2)=3$.
* $r=3 \rightarrow p(3)=4$.
* $r=4 \rightarrow p(4)=2$.

The original row order is $1, 3, 4, 2$.

## 2. Sum Formulas

The value at cell $(r, c)$ in the new table is:

> $Value(r, c) = (p(r) - 1) \times N + c$

**Sum of row $X$:**

> $\sum_{c=1}^N [(p(X)-1)N + c] = N^2(p(X)-1) + \frac{N(N+1)}{2}$

**Sum of column $Y$:**

> $\sum_{r=1}^N [(p(r)-1)N + Y] = N \times Y + N \sum_{r=1}^N (p(r)-1)$

Since $p(r)$ is a permutation of $1 \dots N$:

> $\sum p(r) = \frac{N(N+1)}{2}$

Therefore:

> $\text{Column sum } Y = NY + \frac{N^2(N-1)}{2}$

**Intersection $(X, Y)$:**

> $(p(X)-1)N + Y$

**Required sum:**

> $S = \text{row sum } X + \text{column sum } Y - \text{intersection}$

## 3. Modulo 2026

Because $N$ can be as large as $10^8$, we compute values modulo $2026$ during the calculation.

---

## Solution (Python)

```python
import sys

def solve():
    MOD = 2026

    n = int(sys.stdin.readline())
    x = int(sys.stdin.readline())
    y = int(sys.stdin.readline())

    mid = (n + 1) // 2
    if x <= mid:
        px = 2 * x - 1
    else:
        last_even = n if n % 2 == 0 else n - 1
        k = x - mid
        px = last_even - 2 * (k - 1)

    sum_row = (pow(n, 2, MOD) * ((px - 1) % MOD)) % MOD
    sum_row = (sum_row + (n * (n + 1) // 2) % MOD) % MOD

    sum_col = (n % MOD * (y % MOD)) % MOD
    sum_col = (sum_col + (pow(n, 2, MOD) * ((n - 1) % MOD) // 2) % MOD) % MOD

    intersect = (((px - 1) % MOD) * (n % MOD)) % MOD
    intersect = (intersect + (y % MOD)) % MOD

    result = (sum_row + sum_col - intersect) % MOD
    print(result)

solve()
```
