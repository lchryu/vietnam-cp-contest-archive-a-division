# Bài 2. Bảng cửu chương

[⬅ Quay lại mục lục](README.md)

## 📌 Đề bài
Bé Bi chỉ mới học thuộc bảng cửu chương (các phép nhân từ `1 x 1` đến `9 x 9`).

Cho trước một số tự nhiên `X`. Nếu `X` là kết quả của một phép nhân trong bảng cửu chương, hãy xác định xem `X` nằm ở bảng cửu chương nào.

- Nếu `X` thuộc nhiều bảng -> in ra bảng có số nhỏ nhất.
- Nếu không tồn tại -> in ra `0`.

---

## 📥 Input
Một số tự nhiên `X` (`1 <= X <= 100`).

---

## 📤 Output
In ra số thứ tự của bảng cửu chương nhỏ nhất chứa `X`, hoặc `0` nếu không tồn tại.

---

## 🧠 Phân tích
Ta cần tìm xem có tồn tại hai số `i, j` sao cho:

`i * j = X`, với `1 <= i, j <= 9`.

Trong đó:
- `i` là bảng cửu chương
- `j` là số nhân

Nếu có nhiều `i` thỏa mãn, phải chọn `i` nhỏ nhất.

---

## 💡 Ý tưởng
Duyệt `i` từ `1` đến `9`:
- Nếu `X % i == 0` thì `i` là ước của `X`.
- Gọi `j = X // i`.
- Nếu `1 <= j <= 9` thì tìm được phép nhân hợp lệ trong bảng cửu chương.

Vì duyệt `i` tăng dần, lần đầu thỏa mãn chính là đáp án nhỏ nhất.

---

## 🔍 Thuật toán
1. Nhập `X`.
2. Lặp `i` từ `1` đến `9`:
   - Nếu `X % i == 0`:
     - Tính `j = X // i`
     - Nếu `1 <= j <= 9`: in `i` và kết thúc.
3. Nếu duyệt hết không có kết quả, in `0`.

---

## 🧪 Ví dụ
### Ví dụ 1
Input:

```text
12
```

Phân tích:
- `1 x 12` (không hợp lệ vì `12 > 9`)
- `2 x 6` (hợp lệ)
- `3 x 4` (hợp lệ)

Chọn bảng nhỏ nhất: `2`.

Output:

```text
2
```

### Ví dụ 2
Input:

```text
14
```

`2 x 7` hợp lệ, nên kết quả là:

```text
2
```

### Ví dụ 3
Input:

```text
13
```

Không có cặp nào trong phạm vi `1..9`, nên:

```text
0
```

---

## 💻 Code Python
```python
x = int(input())

for i in range(1, 10):
    if x % i == 0:
        j = x // i
        if 1 <= j <= 9:
            print(i)
            break
else:
    print(0)
```

---

## 🧾 Giải thích code
- `for i in range(1, 10)`: duyệt tất cả bảng từ `1` đến `9`.
- `if x % i == 0`: kiểm tra `i` có chia hết `X` không.
- `j = x // i`: lấy thừa số còn lại.
- `if 1 <= j <= 9`: xác nhận phép nhân nằm trong bảng cửu chương.
- `print(i); break`: in bảng nhỏ nhất rồi dừng.
- `else: print(0)`: không tìm được bảng nào hợp lệ.

---

## ⚡ Độ phức tạp
- Thời gian: `O(1)` (tối đa 9 lần lặp).
- Bộ nhớ: `O(1)`.

---

## 🧾 Kết luận
Chỉ cần kiểm tra `X` có biểu diễn được thành tích của hai số trong đoạn `1..9` hay không, và lấy bảng nhỏ nhất thỏa mãn.

---

[⬅ Quay lại mục lục](README.md)
