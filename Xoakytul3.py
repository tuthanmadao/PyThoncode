"""
    Chương trình xóa bỏ các ký tự có chỉ số là chỉ số lẻ.
    Ở đây ta sẽ phải dùng phương pháp duyệt theo chỉ số
    Với các chỉ số lẻ sẽ phải loại bỏ ra khỏi chuỗi.
"""
str1 = input('Nhập vào một chuỗi bất kỳ: ')
str2 = ''

for i in range(0, len(str1), 2):
    # 0 là giá trị bắt đầu, kết thúc là độ dài của str1 với bước nhẩy là 2
    # Mục đích là để không in hoặc không lựa chọn các phần tử có chỉ số lẻ
    print(str1[i], end='')
    str2 = str2 + str1[i]  # Lấy tất cả các phần tử có chỉ số chẵn để đẩy vào một chuỗi mới "str2"
print('', end='\n')
print(str2)
