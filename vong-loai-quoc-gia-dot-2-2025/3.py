digits = [int(input()) for _ in range(4)]

count = 0
a = set()
for x in digits:
    for y in digits:
        if x == 0:
            continue
        if y % 2 != 0:
            continue
        a.add(x * 10 + y)
        count += 1

print(len(a))

