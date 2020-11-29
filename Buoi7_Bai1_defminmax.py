"""
    Bài 01: Viết hàm
        def max_min(*numbers)
    trả lại cả giá trị max, min của nhiều số được truyền vào
"""
list_so = []


def max_min_1(*numbers):
    """
    Hàm dùng để tìm ra min, max của một dãy các chữ số được truyền vào hàm
    Ở dây dùng hàm max(), và min() để nhanh chóng tìm ra giá trị lớn nhất nhỏ nhất.
    :param numbers: các số
    :return: giá trị max, min
    """
    return max(numbers), min(numbers)



print(f"max = {max_min_1(1, 2, 3, 4, 5.6, 5.7)[0]}, min = {max_min_1(1, 2, 3, 4, 5.6, 5.7)[1]}")
