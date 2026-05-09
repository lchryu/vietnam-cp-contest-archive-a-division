s = input()
digits = "0123456789"
best = "0"
for old_d in digits:
    for new_d in digits:
        if old_d == new_d:
            continue
        candidate = s.replace(old_d, new_d)
        if candidate[0] == "0" or sum(map(int, candidate)) % 9 != 0:
            continue
        best = max(best, candidate, key=lambda num: (len(num), num))

print(best)
