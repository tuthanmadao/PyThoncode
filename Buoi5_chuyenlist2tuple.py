"""
    Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple
    - Chuyển từ tuple => list dùng lệnh ép kiểu list()
    - Chuyển từ list => tuple dùng lệnh ép kiểu tuple()
"""
tuple_a = ("banana", 2, 3, "apple", "iphone", 3.14, "pi", "Python", "book", "Samsung")

print("Tuple gốc:")
print(tuple_a)
list_a = list(tuple_a)
print("tuple => list")
print(list_a)
tuple_b = tuple(tuple_a)
print("list => tuple")
print(tuple_b)
