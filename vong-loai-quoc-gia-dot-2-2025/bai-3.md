# 🔢 BÀI 3: TẠO SỐ 2 CHỮ SỐ

## 📌 Đề bài

Cho 4 chữ số **A, B, C, D** (mỗi chữ số từ 0 → 9).

👉 Hãy đếm **bao nhiêu số có 2 chữ số** thỏa mãn:

* Chia hết cho **2**
* **Không có số 0 ở đầu**

---

## 🧠 Phân tích

Số dạng:

```text
XY
```

* X: hàng chục
* Y: hàng đơn vị

---

## ⚡ Điều kiện

* X ≠ 0
* Y là số chẵn
* X, Y lấy từ {A, B, C, D}

---

## ❗ Quan trọng

👉  **Đếm số KHÁC NHAU** , không phải số cách tạo

---

## 💡 Ý tưởng

* Duyệt tất cả cặp (x, y)
* Kiểm tra điều kiện
* Dùng `set` để loại trùng

---

## ✅ Code

```python
digits = [int(input()) for _ in range(4)]

s = set()

for x in digits:
    for y in digits:
        if x == 0:
            continue
        if y % 2 != 0:
            continue

        s.add(x * 10 + y)

print(len(s))
```

---

# 💀 CASE BẪY (CỰC QUAN TRỌNG)

## 🔥 Case 1: Tất cả giống nhau

```text
2
2
2
2
```

👉 Các cách tạo:

```text
22, 22, 22, ...
```

👉 ❗ Đáp án đúng: **1**

👉 Nếu không dùng `set` → sai ngay

---

## 🔥 Case 2: Có số 0

```text
0
0
2
2
```

👉 Các số hợp lệ:

```text
20, 22
```

👉 ❗ Không được có:

```text
02 ❌
```

---

## 🔥 Case 3: Không có số chẵn

```text
1
3
5
7
```

👉 Không tạo được số nào

👉 ❗ Output: **0**

---

## 🔥 Case 4: Có trùng nhưng không đủ để tạo lặp

```text
2
3
4
5
```

👉 ❗ Không được tạo:

```text
22 ❌ (chỉ có 1 số 2)
```

👉 Nhưng code sai sẽ vẫn đếm 22

---

## 🔥 Case 5: Tất cả đều chẵn

```text
2
4
6
8
```

👉 Có rất nhiều số:

```text
22, 24, 26, ...
```

👉 ❗ Phải loại trùng nếu input có lặp

---

## 🔥 Case 6: Chỉ có 0 và số lẻ

```text
0
1
3
5
```

👉 ❗ Không có số chẵn → output = 0

---

## 🧠 Ghi nhớ nhanh

```text
- X ≠ 0
- Y chẵn
- Dùng set để loại trùng
```

---

## 🚀 Kết luận

👉 Bài này không khó, nhưng:

> 💀 Sai vì hiểu sai “đếm số” vs “đếm cách”

👉 Chỉ cần nhớ:

* brute force
* * set

→ AC chắc chắn
