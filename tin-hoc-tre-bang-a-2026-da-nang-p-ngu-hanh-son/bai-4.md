# Bài 4. Tính tích

[⬅ Quay lại mục lục](README.md)

## 📌 Đề bài
Cho một dãy số nguyên dương `N` phần tử.
Hãy chia dãy thành hai phần không rỗng: phần trái và phần phải
(giữ nguyên thứ tự ban đầu).

Gọi:
- `S1` là tổng các phần tử của phần trái
- `S2` là tổng các phần tử của phần phải

Hãy tìm cách chia sao cho tích `S1 x S2` là lớn nhất.

---

## 📥 Input
- Dòng 1: số nguyên `N` (`2 <= N <= 10^5`)
- Dòng 2: `N` số nguyên `A[i]` (`1 <= A[i] <= 10^9`)

---

## 📤 Output
- In ra một số nguyên là giá trị lớn nhất của `S1 x S2`.

---

## 🧪 Test mẫu
Input:
```text
4
1 2 3 4
```

Output:
```text
24
```

Giải thích:
- Chia `(1) | (2 3 4)` -> `1 x 9 = 9`
- Chia `(1 2) | (3 4)` -> `3 x 7 = 21`
- Chia `(1 2 3) | (4)` -> `6 x 4 = 24` (lớn nhất)

---

## 🧠 Phân tích
Giả sử tổng cả dãy là `T`.

Nếu ta cắt sau vị trí `i` (với `1 <= i < N`):
- `S1` là tổng `i` phần tử đầu
- `S2 = T - S1`

Khi đó tích cần xét là:

`S1 x (T - S1)`

Vậy chỉ cần duyệt điểm cắt từ trái sang phải:
- cập nhật dần `S1` (prefix sum)
- tính `S2 = T - S1`
- cập nhật đáp án lớn nhất.

---

## 🔍 Thuật toán
1. Nhập `N` và dãy `A`.
2. Tính `T = sum(A)`.
3. Gán `S1 = 0`, `ans = 0`.
4. Duyệt `i` từ `0` đến `N - 2`:
   - `S1 += A[i]`
   - `S2 = T - S1`
   - `ans = max(ans, S1 * S2)`
5. In `ans`.

---

## 💻 Code Python
```python
N = int(input())
A = list(map(int, input().split()))

total = sum(A)
left_sum = 0
best = 0

for i in range(N - 1):
    left_sum += A[i]
    right_sum = total - left_sum
    best = max(best, left_sum * right_sum)

print(best)
```

---

## ⚡ Độ phức tạp
- Thời gian: `O(N)`
- Bộ nhớ: `O(1)` (không tính mảng đầu vào)

---

## 🎯 Chốt nhớ nhanh
Mỗi điểm cắt tạo ra một cặp `(S1, S2)`.
Duyệt mọi điểm cắt hợp lệ và lấy giá trị lớn nhất của `S1 x S2`.

---

[⬅ Quay lại mục lục](README.md)
