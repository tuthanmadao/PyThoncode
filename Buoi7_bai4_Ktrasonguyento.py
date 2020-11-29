"""
    Viết hàm
        def is_prime(n)
    để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
"""
so_ktra = int(input("Nhập số cần kiểm tra: "))


def is_prime(n):
    """
    Số nguyên tố là số lớn hơn 0 và chỉ chia hết cho 1 và chính nó.
    - Để kiểm tra số n có phải là số nguyên tố hay ko? ta kiểm tra só i thuộc khoảng (1, n) - tức là 1 < i < n
        + nếu như n không chia hết cho bất cứ số i nào thì đó là số nguyên tố. kết quả trả là True
        + Nếu có một số i bất kỳ thỏa mãn điều kiện n % i == 0 thì số đó ko phải số nguyên tố. Kết quả trả lại là False
    :param n: Số cần kiểm tra
    :return: True với n là số nguyên tố, False với n ko phải số nguyên tố
    """
    kt = True
    if n > 1:
        for i in range(2, n, 1):
            if n % i == 0:
                kt = False
                break
    else:
        kt = False
    return kt


if is_prime(so_ktra):
    print(f"Số {so_ktra} là số nguyên tố")
else:
    print(f"Số {so_ktra} không phải là số nguyên tố")
