"""
    Viết chương trình lấy các các giá trị không trùng lặp từ dict
    - Cách 1: Lấy list các giá trị value của dict bằng lệnh value().
    - Chuyển list nhận được thành dạng set để loại bỏ các phần tử bị trùng lặp. Cách này sẽ thay đổi thứ tự của các
    value nhận được so với trong dict gốc
    - In ra các giá trị nhận được
    - Cách 2: Duyệt từng phần tử của dict. Lấy các value của các key gán vào một list chứa các giá trị value nếu các
    value chưa có trong list. Thứ tự các value so với trong dict gốc được giữ nguyên
"""
import random
new_list = []
my_dict = {random.randint(0, 15): random.randint(0, 10) for i in range(10)}
print("Dict tạo được là: ")
print(my_dict)

# ######################################################################################################################
# Cách 1:
# lấy list các
list_value = my_dict.values()

# Chuyển list chứa các giá trị nhận được thành định dạng set để loại các phần tử trùng lặp
new_set = set(list_value)

# In ra dict mới tạo
print(f"Các giá trị value không trùng lặp của dict là: {new_set}")
# ######################################################################################################################
# Cách 2:
# Duyệt các phần tử của dict để lấy ra value gán vào list mới với các value chưa có trong list mới
for i in my_dict:
    if my_dict.get(i) not in new_list:
        new_list.append(my_dict.get(i))
print(f"Các giá trị value không trùng lặp của dict là: {new_list}")
