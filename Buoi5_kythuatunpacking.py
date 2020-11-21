"""
    Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau. Sau đó, unpack các phần tử trong
    một tuple.
"""
A = []
index_pt = 0
print("Nhập vào các phần tử của Tuple - nhập 'esc' để thoát nhập")

# ######################################################################################################################
# Nhập 4 phần tử từ bàn phím. sau đó phân loại và được gán vào trong một list
for i in range(4):
    kytu = input(f"A[{i}] = ")
    if kytu.isdigit() or (kytu[0] == "-" and kytu[1:].isdigit()):
        # Kiểm tra xem đây có phải số nguyên hay ko?
        # Nếu đúng gán vào list A với định dạng int(kytu)
        A.append(int(kytu))
    elif kytu.count(".") == 1 and kytu[0:kytu.find(".")].isdigit() and kytu[kytu.find(".") + 1:].isdigit():
        # Kiểm tra xem đây có phải số thực dương hay không?
        # Nếu đúng gán vào list A với định dạng là float(kytu)
        A.append(float(kytu))
    elif kytu[0] == "-" and kytu.count(".") == 1 and kytu[1:kytu.find(".")].isdigit() and \
            kytu[kytu.find(".") + 1:].isdigit():
        # Kiểm tra xem đây có phải số thực âm hay không?
        # Nếu đúng gán vào list A với định dạng là float(kytu)
        A.append(float(kytu))
    elif kytu[0] == "[" and kytu[-1] == "]":
        # Kiểm tra xem đây có phải là 1 list hay không?
        # Nếu đúng ta gán vào trong list dưới dạng list đã phân tách các phần tử dựa trên dấu phẩy
        A.append(kytu[1:-1].split(", "))
    elif kytu[0] == "(" and kytu[-1] == ")":
        # Kiểm tra xem đây có phải là 1 Tuple hay không?
        # Nếu đúng ta gán vào trong list dưới dạng tuple đã phân tách các phần tử dựa trên dấu phẩy
        A.append(tuple(kytu[1:-1].split(", ")))
    else:
        A.append(kytu)
# Đổi từ list sang Tuple
A = tuple(A)
print(f"Tuple nhận được là: {A}")
# Unpacking
print("Unpacking:")
a, b, c, d = A
print(a)
print(b)
print("end", c, d)
