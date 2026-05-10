# Bài toán: Chia kẹo

**Time Limit:** 1.0s  |  **Memory Limit:** 1G

## Đề bài

Cho $N$ học sinh được đánh số từ 1 đến $N$ xếp thành một vòng tròn.
Có $M$ cái kẹo được phát lần lượt theo thứ tự:
$1 \rightarrow 2 \rightarrow 3 \rightarrow \dots \rightarrow N \rightarrow 1 \rightarrow 2 \rightarrow \dots$ (lặp lại).
Mỗi học sinh nhận một cái kẹo mỗi lần đến lượt.

**Yêu cầu:** Tìm học sinh nhận được cái kẹo cuối cùng.

## Dữ liệu nhập vào từ bàn phím
Gồm hai số tự nhiên $N$ và $M$ ($1 \le N, M \le 100$), mỗi số trên một dòng.

## Kết quả ghi ra màn hình
Một số tự nhiên duy nhất là **số thứ tự của học sinh nhận cái kẹo cuối cùng**.

## Ví dụ

**Input**
```text
3
10
```

**Output**
```text
1
```

---

# Giải thích chi tiết bài toán "Chia kẹo"

Trước tiên, chúng ta cần hiểu rõ các dữ kiện đề bài cho:
*   **$N$**: Là số lượng **học sinh** đứng thành vòng tròn.
*   **$M$**: Là số lượng **cái kẹo** sẽ được phát.

Đề bài yêu cầu tìm vị trí của học sinh nhận được cái kẹo cuối cùng (cái kẹo thứ $M$).

Tại sao công thức giải nhanh lại là `(M - 1) % N + 1`? Dưới đây là phân tích từng bước để bạn hiểu bản chất của các bài toán dạng "vòng tròn" này.

## 1. Phân tích đề bài theo góc nhìn "Chu kỳ"
Bạn có $N$ học sinh đứng thành vòng tròn. Việc phát kẹo diễn ra liên tục. Đây chính là một **hệ thống tuần hoàn** với chu kỳ là $N$.

*   **Lượt 1:** Kẹo từ $1$ đến $N$ phát cho HS $1, 2, \dots, N$.
*   **Lượt 2:** Kẹo từ $N+1$ đến $2N$ lại phát cho HS $1, 2, \dots, N$.
*   ... và cứ thế tiếp diễn.

## 2. Tại sao lại dùng phép Modulo (%)?
Phép chia lấy dư (`M % N`) cho chúng ta biết kẹo cuối cùng nằm ở đâu **sau khi đã hoàn thành các vòng chia đầy đủ**.

**Ví dụ với $N=3, M=10$:**
*   Mỗi vòng cần 3 cái kẹo.
*   $10 \div 3 = 3$ dư $1$.
*   Nghĩa là chúng ta đã chia được **3 vòng hoàn chỉnh** (tổng cộng 9 cái kẹo), và còn **dư lại 1 cái kẹo**.
*   Cái kẹo dư thứ 1 này sẽ bắt đầu lượt chia mới và rơi vào học sinh đầu tiên: **HS số 1**.

## 3. Điểm yếu của phép chia dư thông thường
Toán học máy tính có một đặc điểm: `số_chia % số_chia = 0`.
*   Nếu $M=3, N=3$ (kẹo cuối rơi vào HS số 3):
    *   $3 \% 3 = 0$ (Trong khi ta cần kết quả là 3).
*   Nếu $M=6, N=3$ (kẹo cuối rơi vào HS số 3):
    *   $6 \% 3 = 0$ (Trong khi ta cần kết quả là 3).

=> **Quy luật:** Khi chia hết, kết quả máy tính trả về là $0$, nhưng thực tế học sinh nhận kẹo là người cuối cùng (người thứ $N$).

Trong lập trình, phép chia lấy dư `% N` luôn trả về kết quả từ $0$ đến $N-1$. 
Nhưng danh sách học sinh của chúng ta lại đánh số từ $1$ đến $N$.

