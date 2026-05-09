# Chương 1: JavaScript ES6+ Essentials

Để học React tốt, bạn cần thành thạo các tính năng mới của JavaScript (ES6+). Dưới đây là những thứ quan trọng nhất.

## 1. Arrow Functions (Hàm mũi tên)
Giúp viết code ngắn gọn hơn và xử lý từ khóa `this` dễ dàng hơn (quan trọng trong React Class Components cũ, nhưng vẫn là chuẩn mực trong Functional Components mới).

```javascript
// Function thông thường
function sum(a, b) {
  return a + b;
}

// Arrow Function
const sum = (a, b) => a + b;

// Nếu chỉ có 1 tham số, không cần ngoặc đơn
const square = x => x * x;

// Nếu không có tham số
const sayHi = () => console.log("Hi!");
```

## 2. Destructuring (Phá vỡ cấu trúc)
Giúp lấy dữ liệu từ Object hoặc Array cực nhanh.

### Với Object:
```javascript
const person = {
  name: "Tên bạn",
  age: 20,
  country: "Vietnam"
};

// Cách cũ
const name = person.name;
const age = person.age;

// Destructuring
const { name, age, country } = person;
```

### Với Array:
```javascript
const colors = ["Red", "Green", "Blue"];

// Lấy phần tử đầu và thứ hai
const [first, second] = colors;
```

## 3. Template Literals (Chuỗi mẫu)
Sử dụng dấu backtick ( \` ) để nối chuỗi và chèn biến linh hoạt.

```javascript
const name = "React";
const type = "Library";

// Dùng dấu huyền và ${}
console.log(`${name} là một ${type} của JavaScript.`);
```

## 4. Spread & Rest Operator (...)
Dùng để sao chép object/array hoặc gom các tham số.

```javascript
// Spread (Sao chép)
const oldList = [1, 2];
const newList = [...oldList, 3, 4]; // [1, 2, 3, 4]

const user = { name: "A", age: 10 };
const updatedUser = { ...user, age: 11 }; // { name: "A", age: 11 }
```

---

## 🎯 Bài tập thực hành
**Yêu cầu:** 
Viết một hàm Arrow Function tên là `showLaptopInfo` nhận vào một Object `laptop` có cấu trúc: `{ brand: string, price: number }`.
Sử dụng **Destructuring** để lấy `brand`, `price` và dùng **Template Literals** để in ra chuỗi: 
*"Máy tính [brand] có giá [price] USD"*.

**Gợi ý code:**
```javascript
const laptop = { brand: "MacBook", price: 1500 };

const showLaptopInfo = ({ brand, price }) => {
  // Viết code của bạn ở đây
};

showLaptopInfo(laptop);
```
