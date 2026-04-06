def count_2(h, m):
    return str(h).zfill(2).count('2') + str(m).zfill(2).count('2')

# h1 = int(input())
# m1 = int(input())
# h2 = int(input())
# m2 = int(input())

# start = h1 * 60 + m1
# end = h2 * 60 + m2

# total = 0
# cur = start

# while True:
#     h = cur // 60
#     m = cur % 60
    
#     total += count_2(h, m)
    
#     if cur == end:
#         break
    
#     cur = (cur + 1) % 1440

# print(total)



print(count_2(20, 2))
print(count_2(2, 22))