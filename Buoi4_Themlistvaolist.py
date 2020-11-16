"""
    Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
    - Cách 1: Để thêm một chuỗi s vào các phần tử của list cũ ta dùng lệnh for để duyệt từng phần tử.
        + ta dùng new_list.append(pt + chuoi)
    - Cách 2: Hoặc ta có thể dùng cách viết new_list = [pt + chuoi for pt in old_list]
"""
old_list = ["bắp cải ", "cà chua ", "mướp đắng ", "cà rốt "]
chuoi = "để ăn"
new_list = []

# ###############################################################################################
# Thêm chuỗi s vào phần tử của old_list
for pt in old_list:
    new_list.append(pt + chuoi)
# ###############################################################################################
# Chèn thêm chuỗi s vào các phần tử của old_list bằng cách 2
new_list1 = [pt + chuoi for pt in old_list]

# ###############################################################################################
# In ra kết quả
print("Chuỗi cũ")
print(old_list)
print("chuỗi cần thêm là: '{}'".format(chuoi))
print("Chuỗi mới theo cách 1")
print(new_list)
print("Chuỗi mới theo cách 2")
print(new_list1)
