"""
    Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict
    - ĐƠn giản nhất là ta sắp xếp key theo chiều tăng dần bằng lệnh sorted().
    => khi đó các phần tử [-1], [-2], [-3] trong list vừa nhận được chính là 3 key lớn nhất cỉa dict
    - In ra 3 phần tử có key vừa tìm được.
"""
import random
# Tạo dict với các key:value bất kỳ
my_dict = {random.randint(0, 15): random.randint(0, 13) for i in range(10)}
print("Dict gốc: ")
print(my_dict)
# ######################################################################################################################
# Tìm 3 key lớn nhất của dict bằng cách sắp xếp các key của list theo thứ tự tăng dần
list_key = sorted(my_dict)
# In ra 3 phần tử có key thỏa mãn điều kiện
print(f"cặp key - value có key lớn thứ nhất: {list_key[-1]}:{my_dict.get(list_key[-1])}")
print(f"cặp key - value có key lớn thứ hai: {list_key[-2]}:{my_dict.get(list_key[-2])}")
print(f"cặp key - value có key lớn thứ ba: {list_key[-3]}:{my_dict.get(list_key[-3])}")
