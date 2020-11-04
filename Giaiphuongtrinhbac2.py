"""
    Viết chương trình giải phương trình ax^2 + bx + c = 0 (Kể cả a = 0)
    trong đó: a, b, c là các số nhập từ bàn phím.
    - với trường hợp a khác 0
        + Ta tính delta = b^2 - 4ac
            nếu delta < 0 phương trình vô nghiệm
            nếu delta = 0 phương trình có nghiệm kép x1 = x2 = - b / (2a)
            nếu delta > 0 phương trình có hai nghiệm
                x1 = (- b + sqrt(delta))/2a
                x2 = (- b - sqrt(delta))/2a
    - Với trường hợp a = 0 lúc đó phương trình sẽ thành phương trình bậc nhất bx + c = 0
        + Ta có nghiệm x = - c / b
"""
import math
a = float(input('Nhập số a = '))
b = float(input('Nhập số b = '))
c = float(input('Nhập số c = '))
if a != 0:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('Phương trình {}x^2 + {}x + {} vô nghiệm.'.format(a, b, c))
    elif delta == 0:
        print('Phương trình {}x^2 + {}x + {} có nghiệm kép x1 = x2 = {}'.format(a, b, c, - b / (2 * a)))
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print('Phương trình {}x^2 + {}x + {} có nghiệm')
        print('x1 = %.3f' % x1)
        print('x2 = %.3f' % x2)
else:
    print('Phương trình {}x + {} có nghiệm là x = {}'.format(b, c, - c / b))
