"""
    Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]. Viết chương trình để in ra
    hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
    - Cách 1: Ta duyệt từng phần tử. tìm từ phải qua trái dấu "." đầu tiên. sau đó ta lấy chỉ số rồi in ra phần hậu tố
    bằng phương pháp cắt dùng lệnh: print(f"hậu tố của {pt} là {pt[chiso+1:]}").
    - Cách 2: Ta cũng duyệt các phần tử như cách 1. Tuy nhiên để tìm dấu chấm ta sẽ duyệt ngược từ phần tử cuối cùng
    duyệt về đầu. gặp dấu chấm ta dừng lại. sau đó in ra hậu tố.
"""
web_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
list_c1 = []
list_c2 = []
# ######################################################################################################################
# Cách 1:
print("Cách 1: ")
for pt in web_list:
    chiso = pt.rfind(".")
    print(f"hậu tố của {pt} là {pt[chiso+1:]}")
    list_c1.append(pt[chiso+1:])
# #####################################################################################################################
# Đoạn trương trình viết ra dạng: (vn, org, net, com) với số phần từ bất kỳ
print("(", end="")
for pt in list_c1:
    print(pt, end= "")
    if pt != list_c1[-1]:
        print("", end=", ")
print(")", end="\n")
# ######################################################################################################################
# Cách 2:
print("Cách 2")
for i in range(len(web_list)):
    for j in range(-1, - len(web_list[i]) - 1, -1):
        if web_list[i][j] == ".":
            # print(f"hậu tố của {web_list[i]} là {web_list[i][- j + 1:]}")
            print(f"Hậu tố của {web_list[i]} là  {web_list[i][j + 1:]}")
            list_c2.append(web_list[i][j + 1:])
            break
# #####################################################################################################################
# Đoạn trương trình viết ra dạng: (vn, org, net, com)
print("(", end="")
for pt in list_c2:
    print(pt, end= "")
    if pt != list_c2[-1]:
        print("", end=", ")
print(")", end="\n")
