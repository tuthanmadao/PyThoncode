"""
    Lập chương trình tính tổng:
        S2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
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

# Tính tổng S2
s2 = 1
for i in range(1, n + 1):
    s2 = s2 + ((-1) ** i) * (x ** i)
print(s2)
