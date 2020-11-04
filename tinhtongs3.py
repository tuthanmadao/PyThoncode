"""
    Lập chương trình tính tổng:
        S3 = 1 + x/1! + x^2/2! + ... + x^n/n!
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

# Tính tổng S3
giaithua, s3 = 1, 1
for i in range(1, n + 1):
    giaithua = giaithua * i
    s3 = s3 + x ** i / giaithua
print('Tổng S3 = %.4f' % s3)
