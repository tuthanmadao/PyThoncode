"""
    Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.
    - Nhập vào một số nguyên dương và <= độ dài của list gốc.
    - Dùng lệnh for i in range(m) để chia list gốc ra làm hai list mới với list đầu có độ dài m
        + Gán các phần tử trong list gốc từ 0 đến m vào list mới
        + các phần tử còn lại đẩy sang mội list khác. lúc này ta sẽ được hai list mới tách ra
        từ list gốc.
    - Ngoài ra ta có thể dùng lệnh đoạn cắt như sau:
        + list_so1 = list_goc[0:m]: lấy tất cả các phần tử từ có chỉ số từ 0 đến m - 1 gán vào list_so1
        + list_so2 = list_goc[m:]: lấy tất cả các phần tử từ có chỉ số từ m đến hết gán vào list_so2
        => khi này ta được hai list mới có độ tổng độ dài bằng list gốc.
    - Khi m bằng độ dài list gốc, ta sẽ tách được hai list mới trong đó một list có độ dài bằng list gốc,
    list kia sẽ là list rỗng.

"""

list_goc = ["táo", "1kg", 2, 5, "bcd", "xoài", "cóc", "dừa", "bòng", "cam", "chuối", "chanh", "10 cân"]
list_so3 = []
list_so4 = []
# ######################################################################################################
# Đoạn chương trình nhập m nguyên dương và m nhỏ hơn list gốc
while True:
    m = int(input("bạn muốn tách thành hai list, với list với độ dài là: "))
    if 0 < m <= len(list_goc):
        break
# ######################################################################################################
# Đoạn chương trình tách chuỗi dùng đoạn cắt
list_so1 = list_goc[0:m]
list_so2 = list_goc[m:]

print("chuỗi tách bằng phương pháp dùng đoạn cắt")
print(list_so1)
print(list_so2)

# ######################################################################################################
# Ngoài ra ta có thể làm theo cách dùng hàm for
for i in range(m):
    list_so3.append(list_goc[i])
for i in range(m, len(list_goc)):
    list_so4.append(list_goc[i])

print("chuỗi mới dùng hàm for:")
print(list_so3)
print(list_so4)

