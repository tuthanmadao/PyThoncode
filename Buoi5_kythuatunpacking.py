"""
    Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau. Sau đó, unpack các phần tử trong
    một tuple.

"""
A = []
index_pt = 0
thu = "-3d14"
print("Nhập vào các phần tử của Tuple - nhập 'esc' để thoát nhập")
# while True:
#     kytu = input(f"A[{index_pt}] = ")
#     if kytu.isdigit() and kytu != "esc":
#         A.append(int(kytu))
#         index_pt += 1
#     elif kytu == "esc":
#         break
#     else:
#         A.append(kytu)
#         index_pt += 1
# print(A)
for i in range(4):
    kytu = input(f"A[{i}]")
    if kytu.isdigit():
        A.append(int(kytu))
    elif kytu.isalnum():
        A.append(kytu)
    elif kytu[0] == "-" and kytu[0:].isdigit():
        A.append(int(kytu))
    elif
print(thu.isalnum())
