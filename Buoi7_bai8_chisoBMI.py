"""
    Viết hàm
        def body_mass_index(m, h)
    để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
    Công thức tính BMI = can_nang / (chieu_cao ** 2)
    Trong đó cân nặng được tính là kg
    chiều cao tính m.

"""
nguoi_a_au1 = input("Người Châu Á nhập CA, Người Châu Âu nhập AU ")
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


def bmi_informstion(m, h, nguoi_a_au):
    """
    - Gọi hàm body_mass_index(m, h) để tính ra tham số bmi. Sau đó dựa trên các tiêu chuẩn của thông số bmi ta phân
    loại ra các mức độ gầy béo của một người dựa trên chiều cao (h), và cân nặng (m) của người đó.
    :param m: Chỉ số cân nặng
    :param h: Chỉ số chiều cao
    :param nguoi_a_au: Tham số chỉ người châu Á và châu Âu để xếp loại cho đúng
    :return: không có giá trị trả về
    """
    bmi = body_mass_index(m, h)
    print("Chỉ số BMI của quí khách là %.2f" %bmi)
    if bmi < 18.5:
        print("Cân nặng thấp (gầy)")
    elif (18.5 <= bmi <= 24.9 and nguoi_a_au == "AU") or (18.5 <= bmi <= 22.9 and nguoi_a_au == "CA"):
        print("Chỉ số BMI bình thường")
    elif (25 <= bmi <= 29.9 and nguoi_a_au == "AU") or (23 <= bmi <= 24.9 and nguoi_a_au == "CA"):
        print("Bạn đang bị thừa cân")
    elif (30 <= bmi <= 34.9 and nguoi_a_au == "Au") or (25 <= bmi <= 29.9 and nguoi_a_au == "CA"):
        print("Béo phì độ I")
    elif (35 <= bmi <= 39.9 and nguoi_a_au == "AU") or (30 <= bmi <= 34.9 and nguoi_a_au == "CA"):
        print("Béo phì độ II")
    elif (40 <= bmi and nguoi_a_au == "AU") or (35 <= bmi and nguoi_a_au == "CA"):
        print("Béo phì độ III")


bmi_informstion(can_nang, chieu_cao, nguoi_a_au1)
