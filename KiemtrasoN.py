"""
    - Nhập một số n nguyên dương bất kỳ từ bàn phím với n <1000
        + Nếu số nhập vào không đúng điều kiện thì yêu cầu nhập lại
    - Tính tổng các chữ số của số đó
        + Ta phải tách số n ra thành các số hàng trăm, hàng chục và hàng đơn vị
        + Sau đó cộng tổng lại với nhau.
    - Hiển thị kết quả ra màn hình
"""
while True:
    n = int(input('Nhap vao so nguyen duong n (n < 1000) '))
    if 0 < n < 1000:
        break

'''
    Ta cũng có thể viết theo cách 2: tuy nhiên cách này ta phải gán giá trị cho n trước
    
    n = 0
    while n <= 0 or n >=1000:
        n = int(input('Nhap vao so nguyen duong n (n < 1000) ')) 
        
'''

# Tiến hành tách số n ra thành hàng trăm, hàng chục, hàng đơn vị
# Tách lấy số hàng trăm bằng cách lấy n // 1000
# Tách lấy số hàng chục bằng phép toán lấy số dư của phép chia n cho 100
# chia cho 10 ta lấy phần nguyên sẽ ra được số hàng chục, còn phần dư sẽ
# là số đơn vị
# ví dụ 123 // 100 = 1 - hàng trăm
#       123 % 100 = 23
#       23 // 10 = 2 - hàng chục
#       23 % 10 =3 - hàng đơn vị
so_hang_tram = n // 100
so_hang_chuc = (n % 100) // 10
so_hang_donvi = (n % 100) % 10

print('Số n = {} có tổng các chữ số bằng = {}'.format(n, so_hang_tram + so_hang_chuc + so_hang_donvi))
