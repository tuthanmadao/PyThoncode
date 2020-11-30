"""
    Bài 03: Viết chương trình trộn 2 file thành file mới
"""
file_1 = "file_test.txt"
file_2 = "file_test1.txt"
file_3 = "file_tron.txt"


def read_file(name):
    """
        Đọc nội dung file
    :param name: tên file cần đọc
    :return: trả về nội dung của file
    """
    with open(name, 'r', encoding='utf-8') as f:
        return f.readlines()


def write_file(name, noidung):
    """
        Ghi nội dung cần vào trong file name
    :param name: file cần ghi nội dung
    :param noidung: nội dung cần ghi thêm
    :return: không có giá trị trả về
    """
    with open(name, 'a', encoding='utf-8') as f:
        for line in noidung:
            f.write(line)
        pass


def tron_file(name1, name2, name):
    """
        Đọc nội dung của file name1, file name2. Sau đó ghi cả hai nội dung vào file3
    :param name1: file 1
    :param name2: file 2
    :param name: file trộn
    :return: không có giá trị trả về.
    """
    write_file(name, read_file(name1))
    write_file(name, read_file(name2))


tron_file(file_1, file_2, file_3)
with open(file_3, 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

# ######################################################################################################################
# Đoạn chương trình xóa nội dung file 3 để tránh lặp nội dung sau mỗi lần test.
with open(file_3, 'w', encoding='utf-8') as f:
    f.write('')
    pass

