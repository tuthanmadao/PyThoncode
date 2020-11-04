"""
    - Chương trình kiểm tra 3 số nhập được từ bàn phím có phải là 3 cạnh của 1 tam giác hay không
        Kiểm tra bằng cách sử dụng tính chất hai cạnh của một tam giác luôn nhỏ hơn tổng hai
        cạnh còn lại
    - Nếu là ba cạnh của một tam giác thì kiểm tra tiếp xem đó có phải là tam giác vuông hay không.
"""
a = float(input('Nhập số a = '))
b = float(input('Nhập số b = '))
c = float(input('Nhập số c = '))
if a + b > c and a + c > b and b + c > a:
    # Sử dụng quan hệ 3 cạnh của một tam giác
    print('a = {}, b = {}, c = {} là ba cạnh của một tam giác'.format(a, b, c))
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        # Kiểm tra tam giác vuông theo công thức Pytago đảo:
        # Nếu một tam giác có bình phương của một cạnh bằng tổng bình phương hai cạnh kia
        # thì đó là tam giác vuông
        print('Đây là ba cạnh của một tam giác vuông')
    else:
        print('Đây không phải là tam giác vuông')
else:
    print('a 1= {}, b = {}, c = {} không phải là ba cạnh của một tam giác'.format(a, b, c))
