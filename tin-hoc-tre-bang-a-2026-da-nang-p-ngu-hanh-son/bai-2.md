# Bài 2. Chia kẹo

[⬅ Quay lại mục lục](README.md)

## 📄 Đề bài
Cho `N` viên kẹo, mỗi viên có một màu biểu diễn bằng số nguyên dương `a_i`.

Hãy chia tất cả viên kẹo vào một số hộp sao cho trong mỗi hộp **không tồn tại hai viên có màu là hai số nguyên liên tiếp**, tức là:

`|x - y| != 1`

Hãy xác định số hộp ít nhất cần dùng.

---

## 🔢 Input
- Dòng 1: số nguyên `N`
- Dòng 2: `N` số nguyên `a_1, a_2, ..., a_N`

Ràng buộc:
- `1 <= N <= 2 * 10^5`
- `1 <= a_i <= 10^9`

---

## 📤 Output
In ra số hộp ít nhất cần dùng.

---

## 🧠 Phân tích
Trong cùng một hộp, chỉ cấm các cặp dạng `x` và `x+1`.
Lưu ý: hai viên cùng màu (ví dụ `2` và `2`) có hiệu `0` nên **không vi phạm**.

Sau khi sắp xếp mảng tăng dần:
- Nếu có số liên tiếp, chúng sẽ nằm cạnh nhau.
- Chỉ cần kiểm tra xem có tồn tại `a[i] == a[i-1] + 1` hay không.
- Nói cách khác, nếu dãy có cặp liên tiếp thì sau khi sort sẽ luôn lộ ra ở một cặp kề nhau.

Ví dụ ngay tại bước này:
- `1 3 5 7` -> không có cặp liên tiếp -> chỉ cần `1` hộp.
- `2 10 1 20` -> sort thành `1 2 10 20`.
  - Nếu cố nhét vào 1 hộp: trong hộp sẽ có cả `1` và `2`.
  - Vì `|1 - 2| = 1`, điều này vi phạm đề bài.
  - Vậy chắc chắn **không thể** dùng 1 hộp.
  - Chia thành 2 hộp thì hợp lệ, ví dụ:
    - Hộp A: `1, 10, 20`
    - Hộp B: `2`
  - Mỗi hộp đều không chứa cặp liên tiếp.
  - Kết luận: trường hợp này cần ít nhất `2` hộp, và `2` hộp là đủ.

Kết quả chỉ có thể là:
- `1` hộp: khi **không có** cặp liên tiếp nào.
- `2` hộp: khi **có ít nhất 1** cặp liên tiếp.

Vì sao 2 hộp luôn đủ?
- Chia theo tính chẵn/lẻ của **giá trị**:
  - Hộp 1: các số chẵn
  - Hộp 2: các số lẻ
- Trong cùng một hộp, hiệu giữa hai số luôn là số chẵn (`0, 2, 4, ...`), nên không thể bằng `1`.
- Do đó, luôn tồn tại cách chia hợp lệ bằng 2 hộp.

Ví dụ cho cách chia 2 hộp:
- Dãy `1 2 3 4 5 6`
- Hộp 1 (lẻ): `1, 3, 5`
- Hộp 2 (chẵn): `2, 4, 6`
- Mỗi hộp đều không có cặp liên tiếp.

---

## 💡 Ý tưởng
1. Sắp xếp mảng.
2. Duyệt từ trái sang phải:
   - nếu gặp `a[i] == a[i-1] + 1` thì in `2` và dừng ngay.
3. Nếu duyệt hết mà không gặp cặp liên tiếp nào, in `1`.

---

## 🔍 Thuật toán
1. Nhập `N` và mảng `a`.
2. `a.sort()`.
3. Với `i` từ `1` đến `N-1`:
   - nếu `a[i] == a[i-1] + 1`:
     - in `2`, kết thúc chương trình.
4. In `1`.

---

## 📌 Ví dụ tổng hợp
Ví dụ 1:
```text
Input
4
1 3 5 7
Output
1
```

Ví dụ 2:
```text
Input
4
2 10 1 20
Output
2
```

Ví dụ 3:
```text
Input
6
1 2 3 4 5 6
Output
2
```

---

## 💻 Code Python
```python
n = int(input())
a = list(map(int, input().split()))

a.sort()

for i in range(1, n):
    if a[i] == a[i - 1] + 1:
        print(2)
        break
else:
    print(1)
```

---

## ⏱ Độ phức tạp
- Sắp xếp: `O(N log N)`
- Duyệt kiểm tra: `O(N)`
- Tổng: `O(N log N)` (do bước sort chi phối)
- Bộ nhớ phụ: `O(1)` (không tính bộ nhớ lưu input)

---

## 🎯 Chốt nhanh
Chỉ cần kiểm tra có xuất hiện cặp liên tiếp `x, x+1` hay không:
- Có -> `2`
- Không -> `1`

---

[⬅ Quay lại mục lục](README.md)
