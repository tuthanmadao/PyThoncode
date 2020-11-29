"""
    Viết hàm
        def change_upper_lower(str)
    chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
"""

chuoi = (input('Nhập vào một chuỗi bất kỳ: '))


def change_upper_lower(chuoi1):
    """
    - Để chuyển được các ký tự thường sang ký tự hoa và ngược lại ta cần duyệt từng phần tử trong chuỗi:
        + Nếu ký tự đó là in hoa (if 'A' <= chuoi[i] <= 'Z':), ta dùng lệnh chuoi[i].lower() để đưa về ký tự in thường
        + Nếu ký tự đó là in thường (elif 'a' <= chuoi[i] <= 'z':), ta dùng lệnh chuoi[i].upper() để chuyển về in Hoa
        + Nếu là các ký tự khác ta ghi vào chuỗi mới
    :param chuoi1: Chuỗi cần chuyển đổi hoa thường
    :return: cho ra kết quả chuỗi đã chuyển đổn
    """
    chuoi_moi = ''
    for i in range(len(chuoi1)):
        if 'A' <= chuoi1[i] <= 'Z':
            chuoi_moi = chuoi_moi + chuoi1[i].lower()
        elif 'a' <= chuoi1[i] <= 'z':
            chuoi_moi = chuoi_moi + chuoi1[i].upper()
        else:
            chuoi_moi = chuoi_moi + chuoi1[i]
    return chuoi_moi


print('Chuỗi mới được biến đổi: {}'.format(change_upper_lower(chuoi)))
