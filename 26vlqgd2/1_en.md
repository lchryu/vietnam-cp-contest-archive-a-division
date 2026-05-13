# Problem: Drawing Balls of All Three Colors

**Time Limit:** 1.0s  |  **Memory Limit:** 1G

## Problem Statement

In a box, there are $A$ red balls, $B$ blue balls, and $C$ yellow balls. Balls of the same color are identical. You randomly draw balls from the box without looking inside.

**Task:** Find the minimum number of balls you need to draw to be certain that the drawn balls contain all 3 colors: red, blue, and yellow.

## Input

The input consists of three lines. Each line contains one natural number, respectively $A$, $B$, and $C$ ($1 \le A, B, C \le 100$).

## Output

Print one natural number: the minimum number of balls that must be drawn.

## Examples

**Input 1**
```text
3
5
2
```

**Output 1**
```text
9
```

**Input 2**
```text
1
1
1
```

**Output 2**
```text
3
```

---

# Detailed Explanation

To solve this problem, we consider the **worst-case scenario**.

## 1. Analysis

The problem asks for the minimum number of balls needed to **guarantee** that all 3 colors appear. This means that even in the unluckiest possible drawing order, the result must contain red, blue, and yellow balls.

Suppose the numbers of balls are $A, B, C$. To delay getting all 3 colors for as long as possible, the worst case is drawing all balls from the two colors with the largest counts first.

## 2. Worst-Case Strategy

For example, suppose we have red (3), blue (5), and yellow (2).

* If we keep drawing blue and red balls first, these are the two colors with the largest counts.
* We may draw all 5 blue balls and still have only one color.
* Then we may draw all 3 red balls, making 8 balls total, but still only 2 colors.
* At this point, the remaining balls must be yellow.
* Therefore, the 9th ball is guaranteed to be yellow, and now we have all 3 colors.

## 3. General Formula

1. Find the two largest values among $A, B, C$.
2. The answer is the sum of those two largest values plus 1.

Equivalently:

> **`answer = (A + B + C) - min(A, B, C) + 1`**

Here, `min(A, B, C)` is the number of balls of the least frequent color. Subtracting it from the total gives the sum of the other two colors.

## 4. Example Explanation

For $A=3, B=5, C=2$:

* The smallest value is $2$.
* The answer is $(3 + 5 + 2) - 2 + 1 = 10 - 2 + 1 = 9$.

For $A=1, B=1, C=1$:

* The smallest value is $1$.
* The answer is $(1 + 1 + 1) - 1 + 1 = 3$.

---

## Solution (Python)

```python
import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

answer = A + B + C - min(A, B, C) + 1

print(answer)
```
