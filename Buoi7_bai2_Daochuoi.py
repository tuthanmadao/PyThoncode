"""
    Viết hàm
        def reverse_string(str)
    trả lại chuỗi đảo ngược của chuỗi str
    - Cách 1: Ta duyệt chuỗi từ cuối chuỗi về đầu chuỗi - Dùng hàm for với index âm. Ta lần lượt đọc phần tử đó vào một
    biết "chuoi_dao" bằng lệnh: chuoi_dao = chuoi_dao + chuoi[pt].
    - Cách 2: Dùng kỹ thuật cắt lấy index từ đầu đến hết với bước nhảy -1 ta sẽ được chuỗi đảo ngược
    - Cách 3: Ta dùng hàm join và hàm reversed
"""
Chuoinhap = input("Nhập vào một chuỗi bất kỳ: ")


def reverse_string1(chuoi):
    """
    Đảo ngược một chuỗi str
    :param chuoi: Chuỗi cần đảo ngược
    :return: chuỗi đã được đảo ngược
    """
    chuoi_dao = ""
    for pt in range(-1, -len(chuoi) - 1, -1):
        chuoi_dao = chuoi_dao + chuoi[pt]
    return chuoi_dao


def reverse_string2(chuoi):
    """
    Đảo ngược chuỗi str bằng kỹ thuật cắt với bước nhảy âm
    :param chuoi: chuỗi cần đảo ngược
    :return: Chuỗi đã được đảo ngược
    """
    return chuoi[::-1]


def reverse_string3(chuoi):
    """
    Đảo ngược chuỗi bằng hàm join và hàm reversed()
    :param chuoi:
    :return:
    """
    chuoi_dao = ""
    return chuoi_dao.join(reversed(chuoi))


print(f"Chuỗi đảo theo cách 1: {reverse_string1(Chuoinhap)}")
print(f"Chuỗi đảo theo cách 2: {reverse_string2(Chuoinhap)}")
print(f"Chuỗi đảo theo cách 3: {reverse_string3(Chuoinhap)}")
