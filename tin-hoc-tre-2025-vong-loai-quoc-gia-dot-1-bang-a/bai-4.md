# Bài 4. TỔNG DÃY SỐ

[⬅ Quay lại mục lục](README.md)

## Đề bài

Cho dãy số có quy luật sau:
1, 2, 3, 6, 5, 4, 7, 8, 9, 12, 11, 10, 13, 14, 15, 18, 17, 16, ...

**Yêu cầu:** Cho hai số nguyên dương $l, r$. Hãy tính tổng các số từ vị trí $l$ đến vị trí $r$ của dãy số trên.

---

## Input

- Gồm hai số tự nhiên $l$ và $r$ ($1 \le l \le r \le 10^8$)
- Mỗi số trên một dòng.

---

## Output

- Gồm một số tự nhiên là kết quả của bài toán.

---

## Phân tích

Quan sát dãy số, ta thấy dãy được chia thành từng nhóm 3 số:

- Nhóm 1: $1, 2, 3$ (vị trí 1, 2, 3) - Tăng dần.
- Nhóm 2: $6, 5, 4$ (vị trí 4, 5, 6) - Giảm dần.
- Nhóm 3: $7, 8, 9$ (vị trí 7, 8, 9) - Tăng dần.
- Nhóm 4: $12, 11, 10$ (vị trí 10, 11, 12) - Giảm dần.

**Quy luật chung:**

- Nhóm thứ $k$ (1-indexed) chứa các giá trị từ $3k-2$ đến $3k$.
- Nếu $k$ là số lẻ: Các số viết theo thứ tự tăng dần: $3k-2, 3k-1, 3k$.
- Nếu $k$ là số chẵn: Các số viết theo thứ tự giảm dần: $3k, 3k-1, 3k-2$.

---

## Ý tưởng

Để tính tổng từ vị trí $l$ đến $r$, ta sử dụng công thức:

$$
\text{Result} = S(r) - S(l-1)
$$

Trong đó $S(n)$ là tổng của $n$ số đầu tiên trong dãy.

---

## Thuật toán

Để tính $S(n)$:

1. Xác định số nhóm đầy đủ: $k = \lfloor n/3 \rfloor$.
2. Tổng của $k$ nhóm đầy đủ:
   Mỗi nhóm $i$ (bất kể tăng hay giảm) đều chứa bộ 3 số $\{3i-2, 3i-1, 3i\}$.
   Tổng nhóm $i$ là: $(3i-2) + (3i-1) + 3i = 9i - 3$.
   Tổng $k$ nhóm: $\sum_{i=1}^k (9i-3) = 9 \cdot \frac{k(k+1)}{2} - 3k = \frac{9k^2 + 3k}{2}$.
3. Xét các số dư $m = n \pmod 3$:
   Các số này thuộc nhóm thứ $k+1$.
   - Nếu $k+1$ lẻ: Các số là $3k+1, 3k+2, \dots$ (lấy $m$ số đầu).
   - Nếu $k+1$ chẵn: Các số là $3k+3, 3k+2, \dots$ (lấy $m$ số đầu).
4. Cộng dồn phần dư vào tổng.

---

## Code Python

```python📘 TỔNG DÃY SỐ  Cho dãy số có quy luật sau: 1, 2, 3, 6, 5, 4, 7, 8, 9, 12, 11, 10, 13, 14, 15, 18, 17, 16, ...  📌 Yêu cầu  Cho hai số nguyên dương l, r. Hãy tính tổng các số từ vị trí l đến vị trí r của dãy số trên.  📥 Dữ liệu nhập vào từ bàn phím Gồm hai số tự nhiên l và r (1 ≤ l ≤ r ≤ 10⁸) Mỗi số trên một dòng 📤 Kết quả ghi ra màn hình Gồm một số tự nhiên là kết quả của bài toán 📊 Ví dụ Dữ liệu	Kết quả	Giải thích 3	33	Tổng các số từ vị trí 3 đến vị trí 8 là: 8		3 + 6 + 5 + 4 + 7 + 8 = 33 ⚠️ Ràng buộc Có 50% số test ứng với 50% số điểm: r ≤ 10⁵ 50% số test còn lại ứng với 50% số điểm không có ràng buộc gì thêm
def sum_n(n: int) -> int:
    if n <= 0:
        return 0
    k = n // 3
    m = n % 3
  
    # Tổng của k nhóm đầy đủ
    total = (9 * k * k + 3 * k) // 2
  
    # Xét nhóm thứ k + 1
    next_group_idx = k + 1
    start_val = 3 * k + 1
  
    if m > 0:
        if next_group_idx % 2 == 1:
            # Nhóm lẻ: tăng dần 3k+1, 3k+2, 3k+3
            for i in range(m):
                total += (start_val + i)
        else:
            # Nhóm chẵn: giảm dần 3k+3, 3k+2, 3k+1
            current_val = 3 * k + 3
            for i in range(m):
                total += (current_val - i)
              
    return total

import sys
input_data = sys.stdin.read().split()
if len(input_data) >= 2:
    l = int(input_data[0])
    r = int(input_data[1])
    print(sum_n(r) - sum_n(l - 1))
```

---

## Độ phức tạp

- Thời gian: $O(1)$ (vì các phép tính là hằng số, vòng lặp $m$ tối đa 2 lần).
- Bộ nhớ: $O(1)$.

---

[⬅ Quay lại mục lục](README.md)
