"""
    Viết chương trình tính tổng, tích của các phần tử trong một list.
    - Tính tích các phần tử ta dùng for pt in list_01: tich = tich*list_01[i], hoặc dùng
    hàm math.prod(list_01)
    - tính tổng có thể dùng như tính tích hoặc dùng hàm sum(list_01) để tính tổng
    hoặc dùng hàm math.fsum(list_01) để tính tổng. Với hàm math.fsum() thì phải import math
"""
import math
tich = 1
tong = 0
list_01 = [1, 2, 4, 5, 7, 8, 10, 20, 36, 11]

# ##############################################################################################
# Tính tích bằng for
for pt in list_01:
    tich = tich * pt
# #############################################################################################
# Tính tích bằng hàm math.prod
tich1 = math.prod(list_01)
# #############################################################################################
# tính tổng:
for pt in list_01:
    tong += pt
# #############################################################################################
# Tính tổng bằng hàm sum
tong1 = sum(list_01)
# #############################################################################################
tong2 = math.fsum(list_01)

print("tich các phần tử trong list là: ",tich)
print("tích cách phần tử dùng hàm math.prod: ",tich1)
print("tổng tính theo hàm for: ",tong)
print("tổng tính theo hàm sum",tong1)
print("tổng tính theo hàm math.fsum: ",tong2)
