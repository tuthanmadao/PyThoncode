"""
    Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
    - Để chuyển được các ký tự thường sang ký tự hoa và ngược lại ta cần duyệt từng phần tử trong chuỗi:
        + Nếu ký tự đó là in hoa (if 'A' <= chuoi[i] <= 'Z':), ta dùng lệnh chuoi[i].lower() để đưa về ký tự in thường
        + Nếu ký tự đó là in thường (elif 'a' <= chuoi[i] <= 'z':), ta dùng lệnh chuoi[i].upper() để chuyển về in Hoa
        + Nếu là các ký tự khác ta ghi vào chuỗi mới
"""
chuoi = (input('Nhập vào một chuỗi bất kỳ: '))
chuoi_moi = ''
for i in range(len(chuoi)):
    if 'A' <= chuoi[i] <= 'Z':
        chuoi_moi = chuoi_moi + chuoi[i].lower()
    elif 'a' <= chuoi[i] <= 'z':
        chuoi_moi = chuoi_moi + chuoi[i].upper()
    else:
        chuoi_moi = chuoi_moi + chuoi[i]
print('Chuỗi mới được biến đổi: {}'.format(chuoi_moi))
