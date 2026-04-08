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

## 🧪 Test mẫu
Input:
```text
12
```

Output:
```text
2
```

Giải thích:
- `12` có thể viết thành `2 × 6` và `3 × 4`.
- Chọn bảng cửu chương nhỏ nhất nên in `2`.

---

## 🧠 Bản chất bài toán
Thực chất bài này hỏi:

> Có tồn tại `i, j ∈ [1..9]` sao cho `i × j = X` không?

Nếu có:
- `i` chính là "bảng cửu chương"
- cần lấy `i` nhỏ nhất

Nói cách khác, ta kiểm tra `X` có thuộc tập:

`{i × j | 1 ≤ i, j ≤ 9}`

---

## ⚠️ Nhận xét nhanh
- Giá trị lớn nhất trong bảng cửu chương là `9 × 9 = 81`.
  - Nếu `X > 81` thì chắc chắn kết quả là `0`.
- `X = 1` thì luôn thuộc bảng `1`.

---

## 💡 Ý tưởng tối ưu
Ta chỉ cần kiểm tra các ước của `X`.

Logic:
- Duyệt `i` từ `1` đến `9`.
- Nếu `i` là ước của `X` (`X % i == 0`):
  - `j = X // i`
  - nếu `1 <= j <= 9` thì hợp lệ.

Vì duyệt `i` từ nhỏ đến lớn, nghiệm đầu tiên chính là đáp án.

---

## 🔍 Thuật toán
1. Nhập `X`.
2. Lặp `i` từ `1` đến `9`:
   - Nếu `X % i == 0`:
     - Tính `j = X // i`
     - Nếu `1 <= j <= 9`: in `i` và kết thúc.
3. Nếu duyệt hết không có kết quả, in `0`.

---

## 💻 Code Python (tối ưu)
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

## 🧪 Ví dụ
### Ví dụ 1
Input:
```text
12
```

| i | j = X / i | i × j hợp lệ trong [1..9]? |
|---|-----------|----------------------------|
| 1 | 12        | ❌ |
| 2 | 6         | ✅ |
| 3 | 4         | ✅ |

Chọn `i` nhỏ nhất -> `2`.

Output:
```text
2
```

### Ví dụ 2
Input:
```text
14
```

Có `2 × 7` hợp lệ nên kết quả là:
```text
2
```

### Ví dụ 3
Input:
```text
13
```

Không có cặp nào hợp lệ trong `1..9`, nên:
```text
0
```

---

## 🐢 Brute force (tham khảo)
Hai cách dưới đây đều duyệt toàn bộ cặp `(i, j)` với `1 <= i, j <= 9`,
nên vẫn AC vì dữ liệu rất nhỏ (tối đa `81` phép kiểm tra).

### Cách 1: Dùng cờ `found` + `break`
Ý tưởng:
- Duyệt `i` từ nhỏ đến lớn.
- Nếu tìm được `i * j == X` thì in luôn `i` và dừng.
- Vì `i` tăng dần, đáp án đầu tiên tìm được là nhỏ nhất.

```python
x = int(input())
found = False

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == x:
            print(i)
            found = True
            break
    if found:
        break

if not found:
    print(0)
```

### Cách 2: Dùng biến `ans` (không dừng sớm)
Ý tưởng:
- Duyệt hết các cặp `(i, j)`.
- Nếu `i * j == X` thì cập nhật `ans = min(ans, i)`.
- Cuối cùng nếu `ans` không đổi thì in `0`, ngược lại in `ans`.

```python
x = int(input())

ans = 10  # lớn hơn mọi bảng hợp lệ (1..9)

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == x:
            ans = min(ans, i)

if ans == 10:
    print(0)
else:
    print(ans)
```

> Cả hai cách đều đúng và có thể AC.
> Tuy nhiên vẫn khuyến khích dùng cách tối ưu ở phần trên (duyệt theo ước),
> vì ngắn hơn và hiệu quả hơn.
>
> So sánh nhanh độ phức tạp:
> - Brute force 2 vòng: `O(9 * 9) = O(81)` (vẫn AC do hằng số nhỏ)
> - Duyệt theo ước: `O(9)` (gọn và tốt hơn)

---

## 🧠 Nhận diện dạng bài
Khi thấy:
- giới hạn rất nhỏ (`1..9`)
- yêu cầu tìm cặp nhân `i, j`

Nghĩ ngay đến:
- duyệt ước (tối ưu)
- hoặc brute force (để kiểm tra nhanh)

---

## ⚡ Độ phức tạp
- Thời gian: `O(1)` (tối đa 9 lần lặp).
- Bộ nhớ: `O(1)`.

---

## 🧾 Kết luận
Chỉ cần kiểm tra `X` có biểu diễn được thành tích của hai số trong đoạn `1..9` hay không, và lấy bảng nhỏ nhất thỏa mãn.

---

[⬅ Quay lại mục lục](README.md)
