"""
    Viết chương trình kiểm tra 2 list có phần tử chung hay không.
    - Giả sử ta có list A và list B.
    - Cách 1: Để kiểm tra xem phần tử của list A có trong list B hay không ta lấy từng phần tử trong A so sánh với các
    phần tử của List B. Nếu có phép toán bằng nhau tức là A có phần tử chung với B
    - Cách 2: Ta cũng sẽ duyệt từng phần tử của A tuy nhiên ta sẽ dùng lệnh in để kiểm tra. Nếu có kết quả là True thì
    hai list có phần tử chung. còn không thì hai list này ko có phần tử chung.
"""
A = [1, 2, 5, 2, 11, "cà chua", "bắp cải", 3.14, -270, "gas"]
B = [0, 3, 6, 7, 11, "cà Chua", "rau muốn", "cải bắp", "3.14"]
thoat = False

# ######################################################################################################################
# Cách 1:
for pta in A:
    for ptb in B:
        if pta == ptb:
            thoat = True
            break
    if thoat:
        break
if thoat:
    print("kiểm tra theo cách một có kết quả hai list có phần tử chung")
else:
    print("kiểm tra theo cách 1 kết quả là không có phần tử chung")

# ######################################################################################################################
# Cách 2
kt = False
for pt in A:
    if pt in B:
        kt = True
        print("Hai chuỗi có phần tử chung")
        break

if not kt:
    print("Hai chuỗi không có phẩn tử chung")
