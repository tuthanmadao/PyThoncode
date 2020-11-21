"""
    Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.
    - Tìm phần tử lớn nhất:
        + Cách 1: Dùng lệnh max() để tìm ra phần tử lớn nhất.
        + Cách 2: Ta dùng duyệt for duyệt tất cả các phần tử để tìm phần tử lớn nhất bằng lệnh
                if ptmax < pt:
                    ptmax = pt
    - Tính tống các phần tử trong tuple:
        + Cách 1: dùng lệnh sum()
        + Cách 2: dùng lệnh toán học trong thư viện math: math.fsum()
        + Cách 3: Dùng lệnh vòng lặp for để cộng các phần tử

"""
import math
my_tuple = (2.0, 3.5, 3.6, 4.0, 4.3, -1.8)
ptmax = 0
tong = 0
# ######################################################################################################################
# Cách 1: tìm phần tử lớn nhất:
print(f"Phần tử lớn nhất trong Tuple tìm được theo cách 1 là{max(my_tuple)}")
# ######################################################################################################################
# Cách 2: tìm phần tử lớn nhất:
for pt in my_tuple:
    if ptmax < pt:
        ptmax = pt
print(f"Phần tử lớn nhất của Tuple theo cách 2: {ptmax}")
# ######################################################################################################################
# Cách 1: Tính tổng:
print(f"Tổng các phần tử tuple tính theo cách 1 bằng: {sum(my_tuple)}")
# ######################################################################################################################
# Cách 2: Tính tổng:
print(f"Tổng các phần tử tuple tính theo cách 2 bằng: {math.fsum(my_tuple)}")
# ######################################################################################################################
# Cách 3: Tính tổng:
for pt in my_tuple:
    tong += pt
print(f"Tổng các phần tử tuple tính theo cách 3 bằng: {tong}")