## 4. Giải pháp: Kỹ thuật "Dịch gốc 0" (Shift to Zero-index)

Đây là phần quan trọng nhất để hiểu công thức. Hãy tưởng tượng thế này:

### Tại sao phải "dịch"?
Máy tính và phép toán `%` (Modulo) "thích" số 0. Khi bạn chia cho 3, kết quả dư chỉ có thể là `0, 1, 2`. 
Nhưng con người lại thích đánh số từ 1: `1, 2, 3`.

Sự lệch pha này tạo ra rắc rối ở số cuối cùng ($N$):
*   Con người gọi là người thứ **3**.
*   Máy tính tính toán ra dư **0**.

Để giải quyết, chúng ta dùng mẹo: **"Đưa tất cả về gốc 0 để máy tính tính đúng, sau đó mới trả về gốc 1 cho con người."**

### Quy trình chi tiết 3 bước:

| Bước | Hành động | Mục tiêu |
| :--- | :--- | :--- |
| **B1: Trừ 1** | `M - 1` | Biến kẹo 1 thành 0, kẹo 2 thành 1... kẹo $N$ thành $N-1$. Bây giờ kẹo cuối cùng của vòng đầu tiên không còn là $N$ nữa mà là $N-1$. |
| **B2: Chia dư** | `% N` | Phép chia này hoạt động hoàn hảo trên dãy từ $0$ đến $N-1$. Nếu kết quả là $0$, nó thực sự là vị trí đầu tiên. Nếu kết quả là $N-1$, nó thực sự là vị trí cuối cùng. |
| **B3: Cộng 1** | `+ 1` | Sau khi máy tính đã tìm ra vị trí chính xác (theo kiểu của nó), ta cộng 1 để chuyển số hiệu đó về đúng tên mà con người đã đặt cho học sinh. |

### Ví dụ cực kỳ chi tiết với $N=3, M=3$ (Kẹo rơi vào HS 3):
1.  **Trừ 1:** $3 - 1 = 2$. (Ta coi như đang tìm vị trí của cái kẹo thứ "2" trong hệ thống bắt đầu từ 0).
2.  **Chia dư:** $2 \% 3 = 2$. (Vị trí "2" trong hệ thống 0 chính là: 0, 1, **2**).
3.  **Cộng 1:** $2 + 1 = 3$. (Chuyển vị trí "2" của máy tính thành HS số "3" của con người). **Kết quả đúng!**

Nếu không có bước trừ 1 và cộng 1, phép toán `3 % 3` sẽ ra `0`, và bạn sẽ phải viết thêm lệnh `if (du == 0) du = N` rất rắc rối. Kỹ thuật dịch gốc này giúp công thức ngắn gọn và chạy được cho mọi trường hợp.

## 5. Mô phỏng trực quan ($N=3, M=10$)
Hãy tưởng tượng các cái kẹo được xếp hàng dài:
`K1, K2, K3 | K4, K5, K6 | K7, K8, K9 | K10`

*   **Cụm 1:** HS 1, 2, 3 nhận.
*   **Cụm 2:** HS 1, 2, 3 nhận.
*   **Cụm 3:** HS 1, 2, 3 nhận.
*   **Kẹo cuối (K10):** Rơi vào người tiếp theo sau khi kết thúc cụm 3 $\rightarrow$ **HS 1**.

## 6. Tổng kết
> **`Học sinh = (Số kẹo - 1) % Số người + 1`**

---

## Lời giải (Python)

```python
# Nhập số học sinh N và số kẹo M từ bàn phím
# Vì mỗi số nằm trên một dòng, ta gọi input() hai lần
N = int(input())
M = int(input())

# Áp dụng công thức dịch gốc 0: (M - 1) % N + 1
result = (M - 1) % N + 1

# In kết quả ra màn hình
print(result)
```
