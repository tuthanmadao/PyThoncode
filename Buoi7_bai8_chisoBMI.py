"""
    Viết hàm
        def body_mass_index(m, h)
    để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
    Công thức tính BMI = can_nang / (chieu_cao ** 2)
    Trong đó cân nặng được tính là kg
    chiều cao tính m.

"""
nguoi_a_au = input("Người Châu Á nhập CA, Người Châu Âu nhập AU ")
# Phân biệt người châu Á - Âu để dùng tiêu chuẩn tương ứng
chieu_cao = float(input("Chiều cao của bạn là: "))
can_nang = float(input("Cân nặng của bạn: "))


def body_mass_index(m, h):
    """
    để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
    Công thức tính BMI = can_nang / (chieu_cao ** 2)
    Trong đó cân nặng được tính là kg
    chiều cao tính m.
    :param m: Cân nặng (kg)
    :param h: Chiều cao (m)
    :return: Trả về giá trị BMI
   """
    return m / (h ** 2)


BMI = body_mass_index(can_nang, chieu_cao)
print(BMI)
if BMI < 18.5:
    print("Cân nặng thấp (gầy)")
elif (18.5 <= BMI <= 24.9 and nguoi_a_au == "AU") or (18.5 <= BMI <= 22.9 and nguoi_a_au == "CA"):
    print("Chỉ số BMI bình thường")
elif (25 <= BMI <= 29.9 and nguoi_a_au == "AU") or (23 <= BMI <= 24.9 and nguoi_a_au == "CA"):
    print("Bạn đang bị thừa cân")
elif (30 <= BMI <= 34.9 and nguoi_a_au == "Au") or (25 <= BMI <= 29.9 and nguoi_a_au == "CA"):
    print("Béo phì độ I")
elif (35 <= BMI <= 39.9 and nguoi_a_au == "AU") or (30 <= BMI <= 34.9 and nguoi_a_au == "CA"):
    print("Béo phì độ II")
elif (40 <= BMI and nguoi_a_au == "AU") or (35 <= BMI and nguoi_a_au == "CA"):
    print("Béo phì độ III")
