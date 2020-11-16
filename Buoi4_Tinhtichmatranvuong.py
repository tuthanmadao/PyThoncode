"""
    Viết chương trình tính tích của 2 ma trận vuông cấp 3.
    - Tích của hai ma trận vuông A B: ta lấy từng phần tử hàng của A nhân với các phần tử cột của B
    -              dòng 1, cột 1 = tổng (dòng 1 x cột 1)
                   dòng 1, cột 2 = tổng (dòng 1 x cột 2)
                   dòng 1, cột 3 = tổng (dòng 1 x cột 3)
                   ....................................................
                   dòng i, cột j = tổng (dòng i x cột j)
                   ....................................................
                   dòng m, cột n = tổng (dòng m x cột n)
"""
MT = []
MTC = []
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 2, 0]]
B = [
     [4, 5, 12],
     [0, 1, 2],
     [3, 3, 0]
     ]

for i in range(3):
     for j in range(3):
          MT.append(A[i][0]*B[0][j]+A[i][1]*B[1][j]+A[i][2]*B[2][j])
     MTC.insert(i,MT)
     MT = []
for i in range(3):
     print(MTC[i], end="\n")
