"""
    Tìm hiểu, giải thích ý nghĩa và code minh họa cho các hàm phổ biến của String sau:
        s.upper()
        s.lower()
        s.title()
        s.strip()
        s.lstrip()
        s.rstrip()
        s.count(sub)
"""

# Cho chuối s như sau:
s = "    toi hoc lap trinh PYTHON Tai trUng taM PlusPlus    "

# ######################################################################
# Lệnh s.upper(): lênh này sẽ chuyển các ký tự của chuối "s" thành in hoa

print(s.upper())

# Kết quả lúc này sẽ là:
# "   TOI HOC LAP TRINH PYTHON TAI TRUNG TAM PLUSPLUS    "

# ######################################################################
# Lệnh s.lower(): lệnh này sẽ chuyển các ký tự trong chuỗi "s" về in thường

print(s.lower())

# Kết quả sẽ là:
# Chuỗi chưa đổi là:"    toi hoc lap trinh PYTHON Tai trUng taM PlusPlus    "
# Chuỗi sau khi đổi:"    toi hoc lap trinh python tai trung tam plusplus    "

# ######################################################################
# Lênh s.title(): Lệnh này sẽ viết đầu tất cả các chữ cái đầu của các từ trong một chuỗi
# hoặc đầu các đoạn ký tự được phân tách nhau bằng dấu cách. Đồng thời chuyển các ký tự còn lại
# của từ hoặc đoạn ký tự thành in thường

print(s.title())

# Kết quả cho ra là:
# Chuỗi cũ: "    toi hoc lap trinh PYTHON Tai trUng taM PlusPlus    "
# Chuỗi mới:"    Toi Hoc Lap Trinh Python Tai Trung Tam Plusplus    "

# ######################################################################
# Lệnhs.strip(): Lênh này sẽ xóa khoảng trắng ở đầu và cuối chuỗi "s"

print(s.strip())

# Kết quả:
# Chuỗi cũ :"    toi hoc lap trinh PYTHON Tai trUng taM PlusPlus    "
# Chuỗi mới:"toi hoc lap trinh PYTHON Tai trUng taM PlusPlus"

# #####################################################################
# Lệnh s.lstrip(): Xóa khoảng trắng ở đầu chuỗi "s".

print(s.lstrip())

# Kết quả là:
# Chuỗi cũ :"    toi hoc lap trinh PYTHON Tai trUng taM PlusPlus    "
# Chuỗi mới:"toi hoc lap trinh PYTHON Tai trUng taM PlusPlus    "

# #####################################################################
# Lệnh s.rstrip(): Lênh xóa khoảng trắng ở cuối chuỗi "s"

print(s.rstrip())

# Kết quả là:
# Chuối cũ :"    toi hoc lap trinh PYTHON Tai trUng taM PlusPlus    "
# Chuỗi mới:"    toi hoc lap trinh PYTHON Tai trUng taM PlusPlus"


# ####################################################################
# Lệnh s.count(sub): đếm trong chuỗi "s" có bao nhiêu ký tự/chuỗi "sub"

print(s.count("lus"))

# Kết quả:
# Trong chuỗi "s" ký tự/ chuỗi "lus" xuất hiện hai lần tại vị trí Plusplus. Vậy nên đáp án sẽ là:
# 2
