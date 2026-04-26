def sum_n(n: int) -> int:
    if n <= 0:
        return 0
    k = n // 3
    m = n % 3
    
    # Tổng của k nhóm đầy đủ (mỗi nhóm i có tổng là 9i - 3)
    # Sum_{i=1 to k} (9i - 3) = 9 * k*(k+1)/2 - 3k = (9k^2 + 9k - 6k) / 2 = (9k^2 + 3k) / 2
    total = (9 * k * k + 3 * k) // 2
    
    # Xét nhóm thứ k + 1
    next_group_idx = k + 1
    start_val = 3 * k + 1
    
    if m > 0:
        if next_group_idx % 2 == 1:
            # Nhóm lẻ: tăng dần 3k+1, 3k+2, 3k+3
            for i in range(m):
                total += (start_val + i)
        else:
            # Nhóm chẵn: giảm dần 3k+3, 3k+2, 3k+1
            # Các giá trị là: (3k+3), (3k+2), (3k+1)
            # m=1 -> 3k+3
            # m=2 -> (3k+3) + (3k+2)
            current_val = 3 * k + 3
            for i in range(m):
                total += (current_val - i)
                
    return total

try:
    import sys
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        l = int(input_data[0])
        r = int(input_data[1])
        print(sum_n(r) - sum_n(l - 1))
except EOFError:
    pass
