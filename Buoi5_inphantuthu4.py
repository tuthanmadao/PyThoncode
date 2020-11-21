"""
    Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple.
    - Dùng lệnh print(tuple_a[4]) và phần tử thứ 4 từ cuối lên dùng print(tuple_a[-4])
"""
tuple_a = ("banana", 2, 3, "apple", "iphone", 3.14, "pi", "Python", "book", "Samsung")

print("Tuple:")
print(tuple_a)
print(f"Phần tử thứ 4 của tuple là: {tuple_a[3]}")
print(f"Phần tử thứ 4 từ cuối lên là: {tuple_a[-4]}")
