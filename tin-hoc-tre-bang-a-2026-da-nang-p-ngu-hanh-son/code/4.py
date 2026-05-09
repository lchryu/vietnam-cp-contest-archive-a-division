def cnt2(h, m):
    return (str(h) + str(m)).count("2")
    # 02:20
    # "0220".cnt(2)


h1 = int(input())
m1 = int(input())

h2 = int(input())
m2 = int(input())

cur = h1 * 60 + m1
end = h2 * 60 + m2

t = 0

while True:
    h = cur // 60 
    m = cur % 60 
    
    t += cnt2(h, m)
    
    if cur == end: break
    
    cur = (cur + 1) % 1440
    
    
print(t)
    