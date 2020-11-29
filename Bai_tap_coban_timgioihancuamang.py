"""
    Cho mảng một chiều các số thực hãy tìm đoạn [a,b] sao cho đoạn này chứa tất cả các giá trị trong mảng
    (a,b: số nguyên). (Sử dụng numpy)
"""
import numpy as np
mang = np.array([2.5, 4.5, 7.8, -5.0, -2.0, 2.0, 30.0, 25.0])
a = np.min(mang)
b = np.max(mang)
print(f"Đoạn [{a}, {b}] là đoạn chứa tất cả các giá trị trong mảng")
