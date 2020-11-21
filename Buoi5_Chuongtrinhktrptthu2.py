"""
    Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.
    - Sử dụng hàm min()
"""
my_list = [(1, 2, 3, 0), (3, 4), (12, -5), (-5, -1, 3, 4, 1)]

def min_lis(elem):
    return elem[1]
print(min(my_list, key=min_lis))
