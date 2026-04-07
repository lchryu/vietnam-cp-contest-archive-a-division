# Bài 3. Chuỗi lặp đều

[⬅ Quay lại mục lục](README.md)

## 📌 Đề bài
Một chuỗi được gọi là chuỗi lặp đều `k` lần nếu nó được tạo thành bằng cách lặp lại `k` lần một chuỗi con nào đó.

Ví dụ:
- `xyzxyz` là chuỗi lặp đều 2 lần (chuỗi con là `xyz`)
- `cdcdcdcd` vừa là chuỗi lặp đều 4 lần, vừa là chuỗi lặp đều 2 lần
- `hello` là chuỗi lặp đều 1 lần

Cho số nguyên dương `k` và chuỗi `S`.  
Hãy sắp xếp lại các ký tự trong `S` để thu được một chuỗi lặp đều đúng `k` lần.

- Nếu làm được, in ra một chuỗi thỏa mãn.
- Nếu không thể, in ra `-1`.

---

## 📥 Input
- Dòng 1: số nguyên `k`
- Dòng 2: chuỗi `S` gồm các chữ cái thường `a..z`

---

## 📤 Output
- In ra một chuỗi lặp đều đúng `k` lần tạo được từ `S`
- Nếu không thể, in ra `-1`
- Nếu có nhiều đáp án, in ra một đáp án bất kỳ

---

## 🧪 Test mẫu
### Test mẫu 1
Input:
```text
2
aabbcc
```

Output:
```text
abcabc
```

Giải thích:
- Kết quả `abcabc` có thể tách thành `abc` và `abc`, tức là một chuỗi con được lặp đúng `2` lần.
- Chuỗi này dùng lại đúng các ký tự của `S` sau khi sắp xếp lại.

### Test mẫu 2
Input:
```text
2
abcd
```

Output:
```text
-1
```

Giải thích:
- Không thể sắp xếp các ký tự của `abcd` để thu được chuỗi có dạng `T` lặp đúng `2` lần.

---

## 🧠 Phân tích
Ta cần tạo chuỗi kết quả có dạng:

`T + T + ... + T` (lặp `k` lần)

Vì được phép sắp xếp lại ký tự nên thứ tự ban đầu không quan trọng,
chỉ cần quan tâm số lượng từng ký tự.

Hãy tưởng tượng ta chia chuỗi kết quả thành `k` khối giống hệt nhau,
mỗi khối chính là `T`.

Ký hiệu `cnt[c]` là số lần ký tự `c` xuất hiện trong chuỗi `S`.

Ví dụ nếu `S = aabbcc` thì:
- `cnt = {'a': 2, 'b': 2, 'c': 2}`
- `cnt['a'] = 2`, `cnt['b'] = 2`, `cnt['c'] = 2`

Giả sử ký tự `c` xuất hiện `cnt[c]` lần trong `S`.

Nếu kết quả là `T * k`, tổng số ký tự `c` phải được chia đều cho `k` khối.
Vì vậy, trong mỗi bản `T`, ký tự `c` phải xuất hiện:

`cnt[c] / k`

Do đó điều kiện bắt buộc là:

`cnt[c] % k == 0` với mọi ký tự `c`.

Nếu có ít nhất 1 ký tự không chia hết cho `k` thì không thể tạo chuỗi lặp đều `k` lần.

---

## 🔍 Thuật toán
1. Nhập `k`, `S`.
2. Dùng `Counter` để đếm tần suất, lưu vào `cnt` (`cnt[c]` là số lần xuất hiện của ký tự `c`).
3. Với mỗi ký tự:
   - nếu `cnt[c] % k != 0` -> in `-1` và dừng.
4. Tạo `T` từ các ký tự theo thứ tự từ điển:
   - thêm `c * (cnt[c] // k)` vào `T`.
5. In `T * k`.

---

## 💻 Code Python
```python
from collections import Counter

k = int(input())
S = input().strip()

cnt = Counter(S)

for c in cnt:
    if cnt[c] % k != 0:
        print(-1)
        break
else:
    T = ""
    for c in sorted(cnt):
        T += c * (cnt[c] // k)
    print(T * k)
```

---

## ⚡ Độ phức tạp
- Thời gian: `O(n + m log m)` với `m` là số ký tự khác nhau (ở đây `m <= 26`, nên coi như gần `O(n)`)
- Bộ nhớ: `O(m)` (hoặc `O(26)`)

---

## 🎯 Chốt nhớ nhanh
Muốn tạo chuỗi lặp `k` lần -> mỗi ký tự phải có số lần xuất hiện chia hết cho `k`.

---

[⬅ Quay lại mục lục](README.md)
