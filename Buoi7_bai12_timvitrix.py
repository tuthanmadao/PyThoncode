"""
    Viết hàm
        def find_x(a_list, x)
    trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1
"""
a_list = [1, "1", 2, 3, 4, 1, "1", 4, "banana", "Banana", "apple", "xoai"]
ky_tu = 1

def find_x(list1, x):
    """
        Tìm vị trí các phần thử giống x, ta dùng vòng lặp for để duyệt. Duyệt từng phần tử trong list, nếu:
            + phần tử giống x ta append vị trí i của phần tử dó vào một list
            + nếu không giống ta chuyển sang phần tử tiếp
        sau khi duyệt xong ta tìm độ dài của list vừa tìm được. Nếu:
            + Độ dài bằng 0 ta đẩy ra giá trị -1
            + ĐỘ dài khác 0 ta đẩy ra list vừa tìm được
    :param list1: list chứa các giá trị
    :param x: phần tử cần tìm trong list
    :return: giá trị của các phần tử giống x. nếu ko có pt trùng thì return -1
    """
    list_a = []
    for i in range(len(list1)):
        if list1[i] == x:
            list_a.append(i)
    if len(list_a) != 0:
        return list_a
    else:
        return -1


def find_x1(list1, x):
    """
    Sử dụng hàm lambda, filter
    - hàm filter(lambda i: list[i] == x, range(len(list1))). trong đó i là giá trị vị trí của x được quy định bởi điều
    kiện list1[i] == 1. Và biến i sẽ chạy trong khoảng range(len(list1)) chạy từ 0 đến độ dài của list1.
    - Hàm if len(list(filter(lambda i: list1[i] == x, range(len(list1))))) != 0:
    đây là hàm kiểm tra xem list trả về có phải là hàm rỗng hay không?
        + Nếu có thì ta trả về list
        + Nếu không trả về giá trị -1
    :param list1: list chứa các phần tử cần so sánh
    :param x: phần tử cần tìm trong list
    :return: giá trị của các phần tử giống x. nếu ko có pt trùng thì return -1
    """
    if len(list(filter(lambda i: list1[i] == x, range(len(list1))))) != 0:
        return list(filter(lambda i: list1[i] == x, range(len(list1))))
    else:
        return -1


print(f"Cách 1: các vị trí xuất hiện phần tử {ky_tu} là {find_x(a_list, ky_tu)}")
print(f"Cách 2: các vị trí xuất hiện phần tử {ky_tu} là {find_x1(a_list, ky_tu)}")
