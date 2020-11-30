"""
    Bài 02: Viết chương trình thêm một chuỗi nào đó vào cuối file
"""
str_add = "Ngôn Ngữ lập trình Python\n"
file_name = "file_test.txt"


def read_file(name):
    """
        Đọc nội dung của file
    :param name: tên file cần đọc
    :return: ko có giá trị trả về.
    """
    with open(name, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


def write_file(str_add1, name):
    """
        Ghi một chuối vào file có tên chứa trong name
    :param str_add1: chuỗi cần add
    :param name: tên file
    :return: không có giá trị trả về
    """
    with open(name, 'a', encoding='utf-8') as f:
        f.write(str_add1)
        pass


write_file(str_add, file_name)
read_file(file_name)
