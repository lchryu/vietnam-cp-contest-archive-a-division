def check(n):
    return n % 400 == 0 or n % 4 == 0 and n % 100 != 0

a = int(input())
b = int(input())
cnt = 0
for i in range(a, b + 1):
    if check(i):
        cnt += 1

print(cnt + (b - a + 1) * 365)