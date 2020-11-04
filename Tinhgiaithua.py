"""
    Tính giai thừa của một số n theo công thức
        n! = 1 * 2 * 3 * ... *n
    Ta dùng 3 cách tính giai thừa là
        - Dùng vòng lặp for:
            giaithua = 1
            for i in range(1, n+1):
                giaithua = giaithua * i
        - Dùng vòng lặp while:
            giaithua, i = 1, 1
            while i <= n
                giaithua = giaithua * i
                i +=1
        - Dùng hàm trong thư viện math:
            math.factorial(n)

"""
import math
n = int(input('Nhập số n = '))
giaithua = 1
# Tính giai thừa sử dụng vòng lặp for
for i in range(1, n + 1):
    giaithua = giaithua * i
giaithua1, j = 1, 1
# Tính giai thừa sử dụng vòng lặp while
while j <= n:
    giaithua1 = giaithua1 * j
    j += 1
# Tính giai thừa sử dụng hàm math
    giaithua2 = math.factorial(n)

print('Kết quả tính giai thừa của cách dùng vòng lặp for là:      ', giaithua)
print('Kết quả tính giai thừa của cách dùng vòng lặp while là:    ', giaithua1)
print('Kết quả tính giai thừa của cách dùng hàm math.factorial là:', giaithua2)
