"""
    Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng
"""
so_dong = int(input("Hãy nhập số dòng mà bạn muốn đọc: "))


def read_file(n):
    """
        Đọc số dòng từ file do người dùng đặt vào.
    :param n: số dòng người dùng muốn đọc
    :return: trả lại số dòng đọc được
    """
    list_noidung = []
    with open("file_test.txt", 'r', encoding='utf-8') as f_read:
        for i in range(n):
            list_noidung.append(f_read.readline())
            pass
        return list_noidung


def print_file(n):
    """
        In ra dòng đọc được từ file_test.txt
    :param n: số dòng
    :return: ko có hàm trả về
    """
    for i in range(n):
        print(read_file(n)[i], end='')
    # print(read_file(n), end="")

print_file(so_dong)
