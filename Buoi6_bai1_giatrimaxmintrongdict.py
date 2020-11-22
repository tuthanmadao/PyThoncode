"""
    Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict

"""
import random
my_dict = {i: random.randint(0, 20) for i in range(10)}
print("Dict tạo được là: ")
print(my_dict)

# ######################################################################################################################
# In ra phần tử min, max - Viết gộp trên 1 dòng lệnh
print(f"Giá trị nhỏ nhất là: {min(my_dict.values())}")
print(f"Giá trị lớn nhất là: {max(my_dict.values())}")
