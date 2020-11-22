"""
    Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
        Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
"""
import random
# Tạo ra dict bất kỳ phù hợp với yêu cầu đề bài:
my_dict = {i: [random.randint(0, 9) for j in range(5)] for i in range(10)}
print("Dict tạo được:")
print(my_dict)
# ######################################################################################################################
# Truy cập và in ra phần tử thứ 5 trong phần value của các phần tử trong dict
print("Phần tử thứ 5 của các value trong dict là")
# Duyệt các phần tử bằng hàm for
for pt in my_dict:
    print(my_dict[pt][4], end=" ")
