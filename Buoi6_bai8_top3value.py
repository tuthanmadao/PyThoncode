"""
    Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict
    - Để dễ dàng lấy được top 3 của dict_goc ta dùng lệnh dict.value() để lấy ra được list các value. sau đó chuyển đổi
    list đó thành một set() sắp xếp và chuyển ngược trở lại list. khi đó ta có được một list chứa các value đã được sắp
    xếp. khi đó phần tử [-1][-2][-3] chính là top 3 value có giá trị lớn nhất của dict.
    - Sau đó ta duyệt các phần tử trong dict. so sánh value trong dict với các value thuộc top 3 lấy được. Sau đó lấy ra
    được tất cả các phần tử có value thuộc top 3. Để làm được cần kết hợp hàm for và if.
"""
import random
dict_goc = {random.randint(0, 17): random.randint(0, 20) for i in range(10)}
dict_moi = {}
print("Dict tạo được:")
print(dict_goc)
# ######################################################################################################################
# lấy ra list các value trong dict gốc.
list_value = dict_goc.values()
# ######################################################################################################################
# Đẩy chuỗi vừa tạo được thành dạng set. Sau đó chuyển lại thành list và sắp xếp lại theo chiều tăng dần.
list_value_sort = sorted(list(set(list_value)))

# Duyệt các phần tử top 3 và tìm kiếm tất cả các key có value thuộc top 3
# Đồng thời in ra các phần tử có value thuộc top 3:
# Đưa các phần tử này vào dict mới để lưu trữ cũng như có thể sử dụng sau này.
print("Các phần tử thuộc top 3 value lớn nhất từ dict gốc")
for i in range(-1, -4, -1):
    for key in dict_goc:
        if dict_goc[key] == list_value_sort[i]:
            dict_moi[key] = dict_goc[key]
            print(f"{key}: {dict_goc[key]}")
# In ra dict mới tạo được.
print("Dict chứa tất cả các phần tử thuộc top 3 value trong dict gốc")
print(dict_moi)
