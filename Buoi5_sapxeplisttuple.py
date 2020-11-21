"""
    Cho 1 list chứa các tuple không rỗng. Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong
    mỗi tuple.
    - Cách 1: Sắp xếp bằng lệnh list.sort(key=sort_list). Trong đó sort_list là một hàm được khai báo như sau:
        def sort_list(elem):
            return elem[-1]
    - Cách 2: Dùng hai hàm for lồng để sắp xếp theo thứ tự mong muốn.
    Bước 1: Lấy phần tử cuối cùng của tuple đầu tiên so sánh với các phần tử cuối cùng của các tuple còn lại
    nếu nó lớn hơn thì ta đảo vị trí cho nhau.
    Bước 2: thực hiện tương tự cho đến tuple [-2] của list. Lúc này ta sẽ được list mới làm list đã được sắp xếp theo
    yêu cầu.
    lệnh:
        for i in range(len(my_list2) - 1):
            for j in range(i, len(my_list2), 1):
                if my_list2[i][-1] > my_list2[j][-1]:
                    my_list2[i], my_list2[j] = my_list2[j], my_list2[i]
"""
my_list = [(1, 2), (5, 2), (3, 6), (0, 2, 3), (2, 5, 10), (3, 3, -1), (2, 4), (-1, 2, -5)]
my_list2 = my_list.copy()
print("List gốc:")
print(my_list)
print("")
# ######################################################################################################################
# Cách 1: Sắp xếp list theo lệnh my_list.sort()
print("List sắp xếp theo cách 1 là")
def sort_list(elem):
    return elem[-1]
my_list.sort(key=sort_list)
print(my_list)
# ######################################################################################################################
# Cách 1: Sắp xếp list theo lệnh my_list.sort()
print("list sắp xếp theo cách 2 là:")
for i in range(len(my_list2) - 1):
    for j in range(i, len(my_list2), 1):
        if my_list2[i][-1] > my_list2[j][-1]:
            my_list2[i], my_list2[j] = my_list2[j], my_list2[i]
print(my_list2)
