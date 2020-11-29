"""
    VIết hàm nhận vào một số nguyên tính vào trả lợi giá trị biểu thức n!/2^n

"""

def tinh_ham_n(n):
    giaithua = 1
    for i in range(1, n + 1, 1):
        giaithua *= i
    return giaithua / 2**n

print(tinh_ham_n(2))
print(tinh_ham_n(5))
