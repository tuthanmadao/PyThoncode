"""
    Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một chuỗi s thành $
    - Cách 1: Dùng lệnh for kytu in range(chuoi)
        + Nếu kytu == chuoi[0] (tìm những phần tử trùng với ký tự đầu tiên của chuỗi) thì ta thay thế ký tự đó
        bằng ký tự "$".
        + Nếu kytu != chuoi[0] ta đưa kytu vào chuỗi mới.
    - Cách 2: Dùng lênh chuoi_moi = chuoi.replace(chuoi[0], "$")
"""
# Cách 1: dùng cách duyệt từng phần tử trong chuỗi
chuoi = input('Nhập một chuỗi bất kỳ: ')
chuoi_moi = ""
for kytu in chuoi:
    if kytu == chuoi[0]:
        chuoi_moi = chuoi_moi + '$'
    else:
        chuoi_moi = chuoi_moi + kytu
print('Chuỗi mới tạo là: {}'.format(chuoi_moi))

# Cách 2: Dùng lênh chuoi.replace(chuoi[0], "$")
chuoi_moi = chuoi.replace(chuoi[0], "$")
print(chuoi_moi)
