"""
    Thực hiện code lại hàm sau và cho biết ý nghĩa của nó
def enter_data():
    while True:
        n = input("Nhập 1 số nguyên: ")
        if n.isnumeric():
            n = int(n)
            if n > 0:
                print("Đã nhập số dương")
                return n
            print("Đã nhập số không dương. Chương trình sẽ tiếp tục!")
        else:
            print("Dữ liệu đã nhập không phải số nguyên")
"""


def enter_data():
    """
    - Hàm này thực hiện nhiệm vụ nhập vào một số nguyên dương bất kỳ từ bàn phím.
    - Hoạt động:
        + hàm sẽ đọc các ký tự nhập vào từ bàn phím.
        + Nếu đó là một số nguyên dương ta trả về giá trj n
        + Nếu đó là số không dương ta bắt đầu lại. bắt người dùng nhập lại giá trị.
        + Nếu đó không phải là một số nguyên thì ta bắt người dùng nhập lại.
    - Hàm sẽ thực hiện liên tục cho đến khi ký tự nhận được là một số nguyên dương.
    :return: Trả về giá trị là một số nguyên dương.
    """
    while True:
        n = input("Nhập 1 số nguyên: ")
        if n.isnumeric():
            n = int(n)
            if n > 0:
                print("Đã nhập số dương")
                return n
            print("Đã nhập số không dương. Chương trình sẽ tiếp tục!")
        else:
            print("Dữ liệu đã nhập không phải số nguyên")


a = enter_data()
print(a)
