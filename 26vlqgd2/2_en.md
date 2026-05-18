# Problem: Digital Clock

**Time Limit:** 1.0s  |  **Memory Limit:** 1G

## Problem Statement

Pink likes looking at a digital clock displayed in the format $HH:MM$, where the hour ranges from $00$ to $23$ and the minute ranges from $00$ to $59$.

Pink calls a time **"harmonious"** if the sum of the digits of the hour is exactly equal to the sum of the digits of the minute.

* For example, $14:32$ is harmonious because $1+4 = 3+2 = 5$.
* $07:07$ is also harmonious because $0+7 = 0+7 = 7$.

**Task:** The current clock time is $H$ hours and $M$ minutes. Count how many harmonious times appear from the current time through the next $K$ minutes, including the current time. This interval may continue into the next day or even later days.

## Input

The input consists of three lines. Each line contains one natural number, respectively $H$, $M$, and $K$ ($0 \le H \le 23; 0 \le M \le 59; 0 \le K \le 2880$).

## Output

Print one natural number: the number of harmonious times found.

## Examples

**Input 1**
```text
23
58
5
```

**Output 1**
```text
1
```

**Input 2**
```text
7
7
0
```

**Output 2**
```text
1
```

---

# Detailed Explanation

## 1. Definition of a Harmonious Time

A time $HH:MM$ is harmonious when:

`tens_digit_of_hour + ones_digit_of_hour = tens_digit_of_minute + ones_digit_of_minute`

Example:

* Hour $23$: digit sum is $2 + 3 = 5$.
* Minute $58$: digit sum is $5 + 8 = 13$.
* Since $5 \neq 13$, this time is not harmonious.

## 2. Approach: Simulation

Since the maximum value of $K$ is $2880$ minutes, exactly 2 days, we can simply simulate each minute and check the condition.

### Steps

1. Start from time $(H, M)$.
2. Repeat $K+1$ times, because the current time is included:
   * Compute the digit sum of $H$: `sum_h = (H // 10) + (H % 10)`.
   * Compute the digit sum of $M$: `sum_m = (M // 10) + (M % 10)`.
   * If `sum_h == sum_m`, increase the counter.
   * Move the time forward by 1 minute:
     * $M = M + 1$.
     * If $M = 60$, set $M = 0$ and increase $H$ by 1.
     * If $H = 24$, set $H = 0$.

## 3. Example 1

For $(H=23, M=58, K=5)$:

* Minute 0: $23:58 \rightarrow 2+3=5, 5+8=13 \rightarrow$ No.
* Minute 1: $23:59 \rightarrow 2+3=5, 5+9=14 \rightarrow$ No.
* Minute 2: $00:00 \rightarrow 0+0=0, 0+0=0 \rightarrow$ Harmonious. Count = 1.
* Minute 3: $00:01 \rightarrow 0, 1 \rightarrow$ No.
* Minute 4: $00:02 \rightarrow 0, 2 \rightarrow$ No.
* Minute 5: $00:03 \rightarrow 0, 3 \rightarrow$ No.

The answer is $1$.

---

## Solution (Python)

```python
import sys

def sum_digits(n):
    return (n // 10) + (n % 10)

h = int(sys.stdin.readline())
m = int(sys.stdin.readline())
k = int(sys.stdin.readline())

count = 0

for _ in range(k + 1):
    if sum_digits(h) == sum_digits(m):
        count += 1

    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0

print(count)
```

### Approach 2: Using a `for` loop (Total minutes conversion)
Instead of manually managing the minutes and hours, we can convert the current time to the total elapsed minutes of the day, then use the modulo operator to update the time efficiently.

```python
import sys

def sum_digits(n: int) -> int:
    return n // 10 + n % 10

def is_harmonious(h: int, m: int) -> bool:
    return sum_digits(h) == sum_digits(m)

h = int(sys.stdin.readline())
m = int(sys.stdin.readline())
k = int(sys.stdin.readline())

current_minutes = h * 60 + m
harmonious_count = 0

for _ in range(k + 1):
    current_h = (current_minutes // 60) % 24
    current_m = current_minutes % 60
    
    if is_harmonious(current_h, current_m):
        harmonious_count += 1
        
    current_minutes = (current_minutes + 1) % 1440

print(harmonious_count)
```

### Approach 3: Using a `while` loop
We can use a `while True` loop and keep track of the elapsed minutes. It is important to check the break condition (whether $K$ minutes have passed) immediately after evaluating the current time.

```python
import sys

def sum_digits(n: int) -> int:
    return n // 10 + n % 10

def is_harmonious(h: int, m: int) -> bool:
    return sum_digits(h) == sum_digits(m)

h = int(sys.stdin.readline())
m = int(sys.stdin.readline())
k = int(sys.stdin.readline())

current_minutes = h * 60 + m
harmonious_count = 0
elapsed_minutes = 0

while True:
    current_h = (current_minutes // 60) % 24
    current_m = current_minutes % 60
    
    if is_harmonious(current_h, current_m):
        harmonious_count += 1
        
    if elapsed_minutes == k:
        break
        
    elapsed_minutes += 1
    current_minutes = (current_minutes + 1) % 1440

print(harmonious_count)
```
