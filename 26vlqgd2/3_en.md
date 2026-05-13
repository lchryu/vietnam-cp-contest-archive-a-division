# Problem: Queen

**Time Limit:** 1.0s  |  **Memory Limit:** 1G

## Problem Statement

Given a chessboard of size $N \times N$. Rows are numbered from $1$ to $N$ from top to bottom, and columns are numbered from $1$ to $N$ from left to right.

A queen is standing at cell $(x, y)$. The queen moves according to chess rules: in one move, it can move to any cell in the same row, same column, or same diagonal as its current cell, as long as the target cell is still inside the board.

**Task:** Count how many cells $(u, v)$ the queen can move to in exactly 1 move such that $u + v$ is even.

## Input

The input consists of three lines. Each line contains one natural number, respectively $N$, $x$, and $y$ ($1 \le x, y \le N \le 10^8$).

## Output

Print one natural number: the number of valid next cells.

## Examples

**Input 1**
```text
8
4
4
```

**Output 1**
```text
19
```

**Input 2**
```text
5
2
1
```

**Output 2**
```text
5
```

---

# Detailed Explanation

## 1. Movement Conditions

The queen at $(x, y)$ can move to $(u, v)$ if:

1. Same row: $u = x$ and $v \neq y$.
2. Same column: $v = y$ and $u \neq x$.
3. Main diagonal: $u - v = x - y$ and $(u, v) \neq (x, y)$.
4. Anti-diagonal: $u + v = x + y$ and $(u, v) \neq (x, y)$.

There is one additional condition: **$u + v$ must be even.**

## 2. Parity Analysis of $u + v$

* **Same row $x$:** $u + v = x + v$. For $x + v$ to be even, $v$ must have the same parity as $x$.
* **Same column $y$:** $u + v = u + y$. For $u + y$ to be even, $u$ must have the same parity as $y$.
* **Anti-diagonal:** Every cell on this diagonal has the same sum $u + v = x + y$.
  * If $x + y$ is even, every cell on this diagonal satisfies the condition.
  * If $x + y$ is odd, no cell on this diagonal satisfies the condition.
* **Main diagonal:** $u - v = x - y$, so $u + v = (u - v) + 2v = (x - y) + 2v$.
  Since $2v$ is always even, $u + v$ has the same parity as $x - y$, which has the same parity as $x + y$.
  * If $x + y$ is even, every cell on this diagonal satisfies the condition.
  * If $x + y$ is odd, no cell on this diagonal satisfies the condition.

## 3. Counting Cells

### Case 1: $x + y$ is odd

Only cells in the same row and same column can satisfy the condition.

* Same row $x$: cells $(x, v)$ such that $v \neq y$ and $v \equiv x \pmod 2$.
* Same column $y$: cells $(u, y)$ such that $u \neq x$ and $u \equiv y \pmod 2$.

### Case 2: $x + y$ is even

All 4 movement lines may contain valid cells.

* Same row $x$: count columns $v$ with the same parity as $x$.
* Same column $y$: count rows $u$ with the same parity as $y$.
* Main diagonal, excluding $(x, y)$.
* Anti-diagonal, excluding $(x, y)$.

**Number of integers with the same parity as $A$ in the range $[1, N]$:**

* If $A$ is odd: the number of odd integers is `(N + 1) // 2`.
* If $A$ is even: the number of even integers is `N // 2`.

## 4. Example 1: $N=8, x=4, y=4$

$x+y = 8$, which is even.

* Row 4: even $v$ values are $\{2, 6, 8\}$ after excluding $4$. There are 3 cells.
* Column 4: even $u$ values are $\{2, 6, 8\}$ after excluding $4$. There are 3 cells.
* Main diagonal ($u-v=0$): 8 cells, excluding $(4,4)$ leaves 7 cells.
* Anti-diagonal ($u+v=8$): 7 cells, excluding $(4,4)$ leaves 6 cells.

Total: $3 + 3 + 7 + 6 = 19$.

---

## Solution (Python)

```python
import sys

def count_same_parity(a, n):
    if a % 2 == 1:
        return (n + 1) // 2
    return n // 2

def solve():
    n = int(sys.stdin.readline())
    x = int(sys.stdin.readline())
    y = int(sys.stdin.readline())

    ans = 0

    ans += count_same_parity(x, n) - 1
    ans += count_same_parity(y, n) - 1

    if (x + y) % 2 == 0:
        ans += (n - abs(x - y)) - 1

        if x + y <= n + 1:
            ans += (x + y - 1) - 1
        else:
            ans += (2 * n - (x + y) + 1) - 1

    print(ans)

solve()
```
