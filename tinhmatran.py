"""
    Tạo ma trận, tính A^n
"""
import numpy as np
import random
B = []
m = int(input("nhập vào số m = "))
n = int(input("nhập vào số n = "))

A = np.array([np.random.randint(0, 9, m) for i in range(m)])

print(A)
print(f"B \n{B}")
