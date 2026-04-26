# 🃏 BÀI 5: RÚT THẺ

## 📌 Đề bài

Có các thẻ được đánh số từ  **1 → N** .

Mỗi lượt, An và Bình cùng rút thẻ theo quy luật:

### Lượt lẻ

* An rút **X thẻ lớn nhất**
* Bình rút **Y thẻ nhỏ nhất**

### Lượt chẵn

* An rút **X thẻ nhỏ nhất**
* Bình rút **Y thẻ lớn nhất**

Cho hai số **U** và  **V** .

👉 Yêu cầu: xác định:

* Thẻ U do ai rút?
* Ở lượt thứ mấy?
* Thẻ V do ai rút?
* Ở lượt thứ mấy?

---

## 🧠 Phân tích

Ban đầu còn đoạn thẻ:

```text
[1 ... N]
```

Ta dùng hai biến:

```text
left = 1
right = N
```

* `left`: thẻ nhỏ nhất còn lại
* `right`: thẻ lớn nhất còn lại

---

## 💡 Ý tưởng cơ bản

Mỗi lượt chỉ cần kiểm tra xem thẻ cần tìm có nằm trong đoạn bị rút không.

### Lượt lẻ

```text
An rút X thẻ lớn nhất:
[right - X + 1 ... right]

Bình rút Y thẻ nhỏ nhất:
[left ... left + Y - 1]
```

### Lượt chẵn

```text
An rút X thẻ nhỏ nhất:
[left ... left + X - 1]

Bình rút Y thẻ lớn nhất:
[right - Y + 1 ... right]
```

---

## ❌ Vì sao mô phỏng từng lượt bị TLE?

Nếu N rất lớn, ví dụ:

```text
N = 10^16
X = 1
Y = 1
```

Mỗi lượt chỉ rút 2 thẻ.

👉 Nếu dùng `while` từng lượt thì có thể chạy khoảng:

```text
10^16 / 2 lượt
```

=> chắc chắn TLE 💀

---

# 🔥 Insight tối ưu: Gom 2 lượt thành 1 block

Xét 2 lượt liên tiếp:

## Lượt lẻ

* Bên trái bị rút `Y`
* Bên phải bị rút `X`

## Lượt chẵn

* Bên trái bị rút `X`
* Bên phải bị rút `Y`

👉 Sau 2 lượt:

```text
Bên trái mất: X + Y thẻ
Bên phải mất: X + Y thẻ
```

---

## 🚀 Tính số block bỏ qua

Với thẻ `target`, ta tính:

```text
left_dist = target - 1
right_dist = N - target
```

Số block chắc chắn có thể bỏ qua:

```text
block = min(left_dist, right_dist) // (X + Y)
```

Sau đó cập nhật:

```text
left = 1 + block × (X + Y)
right = N - block × (X + Y)
turn = block × 2 + 1
```

👉 Lúc này chỉ cần mô phỏng vài lượt cuối.

---

## ✅ Code hoàn chỉnh AC

```python
def solve_one(n, x, y, target):
    left_dist = target - 1
    right_dist = n - target

    # Mỗi block gồm 2 lượt
    # Sau 2 lượt, mỗi bên mất x + y thẻ
    block = min(left_dist, right_dist) // (x + y)

    left = 1 + block * (x + y)
    right = n - block * (x + y)
    turn = block * 2 + 1

    while True:
        if turn % 2 == 1:
            # Lượt lẻ:
            # An rút x thẻ lớn nhất
            if target > right - x:
                return "A", turn
            right -= x

            # Bình rút y thẻ nhỏ nhất
            if target < left + y:
                return "B", turn
            left += y

        else:
            # Lượt chẵn:
            # An rút x thẻ nhỏ nhất
            if target < left + x:
                return "A", turn
            left += x

            # Bình rút y thẻ lớn nhất
            if target > right - y:
                return "B", turn
            right -= y

        turn += 1


n = int(input())
x = int(input())
y = int(input())
u = int(input())
v = int(input())

player_u, turn_u = solve_one(n, x, y, u)
player_v, turn_v = solve_one(n, x, y, v)

print(player_u)
print(turn_u)
print(player_v)
print(turn_v)
```

---

# 💀 CASE BẪY

## 🔥 Case 1: Logic đúng nhưng TLE

```text
N = 10^16
X = 1
Y = 1
U = 5×10^15
V = 5×10^15 + 1
```

👉 Mô phỏng từng lượt sẽ cực chậm.
👉 Phải dùng block.

---

## 🔥 Case 2: Nhầm lượt lẻ / lượt chẵn

```text
Lượt lẻ:
A lấy lớn
B lấy nhỏ

Lượt chẵn:
A lấy nhỏ
B lấy lớn
```

👉 Đảo nhầm là WA ngay.

---

## 🔥 Case 3: Nhầm đoạn bị lấy

Ví dụ lượt lẻ:

```text
A lấy X số lớn nhất:
[right - X + 1 ... right]
```

Điều kiện check:

```python
target > right - x
```

Không phải:

```python
target >= right - x
```

Vì `right - x` chưa bị lấy.

---

## 🔥 Case 4: X và Y không bằng nhau

```text
X = 2
Y = 5
```

👉 Không được nghĩ mỗi lượt hai bên mất bằng nhau.
👉 Chỉ sau **2 lượt** thì mỗi bên mới cùng mất `X + Y`.

---

## 🔥 Case 5: U và V xử lý độc lập

👉 Không được rút thẻ U rồi lấy trạng thái đó để xét V.

Sai:

```text
solve U xong cập nhật left/right
rồi dùng tiếp để solve V ❌
```

Đúng:

```text
solve_one(U)
solve_one(V)
```

---

## 🧠 Ghi nhớ nhanh

```text
Mỗi 2 lượt = 1 block
Mỗi bên mất X + Y thẻ

block = min(target - 1, N - target) // (X + Y)
```

---

## 🚀 Kết luận

Bài này có 2 tầng:

1. **Mô phỏng đoạn bị rút** để hiểu quy luật
2. **Gom block 2 lượt** để tránh TLE

👉 Đây là bài điển hình:

```text
Đúng logic chưa đủ, phải tối ưu đúng
```

---

## 💥 Câu chốt

> “N lớn thì đừng đi từng bước — hãy nhảy theo block.”
>
