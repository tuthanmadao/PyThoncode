"""
    Bài 00. Viết một chương trình để lấy ra tên class của một object?
"""


class Myclass:
    """ Đây là class để thực hành các lệnh cơ bản"""
    # Thuộc tính
    thuoc_tinh = "cơ bản"

    def loi_chao(self):
        print(f" hallo!!! Xin chào các bạn.")

    def nameclass(self):
        print(f"Tên class của object là: {Myclass.__name__}")


object_basic = Myclass()
object_basic.loi_chao()
object_basic.nameclass()
