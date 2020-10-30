"""
    Viết chương trình tính giá trị biểu thức theo yêu cầu:
    Bước 1: Bài nhập 3 số thực x, y, z bất kì.
    Bước 2: Tính giá trị biểu thức F:
            F = (x + y + z) / (x ** 2 + y ** 2 + 1) - |x - z * cos(y)|
    Bước 3: Đưa giá trị tính được của F ra màn hình dưới dạng:
            Gia tri cua F = <gia tri>
"""
import math

# Thực hiện bước 1:
# Vì dữ liệu đọc được là dạng tring nên ta cần ép kiểu để sử dụng

print("Nhập số X")
x = float(input())
print("Nhập số Y")
y = float(input())
print("Nhập số Z")
z = float(input())

# Tính toán biểu thức F

f = (x + y + z) / (x ** 2 + y ** 2 + 1) - math.fabs(x - z * math.cos(y))

# In kết quả ra màn hình theo cú pháp

print("Gia tri cua F = <" + str(f) + ">")
