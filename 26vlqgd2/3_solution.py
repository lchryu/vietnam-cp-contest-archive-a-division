import sys


def count_same_parity(a, n):
    if a % 2 == 1:
        return (n + 1) // 2
    return n // 2


data = list(map(int, sys.stdin.read().split()))
n, x, y = data[0], data[1], data[2]

ans = 0

row_count = count_same_parity(x, n)
col_count = count_same_parity(y, n)

if (x + y) % 2 == 0:
    ans += row_count - 1
    ans += col_count - 1

    main_diag = n - abs(x - y)
    ans += main_diag - 1

    if x + y <= n + 1:
        anti_diag = x + y - 1
    else:
        anti_diag = 2 * n - x - y + 1
    ans += anti_diag - 1
else:
    ans += row_count
    ans += col_count

print(ans)
