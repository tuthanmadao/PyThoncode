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
        Trả về tập các dòng trong các file dưới dạng list
    :param file: các file cần trả lại các dòng ký tự
    :return: trả về tập các ký tự dạng list
    """
    list_file = []
    for pt in file:
        with open(pt, 'r', encoding='utf-8') as f:
            for item in f:
                list_file.append(item)
    return list_file


def extract_characters1(*file):
    """
        Trả lại tập ký tự. Các ký tự này sẽ được sắp xếp và loại bỏ tất cả các phần tử trùng lặp
    :param file: các file
    :return: tập ký tự được lưu dạng tuple
    """
    tuple_item = ()
    for pt in file:
        with open(pt, 'r', encoding='utf-8') as f:
            for item in f:
                tuple_item = tuple_item + tuple(item)
    return tuple(sorted(set(tuple_item)))


def print_list_item(item):
    """
        in ra list các phần tử thành từng dòng.
    :param item: tập phần tử cần in
    :return: không có giá trị trả về
    """
    for pt in item:
        print(pt, end="")


def print_list_item1(item):
    """
        In ra tập các phần tử theo dòng, mỗi dòng 10 phần tử.
        các phần tử như ký tự xuống dòng đều được thể hiện thành "" các ký tự này ko phải
        ký tự hiển thị.
    :param item: đưa vào tập các phần tử
    :return: ko có dữ liệu trả về
    """
    print(item)
    dem = 0
    for pt in item:
        if dem >= 10:
            print("\n", end="")
            dem = 0
        dem += 1
        print(pt, end=", ")


# print(extract_characters(file_1, file_2))
# print_list_item(extract_characters(file_1, file_2))
print_list_item1(extract_characters1(file_1, file_2))
