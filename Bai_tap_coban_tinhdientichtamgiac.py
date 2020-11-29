"""
    Viết chương trình nhập vào ba cạnh của một tam giác, tính và xuất ra diện tích của tam giác đó.
"""
import math

a = float(input('Nhập số a = '))
b = float(input('Nhập số b = '))
c = float(input('Nhập số c = '))
if a + b > c and a + c > b and b + c > a:
    # Sử dụng quan hệ 3 cạnh của một tam giác
    print('a = {}, b = {}, c = {} là ba cạnh của một tam giác'.format(a, b, c))
    s = 1 / 4 * math.sqrt((a + b + c) * (a + b - c) * (c + a - b) * (b + c - a))
    print(f"Diện tích của tam giác là: {s}")
else:
    print('a 1= {}, b = {}, c = {} không phải là ba cạnh của một tam giác'.format(a, b, c))
