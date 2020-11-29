"""
    Viết chương trình giải phương trình bậc 2 với các hệ số nhập từ bàn phím (xét đầy đủ các trường hợp).
"""
import math
a = float(input('Nhập số a = '))
b = float(input('Nhập số b = '))
c = float(input('Nhập số c = '))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print(f"Phương trình có nghiệm x = {-c/b}")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('Phương trình {}x^2 + {}x + {} có nghiệm phức.'.format(a, b, c))
        x1 = complex((-b / (2 * a)), (+ math.sqrt(abs(delta)) / (2 * a)))
        x2 = complex((-b / (2 * a)), (- math.sqrt(abs(delta)) / (2 * a)))
        print(f"X1 = {x1}")
        print(f"X2 = {x2}")
        print()
    elif delta == 0:
        print('Phương trình {}x^2 + {}x + {} có nghiệm kép x1 = x2 = {}'.format(a, b, c, - b / (2 * a)))
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print('Phương trình {}x^2 + {}x + {} có nghiệm')
        print('x1 = %.3f' % x1)
        print('x2 = %.3f' % x2)
