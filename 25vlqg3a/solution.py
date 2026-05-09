import sys

def solve():
    # Đọc tất cả các dòng từ input chuẩn
    input_data = sys.stdin.read().split()
    
    # Kiểm tra xem có đủ dữ liệu không
    if len(input_data) >= 2:
        N = int(input_data[0])
        M = int(input_data[1])
        
        # Áp dụng công thức tính người nhận kẹo cuối cùng
        # (M - 1) % N + 1
        result = (M - 1) % N + 1
        
        # In ra kết quả
        print(result)

if __name__ == '__main__':
    solve()
