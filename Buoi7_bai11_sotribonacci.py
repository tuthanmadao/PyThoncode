"""
    Cho dãy số Tribonacci với công thức truy hồi sau:
            F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
    Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
        + Hàm Đệ quy
        + Hàm Không đệ quy

"""
so_tribonacci = int(input("Bạn muốn tính số Tribonacci thứ: "))


def tribonacci(n):
    """
    Nhược điểm tính siêu lâu, tốn tài nguyên.
    Ta dùng công thức F(n) = F(n-1) + F(n-2) + F(n-3) để gọi hàm đệ quy tính số Tribonacci
    :param n: số Tribonaci thứ n
    :return: đưa ra được giá trị số tribonacci
    """
    if n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


def tribonacc1_thuong(n):
    """
    Cách này dùng vòng lặp for và thự hiện tính lần lượt các số tribonacci từ thứ 1 cho đến thứ n. tất cả các giá trị
    tìm được sẽ được dùng để tính cho số sau. Ưu điểm là hiệu suất cao. Nhanh hơn so với hàm hồi qui
    :param n: số triboracci thứ n
    :return: giá trị số triboracci
    """
    tribo = 0
    tri1 = 1
    tri2 = 1
    tri3 = 2
    if n <= 2:
        return 1
    elif n == 3:
        return 2
    else:
        for i in range(4, n+1, 1):
            tribo = tri1 + tri2 + tri3
            tri1, tri2, tri3 = tri2, tri3, tribo
    return tribo


print(f"Cách 1: Số Tribonacci thứ {so_tribonacci} có giá trị là: {tribonacci(so_tribonacci)}")
print(f"Cách 2: Số Tribonacci thứ {so_tribonacci} có giá trị là: {tribonacc1_thuong(so_tribonacci)}")
