"""
    Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng
"""
f4 = open("file_test.txt", mode="w", encoding='utf-8')
f4.write("Quy tắc đặt tên biến:\n")
f4.write("- Chỉ gồm chữ cái (a-z, A-Z) hoặc chữ số (0-9) hoặc gạch dưới (_)\n")
f4.write("- Không bắt đầu bằng chữ số\n")
f4.write("- Không được trùng với từ khóa của ngôn ngữ (bảng từ khóa)\n")
f4.write("- Độ dài tùy ý\n")
f4.close()
f5 = open("file_test1.txt", mode="w", encoding='utf-8')
f5.write("Ví dụ:\n")
f5.write("- Hợp lệ: myClass, var_1, query_set, _products, ...\n")
f5.write(" - Không hợp lệ: 1_connection, global, class, text!, bien-1...\n")
f5.close()
