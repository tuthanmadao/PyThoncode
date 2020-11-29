"""
    Viết hàm
        def is_perfect(n)
    để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
    Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi
"""
so_bat_ky = int(input("Bạn muốn kiểm tra số nào: "))


def is_perfect(n):
    """
    Đây là chương trình kiểm tra xem một số có phải là số hoàn hảo hay ko bằng cách:
    Lấy tất cả các ước số thực sự của n (đây là các ước số nhỏ hơn n) cộng lại. Nếu tổng số các ước thực sự có giá trị
    bằng n thì n là số hoàn hảo. Nếu không bằng thì không phải là số hoàn hảo.
    :param n: số cần kiểm tra
    :return: True nếu số là số hoàn hảo, False nếu số không phải là số hoàn hảo.
    """
    tong_cac_uoc = 0
    for i in range(1, n, 1):
        if n % i == 0:
            tong_cac_uoc += i
    if tong_cac_uoc == n:
        return True
    else:
        return False


if is_perfect(so_bat_ky):
    print(f"Số {so_bat_ky} là số hoàn hảo")
else:
    print(f"Số {so_bat_ky} không phải là số hoàn hảo")
