"""
    Viết chương trình đảo ngược một tuple.
    - Cách 1: ta chuyển tuple cần đảo ngược về list, sau đó ta dảo ngược lại list đó rồi chuyển ngược lại dạng tuple
    - Cách 2: ta dùng duyệt for và dùng lện inser() để đẩy lệnh vào vị trí 0 của list trung gian từ đó ta được list đảo
    ngược. Sau đó ta chuyển list thành tuple
    - Cách 3: Dùng kỹ thuật cắt: với chỉ số âm, bước nhảy -1. tuple_dao = tuple_a[-1: -len(tuple_a) - 1: -1]
    - Cách 4: giống với cách 2 khác là ta duyệt bằng chỉ số âm. Sau đó dùng lệnh list.append() để add phần tử vào list.
    sau đó ta chuyển lại dạng tuple => ta được chuỗi đảo.
"""
tuple_a = ("banana", 2, 3, "apple", "iphone", 3.14, "pi", "Python", "book", "Samsung")
list_tg1 = []

# ######################################################################################################################
# Cách 1:
print("Cách 1: ")
list_tg = list(tuple_a)
list_tg.reverse()
tuple_dao = tuple(list_tg)
print("Tuple gốc: ")
print(tuple_a)
print("Tuple đảo: ")
print(tuple_dao)
# ######################################################################################################################
# Cách 2:
list_tg = []
print("Cách 2:")
for pt in tuple_a:
    list_tg.insert(0, pt)
tuple_dao = tuple(list_tg)
print(tuple_dao)
# ######################################################################################################################
# Cách 3:
print("Cách 3:")
tuple_dao = tuple_a[-1: -len(tuple_a) - 1: -1]
print(tuple_dao)
# ######################################################################################################################
# Cách 4:
print("Cách 4")
for i in range(-1, -len(tuple_a) - 1, -1):
    list_tg1.append(tuple_a[i])
tuple_dao = tuple(list_tg1)
print(tuple_dao)
