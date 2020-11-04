"""
    Lập chương trình tính tổng:
        S1 = 1 + x + x^2 + x^3 + ... + x^n
    trong đó:
        n, x là các số nhập từ bàn phím
        n là só nguyên dương
        x là một số thực bất kỳ
"""
while True:
    n = int(input('Nhập số n nguyên dương: '))
    if n > 0:
        break
x = float(input('Nhập số thực x bất kỳ: '))

# Tính tổng S1
s1 = 1
for i in range(1, n + 1):
    s1 = s1 + (x ** i)
print('Tổng S1 = ',s1)
