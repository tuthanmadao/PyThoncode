"""
    Cho list các số nguyên dương A. Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j]
    thỏa mãn A[i] > A[j] và i < j.
    - Đầu tiên ta sẽ so sánh A[0] với tất cả các phần tử con lại. Nếu thỏa mãn điều kiện A[i] > A[j] và i < j
    thì biến đếm tăng lên 1 đơn vị
    - Sau khi so sánh A[0] xong ta tiếp tục làm tương tự với A[1], A[2], .... , A[len(A) - 1)
    - Để làm được điều đó ta sử dụng hai lệnh for lồng nhau:
        for i in range(len(A)-1):
            for j in range(i, len(A), 1):
                if A[i] < A[j]:
                    dem += 1
"""
A = [1, 22, 10, 6, 7, 8, 10, 20, 12]
# Ta có các cặp thỏa mãn là: [22, 10], [22, 6], [22, 7], [22, 8], [22, 10], [22, 20],
# [22, 12], [10, 6], [10, 7], [10, 8], [20,12].
# có tất cả 11 cặp.

dem = 0
for i in range(len(A) - 1):
    for j in range(i, len(A), 1):
        if A[i] > A[j]:
            dem += 1
print('Có {} cặp phù hợp điều kiện A[i] > A[j] và i <j'.format(dem))
