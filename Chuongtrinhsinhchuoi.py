"""
    Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ
    hơn 2 thì in ra chuỗi rỗng.
    - Kiểm tra xem chuỗi có đủ điều kiện hay không? (if len(chuoi) >= 2)
        + Nếu kết quả là True ta chuyển sang bước tiếp
        + Nếu kết quả là False ta in ra chuỗi rỗng
    - Khi chuỗi nhập vào đủ điều kiện ta lấy hai ký tự đầu và 2 ký tự cuối của chuỗi nhập đưa vào chuỗi mới.
"""
chuoi = input('Nhập vào chuỗi bất kỳ: ')
if len(chuoi) >= 2:
    chuoi_moi = chuoi[0] + chuoi[1] + chuoi[-2] + chuoi[-1]
else:
    chuoi_moi = ""
print("Chuỗi mới được tạo là: {}".format(chuoi_moi))
