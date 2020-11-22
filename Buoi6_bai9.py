"""
    Viết hàm đếm số lần xuất hiện các ký tự trong một String
    Ví dụ:
        Input: ‘Stringings’
        Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}
    - Ta dùng lệnh: dict_01 = {k[i]:k.count(k[i]) for i in range(len(k))}
    Tương tự với một string được nhập vào từ bàn phím.
"""
k = "Stingings"
dict_01 = {k[i]: k.count(k[i]) for i in range(len(k))}
print(dict_01)
