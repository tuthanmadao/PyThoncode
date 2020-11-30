"""
    Bài 04: Viết hàm
        def get_file_size(file)
    để lấy và trả về dung lượng của file
"""
import os
file_check = "file_test.txt"


def get_file_size(file):
    """
        Trả về thông tin size của file
        điều kiện là file check phải cùng thư mục với chương trình.
    :param file: file cần check size
    :return: trả về thông tin size
    """
    # with open(file, 'r', encoding='utf-8') as f:
    return os.path.getsize(file)

print(f"Size file {file_check} là {get_file_size(file_check)} byte")
