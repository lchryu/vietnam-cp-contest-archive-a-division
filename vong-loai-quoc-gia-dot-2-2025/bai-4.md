# 🔢 BÀI 4: BIẾN ĐỔI SỐ CHIA HẾT CHO 9

## 📌 Đề bài

Cho một số nguyên dương rất lớn **N** (có thể dài tới 100 chữ số).

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

## 💡 Ý tưởng

👉 Thử tất cả:

```text
d từ 0 → 9
x từ 0 → 9
```

* Thay toàn bộ d → x
* Kiểm tra điều kiện
* Lấy số lớn nhất

---

## ❗ Vì sao dùng string?

* N có thể rất lớn (100 chữ số)
* ❌ Không dùng int
* ✅ Dùng string

---

## ✅ Code hoàn chỉnh

```python
s = input().strip()

best = "0"

for d in "0123456789":
    for x in "0123456789":
        t = ""

        for c in s:
            if c == d:
                t += x
            else:
                t += c

        # không có số 0 ở đầu
        if t[0] == '0':
            continue

        # kiểm tra chia hết cho 9
        if sum(int(c) for c in t) % 9 != 0:
            continue

        # lấy max
        if len(t) > len(best) or (len(t) == len(best) and t > best):
            best = t

print(best)
```

---

# 💀 CASE BẪY

## 🔥 Case 1: Leading zero

```text
Input:
100
```

👉 Nếu đổi `1 → 0`:

```text
000 ❌ (không hợp lệ)
```

👉 ❗ Phải loại

---

## 🔥 Case 2: Không đổi gì là tốt nhất

```text
Input:
999
```

👉 Đã chia hết cho 9
👉 Không cần đổi

👉 ❗ Đáp án: `999`

---

## 🔥 Case 3: Phải đổi để chia hết 9

```text
Input:
234
```

👉 Tổng = 9 → ok
👉 Nhưng có thể đổi để lớn hơn:

```text
234 → 834 ✔
```

---

## 🔥 Case 4: Có nhiều cách đổi

👉 Phải chọn số  **lớn nhất** , không phải bất kỳ

---

## 🔥 Case 5: Toàn số giống nhau

```text
111111
```

👉 Nếu đổi:

```text
1 → 9 → 999999 ✔
```

---

## 🔥 Case 6: Không có cách nào hợp lệ

👉 Thực tế: luôn có cách (ít nhất giữ nguyên nếu đã chia hết 9)

---

## 🧠 Ghi nhớ nhanh

```text
- Thử mọi d → x
- Replace toàn bộ
- Check chia hết 9
- Loại leading zero
- Lấy max
```

---

## 🚀 Kết luận

* Đây là bài **brute force thông minh**
* Không cần tối ưu phức tạp
* Số trường hợp: 10 × 10 = 100 (rất nhỏ)

👉 Quan trọng:

* xử lý string
* tránh leading zero
* chọn max đúng cách
