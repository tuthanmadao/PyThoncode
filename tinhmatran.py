"""
    Tạo ma trận, tính A^n
"""
# import numpy as np
# import random
# B = []
# m = int(input("nhập vào số m = "))
# n = int(input("nhập vào số n = "))
#
# A = np.array([np.random.randint(0, 9, m) for i in range(m)])
#
# print(A)
# print(f"B \n{B}")
import sys

random_list = ['a', 0, 0.5]

for item in random_list:
    try:
        print("Phần tử:", item)
        r = 1 / int(item)
        print("Nghịch đảo của ", item, "is", r)
    except:
        print("Oops!", sys.exc_info()[0], "Toang Rồi!.")  # import module sys to get the type of exception
        print("=> next \n")
print("12345")