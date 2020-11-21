"""
    Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
    - Cách 1: ta đọc chuỗi vào list và tách thành từng chuỗi con bằng lệnh list.spliit(). Sau đó sắp xếp chuỗi theo tứ
    tự tăng dần với key = len. Lúc này phần tử tại chỉ số [-1] sẽ là chuỗi dài nhất.
    - Cách 2: ta duyệt các phần tử trong chuỗi. đếm từng phẩn tử trong chuỗi để tìm ra chuỗi lớn nhất.
            + Nếu các phần tử trong chuỗi khác ký tự khoảng trắng " " thì biến dem tăng 1 đv. Sau đó chuyển ngay đến
            vòng tiếp bằng lệnh continue
            + Nếu như gặp biến khoảng trắng chương trình sẽ không thực hiện ý 1 mà chuyến sang thực hiện ý 2.
            lúc này nếu biến dem > dodai_max thì dodai_max = dem, tu = tu_doc[i-dem:i] - đây là câu lệnh đọc chuỗi có
            đủ điều kiện
            + Sau khi thực hiện ý 2 thì chương trình sẽ khởi tạo lại biến dem và bắt đầu vòng lặp tiếp.
    - Cách 3: ta vẫn sẽ đọc chuỗi vào một list như cách 1. Tuy nhiên, để tìm từ lớn nhất ta sẽ dùng lệnh
    max(list_B,key=len). khi đó từ dài nhất sẽ được in ra
    - Cách 4: ta cũng vẫn đọc chuỗi vào list như cách 1. Tuy nhiên, ta sẽ duyệt từng phần tử trong list. phần tử là có
    độ dài lớn hơn thì ta sẽ ghi lại.
"""
tu_doc = input("nhập một chuỗi: ")

# ######################################################################################################################
# Cách 1:
list_A = tu_doc.split()
list_A.sort(key=len)
print(f"Cách 1: từ có độ dài lớn nhất là: {list_A[-1]}")

# ######################################################################################################################
# Cách 2:
tu = ""
dem = 0
dodai_max = 0

for i in range(len(tu_doc)):
    if tu_doc[i] != " ":
        dem += 1
        continue
    if dem > dodai_max:
        dodai_max = dem
        tu = tu_doc[i-dem:i]
    dem = 0
print(f"Cách 2: từ dài nhất là: {tu}")

# ######################################################################################################################
# Cách 3:
chuoi_B = tu_doc.split()
print(f"Cách 3: từ dài nhất là: {max(chuoi_B,key=len)}")
# ######################################################################################################################
# Cách 4:
tu_max = ""
list_B = tu_doc.split()
for pt in list_B:
    if len(pt) > len(tu_max):
        tu_max = pt
print(f"Cách 4: Từ dài nhất là {tu_max}")
