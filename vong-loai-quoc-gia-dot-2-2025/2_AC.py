def cnt_leap(n):
    return n // 400 + n // 4 - n // 100

a = int(input())
b = int(input())

leap = cnt_leap(b) - cnt_leap(a - 1)

print(leap + (b - a + 1) * 365)