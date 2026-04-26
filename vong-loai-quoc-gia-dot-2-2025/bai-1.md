# 🧮 BÀI 1: ĐẾM NGÀY

## 📌 Đề bài

Cho hai số nguyên dương **A** và **B** (A ≤ B).

Hãy tính **tổng số ngày** từ năm A đến năm B (tính cả hai năm).

Quy ước:

* Năm thường có **365 ngày**
* Năm nhuận có **366 ngày**

---

## 🧠 Kiến thức cần nhớ

### 📅 Năm nhuận là gì?

Một năm được gọi là **năm nhuận** nếu:

* Chia hết cho 400
  **hoặc**
* Chia hết cho 4 nhưng **không chia hết cho 100**

👉 Công thức kiểm tra:

```python
(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
```

---

## 💡 Ý tưởng giải

### 🔥 Cách 1 (Brute Force – cơ bản)

* Duyệt từ năm A → B
* Nếu là năm nhuận → cộng 366
* Ngược lại → cộng 365

👉 Độ phức tạp: **O(B - A)**

#### 💻 Code Brute Force

```python
a = int(input())
b = int(input())

def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

total = 0

for y in range(a, b + 1):
    if is_leap(y):
        total += 366
    else:
        total += 365

print(total)
```

---

### ⚡ Cách 2 (Tối ưu – O(1))

👉 Ý tưởng:

* Tổng số năm = `B - A + 1`
* Tổng số ngày = `365 * số năm + số năm nhuận`

---

### 🔢 Cách đếm số năm nhuận

Số năm nhuận từ 1 → X:

```python
f(X) = X//4 - X//100 + X//400
```

👉 Số năm nhuận từ A → B:

```python
f(B) - f(A - 1)
```

---

## ✅ Code tối ưu (Cách 2)

```python
a = int(input())
b = int(input())

def count_leap(x):
    return x//4 - x//100 + x//400

leap = count_leap(b) - count_leap(a - 1)
n = b - a + 1

print(n * 365 + leap)
```

---

## 🔍 Ví dụ

### Input

```
2024
2028
```

### Output

```
1827
```

### Giải thích

* Có 5 năm: 2024 → 2028
* Năm nhuận: 2024, 2028 (2 năm)

👉 Tổng ngày:

```
5 × 365 + 2 = 1827
```

---

## ⚠️ Lưu ý

* Không nên dùng vòng lặp nếu khoảng [A, B] lớn
* Luôn ưu tiên công thức O(1) trong thi

---

## 🧠 Ghi nhớ nhanh

```
Tổng ngày = (B - A + 1) × 365 + số năm nhuận
```

---

## 🚀 Kết luận

* Đây là bài toán **đếm trong đoạn**
* Có thể giải bằng:
  * Brute force (dễ hiểu)
  * Công thức (tối ưu)

👉 Trong thi: **nên dùng công thức để tránh TLE**
