# Problem: Queen

**Time Limit:** 1.0s  |  **Memory Limit:** 1G

## Problem Statement

Given a chessboard of size $N \times N$. Rows are numbered from $1$ to $N$ from top to bottom, and columns are numbered from $1$ to $N$ from left to right.

A queen is standing at cell $(x, y)$. In one move, the queen can move to any cell in the same row, same column, or same diagonal as its current cell, as long as the target cell is still inside the board.

**Task:** Count how many cells $(u, v)$ the queen can move to in exactly one move such that $u + v$ is even.

## Input

The input consists of three integers $N, x, y$ ($1 \le x, y \le N \le 10^8$). They may be written on separate lines or separated by spaces.

## Output

Print one integer: the number of valid target cells.

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

## 1. Movement conditions

The queen at $(x, y)$ can move to a different cell $(u, v)$ if one of these conditions holds:

1. Same row: $u = x$.
2. Same column: $v = y$.
3. Main diagonal: $u - v = x - y$.
4. Anti-diagonal: $u + v = x + y$.

The target cell must also satisfy:

```python
(u + v) % 2 == 0
```

Since $N$ can be as large as $10^8$, iterating over the board is impossible. We need an `O(1)` formula.

---

## 2. Counting row and column cells

### Same row $x$

If the queen moves on row $x$, then $u = x$.

The even-sum condition becomes:

```text
x + v is even
```

So `v` must have the same parity as `x`.

### Same column $y$

If the queen moves on column $y$, then $v = y$.

The even-sum condition becomes:

```text
u + y is even
```

So `u` must have the same parity as `y`.

We use this helper function to count how many integers in `[1, N]` have the same parity as `a`:

```python
def count_same_parity(a, n):
    if a % 2 == 1:
        return (n + 1) // 2
    return n // 2
```

If `a` is odd, it returns the number of odd integers from `1` to `n`. If `a` is even, it returns the number of even integers from `1` to `n`.

---

## 3. Counting diagonal cells

### Main diagonal

The main diagonal through $(x, y)$ has equation:

```text
u - v = x - y
```

The number of cells on this diagonal is:

```python
main_diag = n - abs(x - y)
```

### Anti-diagonal

The anti-diagonal through $(x, y)$ has equation:

```text
u + v = x + y
```

The number of cells on this diagonal is:

```python
if x + y <= n + 1:
    anti_diag = x + y - 1
else:
    anti_diag = 2 * n - x - y + 1
```

---

## 4. The important edge case: odd x + y

This is where the old solution was easy to get wrong.

### If $x + y$ is even

The current cell $(x, y)$ also has an even coordinate sum.

Therefore, when we count valid cells on the row, column, main diagonal, and anti-diagonal, the current cell is included in each count.

But the queen must move to another cell, so we subtract the current cell once from each line:

```python
ans += row_count - 1
ans += col_count - 1
ans += main_diag - 1
ans += anti_diag - 1
```

Both diagonals are valid in this case, because every cell on either diagonal through $(x, y)$ has the same sum parity as $(x, y)$.

### If $x + y$ is odd

The current cell $(x, y)$ has an odd coordinate sum.

On the row:

- We need `v` to have the same parity as `x`.
- Since `x + y` is odd, `y` has the opposite parity from `x`.
- So the current cell is not counted in the row count.

On the column:

- We need `u` to have the same parity as `y`.
- Since `x + y` is odd, `x` has the opposite parity from `y`.
- So the current cell is not counted in the column count.

The diagonals contribute nothing, because every cell on either diagonal through $(x, y)$ has odd coordinate sum.

So in this case:

```python
ans = row_count + col_count
```

We must not subtract `1`.

---

## 5. Three implementations

### Solution 1: Iterate over the whole board - $O(N^2)$

This is the most direct approach: iterate over every cell `(u, v)`, check whether the queen can move there, then check whether `(u + v)` is even.

This version is useful for understanding the problem or passing very small tests, but it cannot pass when `N <= 10^8`.

```python
n = int(input())
x = int(input())
y = int(input())

ans = 0

for u in range(1, n + 1):
    for v in range(1, n + 1):
        if u == x and v == y:
            continue

        same_row = (u == x)
        same_col = (v == y)
        same_diag = (abs(u - x) == abs(v - y))

        if same_row or same_col or same_diag:
            if (u + v) % 2 == 0:
                ans += 1

print(ans)
```

### Solution 2: Iterate over the queen's 4 lines - $O(N)$

Instead of scanning the whole board, we only scan:

- The queen's row.
- The queen's column.
- The main diagonal.
- The anti-diagonal.

This is faster than solution 1, but still too slow for `N = 10^8`.

```python
n = int(input())
x = int(input())
y = int(input())

ans = 0

# Same row
for v in range(1, n + 1):
    if v != y and (x + v) % 2 == 0:
        ans += 1

# Same column
for u in range(1, n + 1):
    if u != x and (u + y) % 2 == 0:
        ans += 1

# Main diagonal: u - v = x - y
for u in range(1, n + 1):
    v = u - (x - y)
    if 1 <= v <= n and u != x and (u + v) % 2 == 0:
        ans += 1

# Anti-diagonal: u + v = x + y
for u in range(1, n + 1):
    v = x + y - u
    if 1 <= v <= n and u != x and (u + v) % 2 == 0:
        ans += 1

print(ans)
```

### Solution 3: Use formulas - $O(1)$

This is the version to submit for full score.

```python
import sys


def count_same_parity(a, n):
    if a % 2 == 1:
        return (n + 1) // 2
    return n // 2


data = list(map(int, sys.stdin.read().split()))
n, x, y = data[0], data[1], data[2]

row_count = count_same_parity(x, n)
col_count = count_same_parity(y, n)

if (x + y) % 2 == 0:
    ans = row_count - 1
    ans += col_count - 1

    main_diag = n - abs(x - y)
    ans += main_diag - 1

    if x + y <= n + 1:
        anti_diag = x + y - 1
    else:
        anti_diag = 2 * n - x - y + 1
    ans += anti_diag - 1
else:
    ans = row_count + col_count

print(ans)
```

---

## 6. Example checks

### Example 1

For $N = 8, x = 4, y = 4$:

```text
x + y = 8
```

This is even.

- Row 4: even columns are `2, 4, 6, 8`; excluding column `4` leaves `3` cells.
- Column 4: even rows are `2, 4, 6, 8`; excluding row `4` leaves `3` cells.
- Main diagonal has `8` cells; excluding the current cell leaves `7` cells.
- Anti-diagonal has `7` cells; excluding the current cell leaves `6` cells.

Total:

```text
3 + 3 + 7 + 6 = 19
```

### Example 2

For $N = 5, x = 2, y = 1$:

```text
x + y = 3
```

This is odd.

- Row 2: we need even columns, which are `2, 4`, so there are `2` cells.
- Column 1: we need odd rows, which are `1, 3, 5`, so there are `3` cells.
- Both diagonals contribute `0` valid cells.

Total:

```text
2 + 3 = 5
```

---

## 7. Complexity

The algorithm only uses a few arithmetic operations and does not iterate over the board.

```text
Time complexity: O(1)
Memory usage: O(1)
```
