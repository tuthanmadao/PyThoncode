"""
    Viết hàm
        def count_upper_lower(str)
    trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
    - Cách 1. ta duyệt từng phần tử (pt) trong chuỗi - dùng hàm for. Sau đó ta kiểm tra xem ký tự đó nếu nó nằm trong
    khoảng "a" <= pt <= "z" thì biếm đếm pt_lower tăng 1. Nếu không ta duyệt tiếp khoảng "A" <= pt <= "Z" thì biến đếm
    pt_upper tăng 1. Còn các phần tử khác ta bỏ qua. - Các này có nhược điểm là sẽ không phân biệt được các ký tự có
    dấu như "ư", "ơ", "ố".....
    - Cách 2: Ta làm tương tự cách 1. chỉ khác ta thay các điều kiện "a" <= pt <= "z" bằng chuoi.islower(pt) và điều
     kiện "A" <= pt <= "Z" bằng chuoi.isupper(pt). - Đã khắc phục được nhược điểm của các trên
"""
chuoi_kytu = input("Nhập vào một chuỗi bất kỳ: ")


def count_upper_lower(str1):
    """
    Chú ý cách này không đếm được các ký tự có dấu: "ô", "ố"....
    Cách 1: Ta duyệt từng phần tử (pt) trong chuỗi - dùng hàm for. Sau đó ta kiểm tra xem ký tự đó nếu nó nằm trong
    khoảng "a" <= pt <= "z" thì biếm đếm pt_lower tăng 1. Nếu không ta duyệt tiếp khoảng "A" <= pt <= "Z" thì biến đếm
    pt_upper tăng 1. Còn các phần tử khác ta bỏ qua.
    :param str1: chuỗi cần đếm
    :return: trả về số lượng chữ hoa, thường.
    """
    count_upper = 0
    count_lower = 0
    for pt in str1:
        if "a" <= pt <= "z":
            count_lower += 1
        elif "A" <= pt <= "z":
            count_upper += 1
    return count_lower, count_upper


def count_upper_lower1(str1):
    """
    Chú ý: Cách này đã khắc phục được các nhược điểm của cách trên.
    - Cách 2: Ta làm tương tự cách 1. chỉ khác ta thay các điều kiện "a" <= pt <= "z" bằng chuoi.islower(pt) và
     điều kiện "A" <= pt <= "Z" bằng chuoi.isupper(pt).
    :param str1: Chuỗi cần đếm
    :return: trả về số lượng chữ hoa, thường
    """
    count_upper = 0
    count_lower = 0
    for pt in str1:
        if pt.isupper():
            count_upper += 1
        elif pt.islower():
            count_lower += 1
    return count_lower, count_upper


print(f"Cách 1: Chuỗi nhập có {count_upper_lower(chuoi_kytu)[0]} ký tự thường và {count_upper_lower(chuoi_kytu)[1]} "
      f"ký tự hoa")
print(f"Cách 2: Chuỗi nhập có {count_upper_lower1(chuoi_kytu)[0]} ký tự thường và {count_upper_lower1(chuoi_kytu)[1]}"
      f" ký tự hoa")

# Kết quả:
# Nhập vào một chuỗi bất kỳ: Hôm Nay là
# Cách 1: Chuỗi nhập có 4 ký tự thường và 2 ký tự hoa
# Cách 2: Chuỗi nhập có 6 ký tự thường và 2 ký tự hoa
# Ở đây ta thấy cách 1 đã ko đếm được các ký tự có dấu
# Cách 2 đã đếm được các ký tự có dấu.
