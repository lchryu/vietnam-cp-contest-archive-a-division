# Problem: Sum of Odd Parts

**Time Limit:** 1.0s  |  **Memory Limit:** 1G

## Problem Statement

Consider the sequence of natural numbers from $1$ to $N$: $1, 2, 3, 4, 5, 6, \dots, N$.

Transform each number in the sequence using the following rule:

* If the number is odd, keep it unchanged.
* If the number is even, repeatedly divide it by $2$ until an odd number is obtained, then stop.

Examples:

* $1 \rightarrow 1$
* $2 \rightarrow 1$
* $4 \rightarrow 2 \rightarrow 1$
* $6 \rightarrow 3$
* $12 \rightarrow 6 \rightarrow 3$
* $40 \rightarrow 20 \rightarrow 10 \rightarrow 5$

**Task:** Given a natural number $N$, compute the sum of the numbers in the new sequence after transforming all numbers from $1$ to $N$.

## Input

The input consists of one line containing a natural number $N$ ($1 \le N \le 10^8$).

## Output

Print one natural number: the required sum.

## Examples

**Input 1**
```text
6
```

**Output 1**
```text
14
```

**Input 2**
```text
10
```

**Output 2**
```text
36
```

---

# Detailed Explanation

## 1. Transformation Function

Let $f(i)$ be the number obtained after transforming $i$. According to the rule, $f(i)$ is exactly the **largest odd divisor of $i$**.

For example:

> $f(1)=1, f(2)=1, f(3)=3, f(4)=1, f(5)=5, f(6)=3$

For $N=6$, the sum is:

> $1 + 1 + 3 + 1 + 5 + 3 = 14$

## 2. Finding the Formula for $S(N) = \sum_{i=1}^N f(i)$

In the sequence from $1$ to $N$:

1. **Odd numbers:** $1, 3, 5, \dots, (2k+1) \le N$.
   For these numbers, $f(i) = i$.
   The number of odd values is $m = (N+1) // 2$.
   The sum of these odd values is $m^2$.

2. **Even numbers:** $2, 4, 6, \dots, 2k \le N$.
   For these numbers, $f(2k) = f(k)$.
   Therefore, the sum of $f(i)$ over the even numbers is $\sum_{k=1}^{\lfloor N/2 \rfloor} f(k)$, which is $S(\lfloor N/2 \rfloor)$.

**Recurrence:**

> **`S(N) = ((N + 1) // 2)^2 + S(N // 2)`**

## 3. Example for $N=10$

* $S(10) = (\text{number of odd values from 1 to 10})^2 + S(5)$.
  There are 5 odd values: $1, 3, 5, 7, 9$. Their sum is $5^2 = 25$.
* $S(5) = (\text{number of odd values from 1 to 5})^2 + S(2)$.
  There are 3 odd values: $1, 3, 5$. Their sum is $3^2 = 9$.
* $S(2) = (\text{number of odd values from 1 to 2})^2 + S(1)$.
  There is 1 odd value: $1$. Its sum is $1^2 = 1$.
* $S(1) = 1^2 + S(0) = 1$.

Therefore:

> $S(10) = 25 + 9 + 1 + 1 = 36$

## 4. Complexity

The recurrence halves $N$ at each step, so the complexity is $O(\log N)$. With $N=10^8$, only about 27 computation steps are needed.

---

## Solution (Python)

```python
import sys

def solve_s(n):
    if n == 0:
        return 0

    m = (n + 1) // 2
    return m * m + solve_s(n // 2)

line = sys.stdin.readline()
if line:
    n = int(line.strip())
    print(solve_s(n))
```
