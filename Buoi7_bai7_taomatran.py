"""
    Viết hàm
        def create_matrix(n, m)
    xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j
    - Cách 1: ta dùng hai vòng lặp for để tạo ra ma trận
    - Cách 2: Viết dưới rạng comprehension
"""
hang = int(input("Hàng của ma trận: "))
cot = int(input("Cột của ma trận: "))


def create_matrix(n, m):
    """
    DUyệt hàng và cột bằng lệnh for
    tại mỗi phần tử ta dùng lệnh matrix.append(i * J)
    :param n: số hàng
    :param m: số cột
    :return: ma trận với yêu cầu đề bài
    """
    matrix = []
    hang1 = []
    for i in range(n):
        for j in range(m):
            hang1.append(i * j)
        matrix.append(hang1)
        hang1 = []
    return matrix


def create_matrix1(n, m):
    """
    Sử dụng dạng list comprehension: [[i * j for j in range(m)] for i in range(n)]
    :param n: số hàng
    :param m: số cột
    :return: ma trận cần tìm
    """
    return [[i * j for j in range(m)] for i in range(n)]


def print_matrix(matrix_in):
    """
    In ra ma trận theo hàng và cột
    :param matrix_in: ma trận cần in
    :return: dạng ma trận
    """
    for i in range(len(matrix_in)):
        print(matrix_in[i])


print("Ma trận tạo theo cách 1:")
print_matrix(create_matrix(hang, cot))
print("")
print("Ma trận tạo theo cách 2")
print_matrix(create_matrix1(hang, cot))
