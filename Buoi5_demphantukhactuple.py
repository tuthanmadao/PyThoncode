"""
    Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.
    - Duyệt từng phần tử. nếu các phần tử không phải là tuple (kiểm tra bằng lệnh type()) thì biến đếm tăng lên 1. Nếu
    phần tử đọc được là tuple thì thoát khỏi vòng lặp.
    - kết quả đếm được sẽ là số lượng các phần từ từ đầu đến phần tử tuple.
"""
tuple_a = ("banana", 2, 3, "apple", ("iphone", 1), 3, 3.14, "pi", "Python", "book", "Samsung", (1, 2))
dem = 0
for pt in tuple_a:
    if type(pt) == type(tuple_a):
        break
    else:
        dem += 1
print(f"Có {dem} phần tử trước tuple {pt}")
