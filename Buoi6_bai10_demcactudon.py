"""
    Viết chương trình đếm số lần xuất hiện các từ đơn trong một đoạn văn bản.
    - Đọc một đoạn văn bản nhập vào từ bàn phím.
    - Phân tách đoạn văn bản thành các từ đơn lưu vào trong một list. Phân tách bằng dấu khoảng trắng " ".
    - Các từ có thể có một số từ còn bị đính dấu chấm dấu phẩy. Ta dùng lệnh for để duyệt các phần tử trong list,
    sử dụng lệnh list_tudon.strip() để xóa đi dấu chấm "." và dấu phẩy "," ở đầu hoặc cuối mỗi từ để đưa từ về dạng từ
    chỉ bao gồm các chữ cái.
    - Trong chuỗi có thể có các từ bị lặp. Nếu duyệt từ đầu đến cuối sẽ đãn đến tình trạng đếm bị lặp. Vì thế ta chuyển
    list chuỗi tách được về dạng set để loại bỏ các phần tử trùng lặp. - Nhược điểm là sẽ khiến cho thứ tự các từ bị
    thay đổi. Ta có thể dùng kết hợp giữa for và not in để lọc ra các phần tử không trùng lặp đưa vào trong list mới.
    - Sau khi xóa bỏ các phần tử trùng lặp ta bắt đầu duyệt các phần tử trong set, kiểm tra ở list cũ xem có bao nhiêu
    phần tử bằng câu lệnh list.count().
    - Ta có thể lưu kết quả vào một dict với key là các từ đơn, value là số lần lặp trong đoạn.
    - In các phần tử trong dict ra bằng vòng lặp for sẽ cho ra kết quả, hoặc in đơn thuần sẽ thể hiện từ vào số lần lặp.
"""
# Nhập đoạn văn bản
doan_van_ban = input("Nhập vào một đoạn văn: ")
dict_count_tudon = {}
dict_count_tudon1 = {}
list_tudon_loc = []

# ######################################################################################################################
# Chuyển tất cả các ký tự về chữ in thường - mục đích đồng dạng tất cả các từ có cách viết giống nhau
doan_van_ban_xuly = doan_van_ban.lower()

# ######################################################################################################################
# Tách đoạn văn ra thành các từ đơn với phân tách là khoảng trắng " ".
# Chuyển các từ đơn tách được vào một list để chuyển sang xử lý bước tiếp.
list_tudon = doan_van_ban_xuly.split(" ")

# ######################################################################################################################
# Xóa các dấu phẩy "," hoặc dấu chấm "." còn sót của bước trên bằng cách duyệt từng phần tử của list
for i in range(len(list_tudon)):
    # Xóa dấu chấm "."
    list_tudon[i] = list_tudon[i].strip(".")
    # Xóa dấu phẩy ","
    list_tudon[i] = list_tudon[i].strip(",")

# ######################################################################################################################
# Cách 1: Đưa list về dạng set để loại bỏ tất cả các phần tử (từ đơn) trùng lặp
set_tudon = set(list_tudon)
# Cách 2: Dùng kết hợp for và not in để đưa các phần tử không trùng lặp vào list mới
for pt in list_tudon:
    if pt not in list_tudon_loc:
        list_tudon_loc.append(pt)
# ######################################################################################################################
# Tìm số lần lặp của các phần tử của set trong list gốc
# Thực hiện theo cách dùng set() để lọc phần tử trùng lặp
for pt in set_tudon:
    dict_count_tudon[pt] = list_tudon.count(pt)
# Thực hiện kết hợp giữa for và not in
for pt in list_tudon_loc:
    if pt not in dict_count_tudon1:
        dict_count_tudon1[pt] = list_tudon.count(pt)

# ######################################################################################################################
# In ra kết quả:
print("(Cách dùng set) Số lượng các từ được lặp trong đoạn văn là: ")
for key in dict_count_tudon:
    print(f"từ: '{key}' lặp lại: '{dict_count_tudon[key]}' lần")
print("")
print("(Cách dùng kết hợp for và not in) Số lượng các từ được lặp trong đoạn văn là: ")
for key in dict_count_tudon1:
    print(f"từ: '{key}' lặp lại: '{dict_count_tudon1[key]}' lần")
"""
Kết quả:
    Nhập vào một đoạn văn: một con gà, hai con gà, ba con gà. Thật nhiều gà.
(Cách dùng set) Số lượng các từ được lặp trong đoạn văn là: 
    từ: 'một' lặp lại: '1' lần
    từ: 'thật' lặp lại: '1' lần
    từ: 'con' lặp lại: '3' lần
    từ: 'gà' lặp lại: '4' lần
    từ: 'hai' lặp lại: '1' lần
    từ: 'ba' lặp lại: '1' lần
    từ: 'nhiều' lặp lại: '1' lần

(Cách dùng kết hợp for và not in) Số lượng các từ được lặp trong đoạn văn là: 
    từ: 'một' lặp lại: '1' lần
    từ: 'con' lặp lại: '3' lần
    từ: 'gà' lặp lại: '4' lần
    từ: 'hai' lặp lại: '1' lần
    từ: 'ba' lặp lại: '1' lần
    từ: 'thật' lặp lại: '1' lần
    từ: 'nhiều' lặp lại: '1' lần
"""
