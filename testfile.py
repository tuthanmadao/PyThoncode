# class Fraction:
#     def __init__(self, tu=0, mau=0):
#         self.tu_so = tu
#         self.mau = mau
#         self.gia_tri = tu / mau
#
#     def show(self):
#         print(f"Phân số: {self.tu_so}/{self.mau} = {self.gia_tri}")
#
#
# Phan_so = Fraction(2, 5)
# Phan_so.show()
#
# Phan_so = Fraction(5, 9)
# Phan_so.show()
list_test = ['hahahaha']
tuple_goc = tuple('hdhdhdhdhd')
for i in range(3):
    tuple_goc = tuple_goc + tuple(list_test[0])
print(tuple_goc)
