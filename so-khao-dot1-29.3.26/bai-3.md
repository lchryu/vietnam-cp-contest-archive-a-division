# Bài 3. Tô màu sân trường

[⬅ Quay lại mục lục](README.md)

## 📌 Đề bài
Cho bảng `N x N`.

- Đường chéo chính được tô màu đỏ.
- Các đường chéo song song với đường chéo chính được tô theo chu kỳ:
  `đỏ -> xanh -> vàng -> đỏ -> ...`

Yêu cầu: đếm số ô màu đỏ.

---

## I. Phân tích đề
### 1) Đặc trưng đường chéo
Các ô cùng một đường chéo song song với đường chéo chính thỏa:

`i - j = const`

Do đối xứng, xét:

`d = abs(i - j)`

### 2) Quy luật màu
Chu kỳ màu có độ dài `K = 3`, nên màu phụ thuộc vào:

`d mod 3`

### 3) Điều kiện để là màu đỏ
Ô màu đỏ khi:

`d mod 3 = 0`

---

## II. Lời giải ngây thơ (Brute Force)
### Ý tưởng
Duyệt toàn bộ các ô `(i, j)` và kiểm tra:

`abs(i - j) % 3 == 0`

### Code
```python
n = int(input())

ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if abs(i - j) % 3 == 0:
            ans += 1

print(ans)
```

### Độ phức tạp
`O(N^2)`

---

## III. Tối ưu về O(N)
### 1) Ý tưởng
Không duyệt từng ô nữa, mà duyệt theo từng lớp đường chéo:

`d = 0, 3, 6, 9, ...`

### 2) Giới hạn của `d`
`d_max = N - 1`

### 3) Số ô trong mỗi lớp
- `d = 0`: có `N` ô
- `d > 0`: có `2 * (N - d)` ô

### 4) Code
```python
n = int(input())

ans = 0
for d in range(0, n, 3):
    if d == 0:
        ans += n
    else:
        ans += 2 * (n - d)

print(ans)
```

### Độ phức tạp
`O(N / 3)` (thực tế là tuyến tính theo số lớp, thường viết gọn là `O(N)`).

---

## IV. Tối ưu về O(1)
### 1) Đặt biến
Viết:

`d = 3i`, với `i = 0, 1, 2, ..., t`

Trong đó:

`t = floor((N - 1) / 3)`

### 2) Tổng cần tính
`ans = N + sum(2 * (N - 3i), i = 1..t)`

### 3) Biến đổi
`ans = N + 2 * sum(N - 3i, i = 1..t)`

`= N + 2 * (N * t - 3 * t * (t + 1) / 2)`

### 4) Công thức rút gọn
`ans = N + 2 * N * t - 3 * t * (t + 1)`

### 5) Code
```python
n = int(input())

t = (n - 1) // 3
ans = n + 2 * n * t - 3 * t * (t + 1)

print(ans)
```

---

## V. Chứng minh tính đúng
### 1) Bao phủ đầy đủ
Các lớp được xét là:

`d = 0, 3, 6, ..., 3t`

đều thỏa `d mod 3 = 0`, tức đúng các lớp màu đỏ.

### 2) Không trùng lặp
Mỗi giá trị `d` ứng với đúng một lớp đường chéo, nên không bị đếm trùng.

### 3) Không thiếu
`t = floor((N - 1) / 3)` là giá trị lớn nhất để `3t <= N - 1`, nên không bỏ sót lớp đỏ hợp lệ nào.

### 4) Tổng chính xác
- Lớp `d = 0` đóng góp `N`.
- Mỗi lớp `d > 0` đóng góp `2 * (N - d)`.

Nên công thức tổng là chính xác.

---

## VI. Tóm tắt tư duy
- Mỗi ô thuộc một lớp `d = abs(i - j)`.
- Màu đỏ khi và chỉ khi `d mod 3 = 0`.
- Duyệt theo lớp thay vì duyệt theo ô.
- Tối ưu dần: `O(N^2) -> O(N) -> O(1)`.

---

## VII. Câu chốt
Bài toán hình học được quy về bài toán số học theo khoảng cách đường chéo:

`d = abs(i - j)`.

---

[⬅ Quay lại mục lục](README.md)
