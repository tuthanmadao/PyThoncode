"""
    Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list. Nếu có nhiều phần tử có cùng số lần
    xuất hiện nhiều nhất thì in ra 1 trong số chúng.
    - Ta dùng hàm for để duyệt các phần tử trong list ghi lại số lượng phần tử đó trong list vào một mảng.
    - Sau khi duyệt xong số lượng các phần tử xuất hiện, ta dùng hàm index1 = list_count.index(max(list_count))
    để tìm ra chỉ số có giá trị lớn nhất. Chỉ số này cũng chính là số thứ tự của số có chỉ số lớn nhất trong list gốc
"""
list_01 = [2, 1, 3, 5, 3, 2, 4, 4, 5, 70, 11, 23, 4, 5, 9, 8, 3, 2, 6, 8, 3]
list_count = []
# ###################################################################################################################
# Tìm số lần xuất hiện của phần tử trong list
for pt in list_01:
    list_count.append(list_01.count(pt))
# ###################################################################################################################
# Lấy chỉ số của phần tử lớn nhất đó
index1 = list_count.index(max(list_count))

# ###################################################################################################################
# In ra phần từ có lần xuất hiện nhiều nhất

print(list_01[index1])
