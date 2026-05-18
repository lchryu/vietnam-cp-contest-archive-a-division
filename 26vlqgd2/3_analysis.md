# Phan tich bai toan Quan hau

## 1. Tom tat de bai

Cho ban co kich thuoc `N x N`. Quan hau dang dung tai o `(x, y)`.

Can dem so o `(u, v)` ma quan hau co the di toi trong dung 1 nuoc, dong thoi tong `u + v` la so chan.

Quan hau co the di toi cac o:

- Cung hang voi `(x, y)`.
- Cung cot voi `(x, y)`.
- Cung duong cheo chinh.
- Cung duong cheo phu.

O dang dung `(x, y)` khong duoc tinh la mot nuoc di.

Rang buoc `N <= 10^8`, nen khong the duyet tung o. Can cong thuc `O(1)`.

---

## 2. Y tuong chinh

Dieu kien can kiem tra them la:

```python
(u + v) % 2 == 0
```

Tuc la `u` va `v` phai cung tinh chan le.

### Tren hang x

Neu di tren hang `x`, ta co:

```text
u = x
```

Tong can chan:

```text
u + v = x + v
```

De `x + v` chan, thi `v` phai cung tinh chan le voi `x`.

So cot `v` trong doan `[1, N]` cung tinh chan le voi `x` la:

- Neu `x` le: co `(N + 1) // 2` so le.
- Neu `x` chan: co `N // 2` so chan.

### Tren cot y

Neu di tren cot `y`, ta co:

```text
v = y
```

Tong can chan:

```text
u + v = u + y
```

De `u + y` chan, thi `u` phai cung tinh chan le voi `y`.

So hang `u` trong doan `[1, N]` cung tinh chan le voi `y` cung tinh tuong tu.

---

## 3. Ham dem so cung tinh chan le

Dung ham:

```python
def count_same_parity(a, n):
    if a % 2 == 1:
        return (n + 1) // 2
    return n // 2
```

Y nghia:

- Neu `a` le, ta dem so so le tu `1` den `n`.
- Neu `a` chan, ta dem so so chan tu `1` den `n`.

---

## 4. Xu ly hai truong hop cua x + y

### Truong hop 1: x + y chan

Khi `x + y` chan, o hien tai `(x, y)` cung thoa man dieu kien tong chan.

Viec nay quan trong vi:

- Khi dem tren hang, o `(x, y)` da nam trong danh sach.
- Khi dem tren cot, o `(x, y)` da nam trong danh sach.
- Khi dem tren duong cheo chinh, o `(x, y)` da nam trong danh sach.
- Khi dem tren duong cheo phu, o `(x, y)` da nam trong danh sach.

Nhung quan hau phai di sang o khac, nen moi duong phai tru di 1 o hien tai.

Cong thuc:

```python
ans = row_count - 1 + col_count - 1
```

Trong do:

```python
row_count = count_same_parity(x, n)
col_count = count_same_parity(y, n)
```

Sau do tinh them 2 duong cheo.

#### Duong cheo chinh

Duong cheo chinh co dang:

```text
u - v = x - y
```

So o tren duong cheo nay la:

```python
main_diag = n - abs(x - y)
```

Vi phai bo o hien tai:

```python
ans += main_diag - 1
```

#### Duong cheo phu

Duong cheo phu co dang:

```text
u + v = x + y
```

So o tren duong cheo phu phu thuoc vao vi tri cua tong `x + y`.

Neu duong cheo phu nam o nua tren/trai cua ban co:

```python
if x + y <= n + 1:
    anti_diag = x + y - 1
```

Nguoc lai:

```python
else:
    anti_diag = 2 * n - x - y + 1
```

Vi phai bo o hien tai:

```python
ans += anti_diag - 1
```

### Truong hop 2: x + y le

Khi `x + y` le, o hien tai `(x, y)` khong thoa man dieu kien tong chan.

Luc nay:

- Tren hang, cac o can dem co `v` cung chan le voi `x`.
- Vi `x + y` le nen `y` khac chan le voi `x`.
- Do do o hien tai `(x, y)` khong bi dem vao hang.

Tuong tu:

- Tren cot, cac o can dem co `u` cung chan le voi `y`.
- Vi `x + y` le nen `x` khac chan le voi `y`.
- Do do o hien tai `(x, y)` khong bi dem vao cot.

Hai duong cheo thi khong co o nao thoa man, vi moi o tren duong cheo co cung tinh chan le tong voi `(x, y)`, tuc la deu co tong le.

Vi vay cong thuc la:

```python
ans = row_count + col_count
```

Khong tru 1.

---

## 5. Loi giai Python

```python
import sys


def count_same_parity(a, n):
    if a % 2 == 1:
        return (n + 1) // 2
    return n // 2


data = list(map(int, sys.stdin.read().split()))
n, x, y = data[0], data[1], data[2]

ans = 0

row_count = count_same_parity(x, n)
col_count = count_same_parity(y, n)

if (x + y) % 2 == 0:
    ans += row_count - 1
    ans += col_count - 1

    main_diag = n - abs(x - y)
    ans += main_diag - 1

    if x + y <= n + 1:
        anti_diag = x + y - 1
    else:
        anti_diag = 2 * n - x - y + 1
    ans += anti_diag - 1
else:
    ans += row_count
    ans += col_count

print(ans)
```

---

## 6. Kiem tra vi du

### Vi du 1

Input:

```text
8
4
4
```

Ta co:

```text
x + y = 4 + 4 = 8
```

La so chan.

- Hang: cac cot chan la `2, 4, 6, 8`, bo cot `4`, con `3` o.
- Cot: cac hang chan la `2, 4, 6, 8`, bo hang `4`, con `3` o.
- Cheo chinh: co `8` o, bo o hien tai, con `7` o.
- Cheo phu: co `7` o, bo o hien tai, con `6` o.

Tong:

```text
3 + 3 + 7 + 6 = 19
```

### Vi du 2

Input:

```text
5
2
1
```

Ta co:

```text
x + y = 2 + 1 = 3
```

La so le.

- Hang `x = 2`: can cot chan, co `2, 4`, duoc `2` o.
- Cot `y = 1`: can hang le, co `1, 3, 5`, duoc `3` o.
- Hai duong cheo khong co o nao co tong chan.

Tong:

```text
2 + 3 = 5
```

---

## 7. Do phuc tap

Thuat toan chi dung vai phep tinh so hoc, khong duyet ban co.

```text
Do phuc tap thoi gian: O(1)
Bo nho: O(1)
```
