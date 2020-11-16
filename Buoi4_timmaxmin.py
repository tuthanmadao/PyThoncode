"""
    Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.
    - Dùng hàm for để duyệt các phần tử: nếu gt_max < A[i] thì gt_max = A[i]
    tương tự với gt_min. nếu gt_min > A[i] thì gt_min = A[i]
    - Dùng hàm max(), min() để tìm nhanh giá trị max, min
"""
A = [1, 20, -4, -10, 26, 11, 30, 6, 3, -2]

# #################################################################################
# tìm giá trị max, min dùng hàm for
gt_max = gt_min = A[0]
for pt in A:
    if gt_max < pt:
        gt_max = pt
    if gt_min >pt:
        gt_min = pt
print("Giá trị max = {}, giá trị min = {}".format(gt_max,gt_min))

# ##################################################################################
# Tìm giá trị max, min dùng hàm max, min
gt_max1 = max(A)
gt_min1 = min(A)

print("Giá trị max = {}, giá trị min = {}".format(gt_max1,gt_min1))
