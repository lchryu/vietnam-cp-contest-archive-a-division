# Bài 1. Tặng bánh

[⬅ Quay lại mục lục](README.md)

## Đề bài
Lan có `N` (nghìn đồng) và muốn mua bánh tặng các em nhỏ.

Giá bán:
- Hộp lớn: `30` cái, giá `210` nghìn đồng
- Hộp nhỏ: `5` cái, giá `38` nghìn đồng
- Mua lẻ: `1` cái, giá `9` nghìn đồng

Yêu cầu: tính số cái bánh tối đa Lan có thể mua.

---

## Input
Một số tự nhiên `N` (nghìn đồng).

---

## Output
Một số tự nhiên: số cái bánh tối đa mua được.

---

## Phân tích
So sánh giá trên mỗi cái bánh:
- Hộp lớn: `210 / 30 = 7` (nghìn/cái)
- Hộp nhỏ: `38 / 5 = 7.6` (nghìn/cái)
- Mua lẻ: `9 / 1 = 9` (nghìn/cái)

Thứ tự hiệu quả: `hộp lớn > hộp nhỏ > mua lẻ`.

Vì vậy ta ưu tiên mua:
1. Hộp lớn trước
2. Rồi đến hộp nhỏ
3. Cuối cùng mua lẻ

---

## Brute force (đúng nhưng dễ TLE)
Code minh họa:

```python
N = int(input())
best = 0

for big in range(N // 210 + 1):
    for small in range(N // 38 + 1):
        for single in range(N // 9 + 1):
            cost = big * 210 + small * 38 + single * 9
            if cost <= N:
                best = max(best, big * 30 + small * 5 + single)

print(best)
```

Trace ngắn gọn (với `N = 257`):
- `for big in 0..1`
- `for small in 0..6`
- `for single in 0..28`

Ý nghĩa:
- Ta thử từng khả năng mua `(big, small, single)`.
- Mỗi khả năng đều được kiểm tra tổng tiền có vượt `N` hay không.
- Nếu hợp lệ thì tính số bánh và cập nhật đáp án lớn nhất.

Nhận xét:
- Cách này **luôn đúng** vì đã thử hết.
- Nhưng có 3 vòng lặp lớn, số trường hợp rất nhiều, dễ bị quá thời gian (TLE) khi `N` lớn.
- Vì thế bài này nên dùng greedy `O(1)` ở bên dưới.

---

## Ý tưởng (Greedy - lời giải chính)
Với số tiền `N`:
1. Mua tối đa hộp lớn:
   - `big = N // 210`
   - `N %= 210`
2. Mua tối đa hộp nhỏ:
   - `small = N // 38`
   - `N %= 38`
3. Mua lẻ:
   - `single = N // 9`

Tổng bánh:

`total = big * 30 + small * 5 + single`

Lưu ý:
- Đây là **greedy**, không phải brute force.
- Ta không thử hết mọi tổ hợp, mà chọn ngay phương án hiệu quả nhất ở từng bước.

Mã giả (greedy):

```text
Nhập N

big <- N // 210
N <- N % 210

small <- N // 38
N <- N % 38

single <- N // 9

total <- 30*big + 5*small + single
In total
```

---

## Thuật toán
1. Nhập `N`.
2. Tính `big`, cập nhật `N`.
3. Tính `small`, cập nhật `N`.
4. Tính `single`.
5. In `big * 30 + small * 5 + single`.

---

## Ví dụ
### Ví dụ 1
Input:

```text
210
```

Mua được `1` hộp lớn -> `30` cái.

Output:

```text
30
```

### Ví dụ 2
Input:

```text
257
```

- `1` hộp lớn (`210`) -> còn `47`
- `1` hộp nhỏ (`38`) -> còn `9`
- `1` cái lẻ (`9`)

Tổng: `30 + 5 + 1 = 36`.

Output:

```text
36
```

---

## Code Python
```python
N = int(input())

big = N // 210
N %= 210

small = N // 38
N %= 38

single = N // 9

print(big * 30 + small * 5 + single)
```

---

## Độ phức tạp
- Thời gian: `O(1)`
- Bộ nhớ: `O(1)`

---

## Kết luận
Chỉ cần áp dụng greedy theo thứ tự giá rẻ nhất mỗi cái bánh:
`hộp lớn -> hộp nhỏ -> mua lẻ`.

---

[⬅ Quay lại mục lục](README.md)
