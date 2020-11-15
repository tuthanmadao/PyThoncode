"""
    Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.
    Bước 1: Nhập một chuỗi từ bàn phím
    Bước 2: Ta Duyệt lần lượt từng phần tử để tìm giá trị lớn nhất và giá trị nhỏ nhất.
    Sẽ có 3 trường hợp xảy ra là lớn hơn, nhỏ hơn và bằng
        - Ta gán max = min = str0[0]
        - Để duyệt từng phần từ ta dùng lệnh for i in range(1, len(str1), 1)
        - Ta tìm số lớn nhất bằng hàm if max < str1[i]
            + Kếu quả là True ta gán max = str1[i] sau đó thực hiện tiếp với chỉ số tiếp theo
            + Nếu kết quả là False ta thực hiện bước tiếp
        - Ta tìm số nhỏ hơn bằng hàm if min > str1[i]
            + Nếu kết quả là True ta gán min = str[i] rồi thực hiện với chỉ số tiêp theo
            + Nếu kết quả là False ta thực hiện bước tiếp
        - Đến khi duyệt hết. ta sẽ tìm được phần tử max và min. Nếu như chuỗi là các ký tự giống nhau thì
        các phần tử trong chuỗi đều bằng nhau lúc này max = min. Khi đó ta kết luận chuỗi gồm các phần tử giống
        nhau.
"""
str1 = (input('nhập vào chuỗi bất kỳ: '))
max1 = min1 = str1[0]
for i in range(1, len(str1), 1):
    if max1 < str1[i]:
        max1 = str1[i]
    if min1 > str1[i]:
        min1 = str1[i]
if min1 == max1:
    print('chuỗi vừa nhập gồm các phần tử giống nhau')
else:
    print('Phần tử lớn nhất là {}, phần tử nhỏ nhất là: {}'.format(max1, min1))

"""
    Ngoài ra ta có thể dùng lệnh sau để tìm giá trị lớn nhất nhỏ nhất
    pt_max = max(str1)
    pt_min = min(str1)
"""

str1 = (input('nhập vào chuỗi bất kỳ: '))
pt_max = max(str1)
pt_min = min(str1)

if pt_max == pt_min:
    print('chuỗi vừa nhập gồm các phần tử giống nhau')
else:
    print('Phần tử lớn nhất là {}, phần tử nhỏ nhất là: {}'.format(pt_max, pt_min))

