"""
   Tính tổng các số chia hết cho 3 trong khoảng (0 < i < n)
   Với n nhập vào từ bàn phím
        Ta tìm tất cả các số chia hết cho 3 rồi cộng tổng chúng lại với nhau.
        Ở trong bài ta dùng hàm for i in range(0, n, 3) trong đó bước nhảy ta chọn là 3
        khi đó các số i sẽ là các số chia hết cho 3.
"""
n = int(input('Nhập số n = '))
tong = 0
for i in range(0, n, 3):
    tong = tong + i
print('Tổng các số chia hết cho 3 là: ', tong)
"""
    Ngoài ra ta có thể viết cách khác
    tong = 0
    for i in range(n)
        if i % 3 != 0:  # Mục đích hàm if này để bỏ qua vòng khi số i không chia hết cho 3
            continue
    tong = tong + i
"""
