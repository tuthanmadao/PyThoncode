"""
    Viết chương trình sắp xếp các phần tử của dict theo chiều tăng dần của key
    - Ta lấy ra list các key được sắp xếp theo thứ tự tăng dần bằng lệnh sorted()
    - Sau đó ta tạo dict mới dựa trên list key được sắp xếp
"""
import random
new_dict = {}
my_dict = {random.randint(0, 15): random.randint(0, 20) for i in range(10)}
print("Dict tạo được là: ")
print(my_dict)

# ######################################################################################################################
# lấy list các key đã được sắp xếp
list_key = sorted(my_dict)

# Tạo dict mới bằng cách duyệt từng phần tử key đã được sắp xếp và giá trị value được lấy từ dict gốc.
for pt in list_key:
    new_dict[pt] = my_dict.get(pt)

# In ra dict mới tạo
print(new_dict)
