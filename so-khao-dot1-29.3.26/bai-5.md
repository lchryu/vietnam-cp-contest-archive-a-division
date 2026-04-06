# Bài 5. Chia nhóm

[⬅ Quay lại mục lục](README.md)

## 📌 Đề bài
Cho số nguyên dương `N`. Xét các số từ `1` đến `N`.

Chia các số này thành 3 nhóm:
- Nhóm 1: các số chia hết cho `2` (tăng dần)
- Nhóm 2: các số chia hết cho `3` nhưng chưa xuất hiện ở nhóm 1 (tăng dần)
- Nhóm 3: các số còn lại (tăng dần)

Sau đó ghép 3 nhóm theo thứ tự:
`nhóm 1 -> nhóm 2 -> nhóm 3`.

---

## 🎯 Yêu cầu
Cho `K`, hãy tính tổng của `K` phần tử đầu tiên của dãy sau khi ghép.

---

## 📥 Input
Một dòng gồm hai số:

`N, K` với `1 <= K <= N <= 10^5`.

---

## 📤 Output
Một số nguyên: tổng `K` phần tử đầu tiên.

---

## 🧠 Phân tích
Insight quan trọng của bài:
- Chia nhóm đúng thứ tự ưu tiên.
- Không để số bị trùng nhóm.

Ba nhóm thực chất là:
- Nhóm 1: `i % 2 == 0`
- Nhóm 2: `i % 3 == 0` và `i % 2 != 0`
- Nhóm 3: `i % 2 != 0` và `i % 3 != 0`

Lưu ý:
- Số chia hết cho `6` thuộc nhóm 1, nên không được vào nhóm 2.
- Dùng `if ... elif ... else` là cách gọn và tránh trùng tốt nhất.

---

## 💡 Ý tưởng
Duyệt `i` từ `1` đến `N`:
- nếu chia hết cho `2` -> đưa vào `group1`
- ngược lại nếu chia hết cho `3` -> đưa vào `group2`
- còn lại -> đưa vào `group3`

Nối mảng:

`arr = group1 + group2 + group3`

Kết quả cần in:

`sum(arr[:k])`

---

## 🔍 Thuật toán
1. Nhập `N, K`.
2. Tạo 3 mảng rỗng: `group1`, `group2`, `group3`.
3. Duyệt `i` từ `1` đến `N`:
   - nếu `i % 2 == 0`: thêm vào `group1`
   - `elif i % 3 == 0`: thêm vào `group2`
   - `else`: thêm vào `group3`
4. Ghép 3 mảng theo thứ tự.
5. Lấy `K` phần tử đầu, tính tổng và in ra.

---

## 🧪 Ví dụ
Input:

```text
10 5
```

Chia nhóm:
- Nhóm 1: `2, 4, 6, 8, 10`
- Nhóm 2: `3, 9`
- Nhóm 3: `1, 5, 7`

Dãy sau khi ghép:

`2 4 6 8 10 3 9 1 5 7`

`5` phần tử đầu:

`2 + 4 + 6 + 8 + 10 = 30`

Output:

```text
30
```

---

## 💻 Code Python (khuyên dùng)
```python
n, k = map(int, input().split())

group1 = []
group2 = []
group3 = []

for i in range(1, n + 1):
    if i % 2 == 0:
        group1.append(i)
    elif i % 3 == 0:
        group2.append(i)
    else:
        group3.append(i)

arr = group1 + group2 + group3
print(sum(arr[:k]))
```

---

## 🧾 Giải thích code
- `if i % 2 == 0`: ưu tiên nhóm 1.
- `elif i % 3 == 0`: chỉ chạy khi chưa vào nhóm 1, nên tự động tránh trùng.
- `else`: nhóm 3.
- `arr[:k]`: lấy `K` phần tử đầu tiên của dãy đã ghép.

---

## ⚡ Độ phức tạp
- Thời gian: `O(N)`
- Bộ nhớ: `O(N)`

Với `N <= 10^5`, cách này rất ổn và dễ kiểm soát lỗi.

---

## 🚀 Bản tham khảo tối ưu bộ nhớ (không dùng mảng)
```python
n, k = map(int, input().split())

total = 0
count = 0

# Nhóm 1
for i in range(2, n + 1, 2):
    total += i
    count += 1
    if count == k:
        print(total)
        raise SystemExit

# Nhóm 2
for i in range(3, n + 1, 3):
    if i % 2 != 0:
        total += i
        count += 1
        if count == k:
            print(total)
            raise SystemExit

# Nhóm 3
for i in range(1, n + 1):
    if i % 2 != 0 and i % 3 != 0:
        total += i
        count += 1
        if count == k:
            print(total)
            raise SystemExit
```

Ghi chú:
- Bản này giảm bộ nhớ xuống gần `O(1)`.
- Nhưng code dài hơn, khó debug hơn.
- Với giới hạn đề hiện tại, bản dùng mảng là lựa chọn tốt hơn để nộp.

---

## 🧾 Kết luận
Điểm mấu chốt của bài là:
- chia nhóm đúng thứ tự
- không trùng phần tử giữa các nhóm
- lấy đúng `K` phần tử đầu sau khi ghép

---

## 😏 Insight để nhớ
- `"elif là linh hồn bài này"`
- `"chia nhóm = filter + order"`

---

[⬅ Quay lại mục lục](README.md)
