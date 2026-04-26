def f(x: int) -> int:
    f: int = x // 3
    r: int = x % 3
    s: int = 0
    # for i in range(f):
    #     s += 9 * i + 6
    s += 9 * f * (f - 1) // 2 + 6 * f
    if r == 0:
        return s
    
    if f % 2 == 1:
        if r == 1:
            s += 3 * f + 3
        else:
            s += 3 * f + 3 + 3 * f + 2
    else:
        if r == 1:
            s += 3 * f + 1
        else:
            s += 3 * f + 1 + 3 * f + 2            
    
    return s     

l = int(input())
r = int(input())
print(f(r) - f(l - 1))

# 1 2 3 | 6 5 4 | 7 8 9 | 12
# 0       1        2       3
# f(10) = 57




'''
0-> (f - 1)
9 * f * (f - 1) // 2 + 6f 
'''
