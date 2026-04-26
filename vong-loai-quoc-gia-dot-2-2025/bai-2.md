# 🍬 BÀI 2: KẸO

## 📌 Đề bài

An có **A** viên kẹo.
Bình có **B** viên kẹo.

* Bố cho An thêm **20** viên
* Mẹ cho Bình thêm **25** viên

👉 Hãy tính **độ chênh lệch số viên kẹo** giữa An và Bình sau khi được cho thêm.

---

## 🧠 Phân tích

Sau khi nhận thêm:

* An có:

```text
A + 20
```

* Bình có:

```text
B + 25
```

---

## 🎯 Mục tiêu

👉 Tính:

```text
| (A + 20) - (B + 25) |
```

---

## ⚡ Rút gọn

```text
(A + 20) - (B + 25)
= A - B - 5
```

👉 Công thức cuối cùng:

```text
|A - B - 5|
```

---

## 💡 Ý tưởng

* Không cần tính riêng từng người
* Chỉ cần áp dụng công thức rút gọn
* Dùng **giá trị tuyệt đối** (`abs`)

---

## ✅ Code hoàn chỉnh

```python
a = int(input())
b = int(input())

print(abs(a - b - 5))
```

---

## 🔍 Ví dụ

### Input

```
10
2
```

### Output

```
3
```

### Giải thích

* An: 10 + 20 = 30
* Bình: 2 + 25 = 27

👉 Độ chênh lệch:

```text
|30 - 27| = 3
```

---

## ⚠️ Lưu ý

* Luôn dùng `abs()` để tránh âm
* Không cần if so sánh lớn nhỏ

---

## 🧠 Ghi nhớ nhanh

```text
Độ chênh lệch = |A - B - 5|
```

---

## 🚀 Kết luận

* Bài này là **biến đổi biểu thức**
* Không cần vòng lặp
* Không cần điều kiện

👉 Thuộc dạng **toán cơ bản + code cực ngắn**
