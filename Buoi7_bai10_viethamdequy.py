"""
    Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
    Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
"""
m = 1234567890


def dem_so_le(n):
    """
    Hàm sẽ ktra xem n có phải là số lẻ hay ko? nếu đúng thì trả lại giá trị 1 + dem_so_le(n//10)
    giả sử n = 123
    vòng đầu tiên 123 là số lẻ ta sẽ trả lại giá trị 1 + dem_so_le(n//10). n//10 = 12
    vòng tiếp theo lúc này n = 12 là số chẵn ta trả lại 0 + dem_so_le(n//10). n//10 = 1
    vòng tiếp theo n = 1 là số lẻ ta có giá trị trả lại 1 + dem_so_le(n//10). n//10 = 0
    Vòng tiếp theo n = 0 thì lúc này ta đặt lệnh kiểm tra if n <= 0: return 0
    kết quả ta được 1 + 0 + 1 + 0 = 2. Hai số lẻ
    :param n: số cần đếm
    :return: 0 hoặc 1 + dem_so_le(n//10)
    """
    if n <= 0:
        return 0
    else:
        if n % 2 != 0:
            return 1 + dem_so_le(n//10)
        else:
            return 0 + dem_so_le(n//10)


print(f"Số {m} có {dem_so_le(m)} số lẻ. ")
