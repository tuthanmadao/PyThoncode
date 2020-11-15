"""
    Viết chương trình xóa bỏ ký tự thứ m
    Bước 1: Nhập Chuỗi bất kỳ từ bàn phím
    Bước 2: Nhập số m từ bàn phím
    Bước 3: Ta kiểm tra xem đó có phải chuỗi rỗng hay không bằng câu lệnh if len(str1) > 0
        - Nếu như kế quả đó ko phải chuỗi rỗng (khi đó len(str1) sẽ có độ dài > 0)chuyển sang bước 4
        - Nếu là chuỗi rỗng ta in ra màn hình dòng chữ:"chuỗi nhập được là chuỗi rỗng"
    Bước 4: Ta phải kiểm tra xem ký tự m nhập vào có nằm trong chuỗi cần nhập hay không?
    Sử dụng câu lệnh if m < len(str1).
        - Khi kết quả trả về là True thì m nằm trong chuỗi cần xóa ta chuyển bước 5
        - Khi kết quả trả về False thì m nằm ngoài chuỗi ta in ra dòng:"ký tự thứ m nằm ngoài chuỗi"
    Bước 5: Ta dùng lệnh for duyệt từng phần tử trong chỗi. Các phần tử có chỉ số khác m sẽ được nhập
    vào chuỗi mới. Sau khi duyệt xong ta sẽ in ra chuỗi mới đã xóa đi phần tử thứ m
"""
str1 = input("Nhập vào một chuỗi: ")
while True:
    m = int(input('Nhập vào vị trí m cần xóa: '))
    if 0 <= m:
        break
str2 = ""
if len(str1) > 0:
    if m < len(str1):
        for i in range(len(str1)):
            if i != m:
                str2 = str2 + str1[i]
        print('Chuoi mới là: {}'.format(str2))
    else:
        print('phần tử thứ {} nằm ngoài chuỗi đã nhập.'.format(m))
else:
    print('Chuỗi nhập vào là một chuỗi rỗng')
