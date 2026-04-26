# Bài 4. Đồng hồ

[⬅ Quay lại mục lục](README.md)

## 📌 Đề bài
Một đồng hồ điện tử hiển thị thời gian dạng:

`AB:XY`

Trong đó:
- `AB`: giờ (`00` -> `23`)
- `XY`: phút (`00` -> `59`)

---

## 🎯 Yêu cầu
Cho hai thời điểm:
- thời điểm bắt đầu
- thời điểm kết thúc

Hãy đếm tổng số lần chữ số `'2'` xuất hiện trên màn hình đồng hồ từ thời điểm bắt đầu đến thời điểm kết thúc (kể cả hai đầu).

---

## 📥 Input
Gồm 4 dòng:
- Giờ bắt đầu
- Phút bắt đầu
- Giờ kết thúc
- Phút kết thúc

---

## 📤 Output
Một số nguyên: tổng số lần chữ số `'2'` xuất hiện.

---

## 🧠 Phân tích
Insight quan trọng:

Một ngày có `24 * 60 = 1440` thời điểm.

`1440` là rất nhỏ, nên có thể mô phỏng trực tiếp từng phút (brute force) mà vẫn nhanh.

---

## 🧩 Chuẩn hóa thời gian về phút
Đổi một thời điểm `h:m` thành số phút kể từ `00:00`:

`t = h * 60 + m`

Khi đó:
- `start = h1 * 60 + m1`
- `end = h2 * 60 + m2`

---

## 🔄 Trường hợp qua ngày
- Nếu `start <= end`: duyệt bình thường từ `start` đến `end`.
- Nếu `start > end`: nghĩa là thời gian kết thúc nằm ở ngày hôm sau.

Để xử lý thống nhất cả hai trường hợp, dùng:

`cur = (cur + 1) % 1440`

Ý nghĩa:
- Sau `23:59` (phút `1439`), tăng thêm 1 phút sẽ quay về `00:00` (phút `0`).
- Không bị xuất hiện giờ sai như `24:00`.

---

## 💡 Ý tưởng
1. Chuyển 2 thời điểm về số phút (`start`, `end`).
2. Duyệt từng phút từ `start` đến `end` (kể cả hai đầu).
3. Mỗi phút:
   - Tách lại thành giờ/phút.
   - Đếm số ký tự `'2'` trong dạng `HH` và `MM`.
4. Cộng dồn kết quả.

---

## 🔍 Thuật toán
1. Nhập `h1, m1, h2, m2`.
2. Tính:
   - `start = h1 * 60 + m1`
   - `end = h2 * 60 + m2`
3. Gán `total = 0`, `cur = start`.
4. Lặp vô hạn:
   - `h = cur // 60`
   - `m = cur % 60`
   - `total += count_2(h, m)`
   - Nếu `cur == end` thì dừng.
   - Ngược lại: `cur = (cur + 1) % 1440`
5. In `total`.

---

## 🧪 Ví dụ
Input:

```text
2
20
2
22
```

Các thời điểm được duyệt:
- `02:20` -> `"0220"` -> có `2` số `2`
- `02:21` -> `"0221"` -> có `2` số `2`
- `02:22` -> `"0222"` -> có `3` số `2`

Tổng:

`2 + 2 + 3 = 7`

---

## 💻 Code Python
```python
def count_2(h, m):
    return str(h).zfill(2).count('2') + str(m).zfill(2).count('2')
    # hoặc đơn giản hơn
    # return (str(h) + str(m)).count('2)
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

start = h1 * 60 + m1
end = h2 * 60 + m2

total = 0
cur = start

while True:
    h = cur // 60
    m = cur % 60

    total += count_2(h, m)

    if cur == end:
        break

    cur = (cur + 1) % 1440

print(total)
```

> Ghi chú:
> - Với bài này (đếm chữ số `'2'`), có thể viết gọn:
>   `def cnt2(h, m): return (str(h) + str(m)).count('2')`
> - Tuy nhiên nếu đổi sang đếm chữ số `'0'` thì cần giữ dạng 2 chữ số
>   cho giờ/phút (dùng `zfill(2)`), để không bị sai ở các mốc như `02:00`.

---

## 🧾 Giải thích code
### 1) Hàm đếm số `2`
`str(h).zfill(2)`:
- Chuyển số sang chuỗi.
- Đảm bảo luôn 2 chữ số (ví dụ `2` -> `"02"`).

Làm tương tự với phút, rồi dùng `.count('2')` để đếm số ký tự `'2'`.

### 2) Vòng lặp mô phỏng thời gian
`while True`:
- Mỗi vòng ứng với 1 phút.
- Tính giờ/phút từ `cur` bằng chia và chia dư.

### 3) Quay vòng ngày
`cur = (cur + 1) % 1440`:
- Là chìa khóa xử lý case qua nửa đêm (`23:59` -> `00:00`).

### 4) Điều kiện dừng
`if cur == end: break`
- Bảo đảm đếm đủ từ đầu đến cuối, bao gồm cả thời điểm kết thúc.

---

## ⚡ Độ phức tạp
- Tối đa 1440 bước lặp.
- Thời gian: `O(1440)` (coi như hằng số, rất nhanh).
- Bộ nhớ: `O(1)`.

---

## 🧾 Kết luận
Bài này không cần công thức phức tạp.
Mô phỏng đúng theo phút + đếm ký tự là đủ chính xác và dễ kiểm soát lỗi.

---

## 😏 Insight để nhớ
- `"Time simulation <= 1440 -> brute force là chuẩn"`
- `"Đừng cố nhồi công thức ở bài mô phỏng thời gian"`

---

[⬅ Quay lại mục lục](README.md)
