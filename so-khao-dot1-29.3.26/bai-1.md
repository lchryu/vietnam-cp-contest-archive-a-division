# Bài 1. Diện tích hình chữ nhật

[⬅ Quay lại mục lục](README.md)

## 📌 Đề bài
Cho ba số tự nhiên `A, B, C`.

Hãy chọn hai trong ba số này để làm độ dài hai cạnh của một hình chữ nhật và đưa ra diện tích lớn nhất của hình chữ nhật có thể tạo được.

---

## 📥 Input
Gồm ba số tự nhiên `A, B, C` (`1 <= A, B, C <= 1000`), mỗi số trên một dòng.

---

## 📤 Output
In ra một số tự nhiên duy nhất là diện tích lớn nhất tìm được.

---

## 🧠 Phân tích
Ta cần chọn `2` trong `3` số để tạo hình chữ nhật.

Có đúng `3` khả năng:
- Chọn `A, B` -> diện tích `A * B`
- Chọn `A, C` -> diện tích `A * C`
- Chọn `B, C` -> diện tích `B * C`

Vì số trường hợp rất ít, chỉ cần xét hết rồi lấy lớn nhất.

---

## 💡 Ý tưởng
1. Tính diện tích của cả 3 cặp có thể tạo.
2. Lấy giá trị lớn nhất trong 3 diện tích đó.

---

## 🔍 Thuật toán
1. Nhập `A, B, C`.
2. Tính:
   - `S1 = A * B`
   - `S2 = A * C`
   - `S3 = B * C`
3. Tính `S = max(S1, S2, S3)`.
4. In `S`.

---

## 🧪 Ví dụ
Input:

```text
12
2
5
```

Tính toán:
- `12 * 2 = 24`
- `12 * 5 = 60`
- `2 * 5 = 10`

Giá trị lớn nhất là `60`.

Output:

```text
60
```

---

## 💻 Code Python
```python
a = int(input())
b = int(input())
c = int(input())

area1 = a * b
area2 = a * c
area3 = b * c

print(max(area1, area2, area3))
```

---

## 🧾 Giải thích code
- `area1`, `area2`, `area3` là diện tích của 3 cách chọn cạnh.
- `max(...)` trả về diện tích lớn nhất trong 3 giá trị.

---

## ⚡ Độ phức tạp
- Thời gian: `O(1)`
- Bộ nhớ: `O(1)`

---

## 🧾 Kết luận
Chỉ cần xét tất cả các cặp có thể và lấy giá trị lớn nhất là giải được bài toán.

---

[⬅ Quay lại mục lục](README.md)
