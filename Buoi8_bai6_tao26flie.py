"""
    Bài 06: Viết chương trình tạp ra 26 file text có tên lần lượt từ A.txt, B.txt đến Z.txt
"""
import os


def tao_file():
    """
        Hàm tạo ra 26 file có tên theo bảng chữ cái anphabet bắt đầu từ A.txt đến Z.txt
    :return: không có giá trị trả về
    """
    for item in range(65, 91, 1):
        ten_file = chr(item) + ".txt"
        with open(ten_file, 'w', encoding='utf-8'):
            pass


def xoa_file():
    """
        Xóa các file test được tạo ra trong chương trình
    :return: ko có giá trị trả về
    """
    for item in range(65, 91, 1):
        ten_file = chr(item) + ".txt"
        os.remove(ten_file)


tao_file()
# xoa_file()
