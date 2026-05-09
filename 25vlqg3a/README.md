# Lộ trình học React (React Learning Roadmap)

Chào mừng bạn đến với hành trình chinh phục React! Đây là lộ trình chi tiết để bạn đi từ số 0 đến khi có thể xây dựng được ứng dụng thực tế.

## 1. Giai đoạn chuẩn bị (Prerequisites)
Trước khi bắt đầu với React, hãy đảm bảo bạn đã nắm vững:
- **[Chương 1: JavaScript ES6+ Essentials](./CH01_JS_ES6.md)**
- **HTML5 & CSS3:** Layout (Flexbox, Grid), Responsive design.
- **JavaScript ES6+:** 
    - Arrow functions
    - Destructuring (Object & Array)
    - Spread/Rest operator
    - Map, Filter, Reduce
    - Promises & Async/Await
    - ES Modules (Import/Export)

## 2. Nền tảng React (Fundamentals)
- **JSX:** Cách viết giao diện trong JavaScript.
- **Components:** Chia nhỏ giao diện thành các phần có thể tái sử dụng (Functional Components).
- **Props:** Truyền dữ liệu từ component cha xuống component con.
- **State (useState):** Quản lý dữ liệu thay đổi trong component.
- **Lifecycle & Effects (useEffect):** Xử lý side-effects như gọi API, lắng nghe sự kiện.
- **Handling Events:** Xử lý click, input, form submit.
- **Conditional Rendering:** Hiển thị giao diện dựa trên điều kiện (if/else, &&, ternary).
- **List & Keys:** Hiển thị danh sách dữ liệu bằng vòng lặp.

## 3. Hooks nâng cao & Patterns
- **useContext:** Quản lý state toàn cục mà không cần truyền props quá nhiều tầng.
- **useRef:** Thao tác trực tiếp với DOM hoặc lưu trữ giá trị không gây render lại.
- **useMemo & useCallback:** Tối ưu hóa hiệu năng, tránh render thừa.
- **Custom Hooks:** Tách logic nghiệp vụ ra khỏi giao diện để tái sử dụng.

## 4. Hệ sinh thái React (Ecosystem)
- **Routing:** React Router DOM (Xây dựng ứng dụng đa trang).
- **State Management:** 
    - Zustand (Khuyên dùng: Đơn giản, nhẹ).
    - Redux Toolkit (Phổ biến trong các dự án lớn).
- **Styling:** Tailwind CSS, Styled Components hoặc SCSS.
- **Data Fetching:** Axios, TanStack Query (React Query) - Quản lý trạng thái server.
- **Form Handling:** React Hook Form.

## 5. Thực hành dự án (Projects)
- [ ] **Level 1:** Todo App (CRUD cơ bản).
- [ ] **Level 2:** Weather App hoặc Movie Search (Làm việc với API).
- [ ] **Level 3:** E-commerce Dashboard (Quản lý giỏ hàng, Auth, Routing phức tạp).

## 6. Tài liệu & Bài tập (Resources)
- **Contest Lập trình trẻ:** [https://tinhoctre.vn/contest/25vlqg3a](https://tinhoctre.vn/contest/25vlqg3a)

## 7. Ghi chú thuật toán / Lập trình thi đấu (Python)

### Tại sao `sys.stdin.readline` nhanh hơn `input()`?

Trong lập trình thi đấu với giới hạn thời gian (ví dụ: Time Limit: 1.0s), việc đọc dữ liệu lớn (hàng trăm ngàn dòng hoặc chuỗi rất dài) cực kỳ quan trọng.

**1. Hàm `input()` thông thường:**
*   Chạy chậm vì nó xử lý nhiều bước phụ phía sau hậu trường.
*   Nó phải kiểm tra xem có chuỗi prompt không (vd: `input("Nhập:")`).
*   Nó tự động tìm và cắt bỏ ký tự xuống dòng (`\n`).

**2. Hàm `sys.stdin.readline()`:**
*   Giao tiếp trực tiếp với bộ đệm của hệ điều hành, lấy raw data (dữ liệu thô).
*   Chạy cực kỳ nhanh (nhanh gấp khoảng 10 lần so với `input()`).
*   **Lưu ý:** Nó giữ lại cả ký tự xuống dòng `\n` ở cuối, nên thường phải dùng kèm `.strip()` để cắt bỏ đi (ví dụ: `sys.stdin.readline().strip()`).

**Lời khuyên:** Khi làm bài tập có dữ liệu đầu vào lớn (như chuỗi dài $10^5$ ký tự hoặc hàng ngàn dòng nhập), hãy luôn `import sys` và sử dụng `sys.stdin.readline()` để tránh lỗi **Time Limit Exceeded (TLE)**.
