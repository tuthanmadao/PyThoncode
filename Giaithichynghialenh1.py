"""
    Tìm hiểu, giải thích ý nghĩa và code minh hoạ cho các hàm sau:
    s.find(sub)
    s.rfind(sub)
    s.startswith(sub)
    s.endswith(sub)
    s.replace(s1, s2)
"""
# Lệnh s.find(sub): đây là lệnh sẽ kiểm tra từ trái sang phải chuỗi s, trả về chỉ số của ký tự đầu tiên
# giống với chuỗi "sub"

s = "Toi hoc lap trinh Python tai trung tam Plusplus"
print(s.find("hoc"))

# Lúc này kết quả sẽ được trả lại là:
# 4 - đây là chỉ số của chuỗi "học"


# Lênh s.rfind(sub): Lênh sẽ quét từ phải qua trái chuỗi s. Kết quả trả về sẽ là chỉ số của ký tự đầu tiên
# Giống với chuỗi "sub"

print(s.rfind("ta"))

# ở đây ta có thể thấy có hai vị trí giống với chuỗi "ta" là "ta" tại vị trí có chỉ số 25 ("tai"), và tại vị
# trí có chỉ số 35 là ("tam"). Tuy nhiên, vị trí lệnh nhận được đầu tiên khi quét từ phải qua trái là vị trí
# 35 ("tam") là vị trí lệnh đọc tháy trước. Kết quả trả về là:
# 35


# Lệnh s.startswith(sub): Lệnh này sẽ kiểm tra xem chuỗi "sub" có được bắt đầu bằng chuỗi "sub" hay không
# - Kết quả là True nếu chuỗi "s" được bắt đầu bằng chuỗi "sub"
# - Kết quả là False nếu chuỗi "s" không được bắt đầu bằng chuỗi "sub"

print(s.startswith("Toi"))
print(s.startswith("Ban"))

# Như trên ví dụ chuỗi "s" có bắt đầu bằng chuỗi "Toi" vậy lên câu lệnh trên sẽ cho kết quả là True.
# Còn câu lệnh dưới sẽ có kết quả là False


# Lệnh s.endswith(sub): Lệnh sẽ kiểm tra chuỗi "s" có kết thúc cho phải là chuỗi "sub" hay không.
# - Kết quả là True nếu kết thúc là chuỗi "sub"
# - Kết quả là False nếu kết thúc không phải là chuỗi "sub"

print(s.endswith("lus"))
print(s.endswith("Lus"))

# ở đây kết quả sẽ là True vì chuỗi "s" của chúng ta có kết thúc là "lus"
# Câu lệnh dưới sẽ ra kết quả là False. Tuy cũng là "Lus" tuy nhiên chữ "L" viết hoa
# Python có phân biệt hoa thường


# Câu lệnh s.replace(s1, s2): Câu lệnh này sẽ thay thế các chuỗi nằm trong "s" giống với chuỗi "s1" bằng
# Chuối "s2"

print(s.replace("Toi", "Ban"))

# Lúc này lệnh sẽ thay thế tất cả các chuỗi "Toi" bằng chuỗi "Ban"
# Kết quả:
# Chuỗi cũ:"Toi hoc lap trinh Python tai trung tam Plusplus"
# Chuỗi mới:"Ban hoc lap trinh Python tai trung tam Plusplus"
