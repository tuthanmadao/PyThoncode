"""
    Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.
    - Dùng hàm random để tạo ra các số ngẫu nhiên từ 0 đến độ dài list
    - Lấy 5 phần tử có vị trí tương ứng với các số ngẫu nhiên lấy được
"""
import random
list_vd = ["Chuoi", "xoai", "hong xiem", 1, 2, 3, 3.14, "bong", "hoa hong", "xe may"]
list_index = []
list_moi = []
# ####################################################################################################################
# Lấy 5 vị trí ngẫu nhiên:
for i in range(5):
    while True:
        k = random.randint(0, len(list_vd) - 1)
        if list_index.count(k) < 1:
            break
    list_index.append(k)
# ####################################################################################################################
# Lấy 5 phần tử từ chuỗi cũ gán sang chuỗi mới theo các chỉ số trong list_index
for i in list_index:
    list_moi.append(list_vd[i])
print(list_index)
print(list_moi)

