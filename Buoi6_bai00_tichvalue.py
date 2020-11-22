"""
    Viết chương trình tính tích value của các phần tử trong một dict
    - Ta dùng lệnh value() để lấy ra list các value
    - sau đó dùng lệnh math.prob để tính tích tất cả các value có trong list
"""
import random
import math
# Tạo chuỗi mặc định 10 phần tử từ 0 đến 9
new_dict = {i:random.randint(0,9) for i in range(10)}
print("Dict tạo được là:")
print(new_dict)
# ######################################################################################################################
# Tính tích các value được đọc ra từ dict (viết gộp trong một dòng lệnh)

print(f"Tích các value trong dict là: {math.prod(new_dict.values())}")
