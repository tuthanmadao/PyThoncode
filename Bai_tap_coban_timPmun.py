"""
    Tạo một ma trận P cấp m. sau đó tính P^n
"""
import numpy as np
n = int(input("nhập vào số mũ n = "))
m = int(input("Cấp ma trận là: "))

A = np.array([np.random.randint(0, 9, m) for i in range(m)])
B = np.copy(A)

print("ma trận P =  ")
print(A)
for i in range(n-1):
    B = B.dot(A)
print(f"P^{n} = \n {B}")
