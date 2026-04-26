# 🔢 BÀI 4: BIẾN ĐỔI SỐ CHIA HẾT CHO 9 (TỐI ƯU O(10))

## 📌 Đề bài

Cho một số nguyên dương rất lớn **N** (tối đa 100 chữ số).

👉 Bạn được phép:

* Chọn **một chữ số d (0 → 9)**
* Đổi **tất cả các chữ số d thành một chữ số x (0 → 9)**

---

## 🎯 Yêu cầu

Sau khi biến đổi, số mới phải:

* ❌ Không có số 0 ở đầu
* ✅ Chia hết cho **9**
* 🔥 Là **lớn nhất có thể**

---

## 🧠 Kiến thức cần nhớ

### 🔥 Quy tắc chia hết cho 9

```text
Tổng các chữ số chia hết cho 9
```

---

## 💡 Ý tưởng (bản tối ưu)

### 📌 Gọi:

* `S` = tổng chữ số ban đầu
* `cnt[d]` = số lần xuất hiện của chữ số d

---

### 🔥 Khi đổi d → x

```text
new_sum = S - d × cnt[d] + x × cnt[d]
```

---

### 🎯 Điều kiện chia hết 9

```text
new_sum % 9 == 0
```

---

### ⚡ Rút gọn (mod 9)

```text
(x - d) × cnt[d] ≡ -S (mod 9)
```

👉 Với mỗi `d`, chỉ có **một vài giá trị x hợp lệ**

---

## 🚀 Cách làm

* Duyệt `d` từ 0 → 9
* Với mỗi `d`, tìm `x` lớn nhất thỏa mãn điều kiện
* Thay toàn bộ d → x
* Lấy kết quả lớn nhất

---

## ✅ Code hoàn chỉnh (O(10))

```python
s = input().strip()

# tổng chữ số
S = sum(int(c) for c in s)

# đếm tần suất
cnt = [0]*10
for c in s:
    cnt[int(c)] += 1

best = "0"

for d in range(10):
    if cnt[d] == 0:
        continue

    c = cnt[d]

    # thử x từ lớn → nhỏ để lấy max nhanh
    for x in range(9, -1, -1):
        new_sum = S - d*c + x*c
        if new_sum % 9 != 0:
            continue

        # tạo số mới
        t = []
        for ch in s:
            if int(ch) == d:
                t.append(str(x))
            else:
                t.append(ch)

        t = "".join(t)

        # loại số có 0 đầu
        if t[0] == '0':
            continue

        # cập nhật max
        if len(t) > len(best) or (len(t) == len(best) and t > best):
            best = t

        break  # đã chọn x lớn nhất

print(best)
```

---

# 💀 CASE BẪY

## 🔥 Case 1: Leading zero

```text
Input:
100
```

👉 đổi 1 → 0:

```text
000 ❌
```

---

## 🔥 Case 2: Không cần đổi

```text
Input:
999
```

👉 đã chia hết 9
👉 kết quả vẫn là `999`

---

## 🔥 Case 3: Phải đổi để lớn hơn

```text
Input:
234
```

👉 đổi 2 → 8:

```text
834 ✔
```

---

## 🔥 Case 4: Toàn số giống nhau

```text
111111 → 999999
```

---

## 🔥 Case 5: Nhiều lựa chọn

👉 phải chọn  **x lớn nhất hợp lệ** , không phải bất kỳ

---

## 🧠 Ghi nhớ nhanh

```text
- Không brute force toàn bộ
- Dùng mod 9 để tìm x
- Duyệt x từ lớn → nhỏ
- Loại leading zero
```

---

## 🚀 Kết luận

* Đây là bài **tối ưu bằng toán học (mod)**
* Từ O(100) → O(10)

👉 Level cao hơn brute force

---

## 💥 Câu chốt

> “Thấy chia hết → nghĩ mod, không nghĩ brute”
>
