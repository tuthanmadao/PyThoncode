"""
    Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng
"""
ten_file = "file_test.txt"
so_dong = int(input("Hãy nhập số dòng mà bạn muốn đọc: "))


def read_file(n, file):
    """
        Đọc số dòng từ file do người dùng đặt vào.
    :param n: số dòng người dùng muốn đọc
    :param file: tên file cần đọc
    :return: trả lại số dòng đọc được
    """
    list_noidung = []
    with open(file, 'r', encoding='utf-8') as f_read:
        for i in range(n):
            list_noidung.append(f_read.readline())
            pass
        return list_noidung


def print_file(n, file):
    """
        In ra dòng đọc được từ file_test.txt
    :param n: số dòng
    :param file: tên file cần in
    :return: ko có hàm trả về
    """
    for i in range(n):
        print(read_file(n, file)[i], end='')
    # print(read_file(n), end="")


print_file(so_dong, ten_file)
