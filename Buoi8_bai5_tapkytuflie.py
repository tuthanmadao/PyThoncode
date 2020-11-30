"""
    Bài 05: Viết hàm
        def extract_characters(*file)
    trả lại tập các ký tự trong các file
"""
file_1 = "file_test.txt"
file_2 = "file_test1.txt"
file_3 = "file_tron.txt"


def extract_characters(*file):
    """
        Trả về tập các ký tự trong các file dưới dạng list
    :param file: các file cần trả lại tập ký tự
    :return: trả về tập các ký tự dạng list
    """
    list_file = []
    for pt in file:
        with open(pt, 'r', encoding='utf-8') as f:
            for item in f:
                list_file.append(item)
    return list_file


def print_list_item(item):
    """
        in ra list các phần tử thành từng dòng.
    :param item: tập phần tử cần in
    :return: không có giá trị trả về
    """
    for pt in item:
        print(pt, end="")



print(extract_characters(file_1, file_2))
print_list_item(extract_characters(file_1, file_2))
