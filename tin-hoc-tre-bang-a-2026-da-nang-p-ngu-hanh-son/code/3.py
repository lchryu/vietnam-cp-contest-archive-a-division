k = int(input())
s = input().strip()
#k = 2
#s = "abacbc"
from collections import  Counter
# print(Counter(s)) # Counter({'a': 2, 'b': 2, 'c': 2})

cnt = Counter(s)
flag = True 
for c in Counter(s):
    if cnt[c] % k != 0:
        flag = False 
        print(-1)
        break

if flag:
    res = ""
    for c in sorted(cnt):
        res += c * (cnt[c] // k)
    print(res * k)