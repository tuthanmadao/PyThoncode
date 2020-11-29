"""
    Viết chương trình xuất ra màn hình hình vuông đặc kí tự "*" có cạnh bằng a (với a nhập từ bàn phím).
"""
a = int(input("Nhập vào cạnh hình vuông: "))
for i in range(a):
    for j in range(a):
        if i == 0 or i == a - 1:
            print("* " * a, end="")
            break
        elif j == 0 or j == a - 1:
            print("* ", end="")
        else:
            print(" ", end=" ")
    print("", end="\n")

# Kết quả:
"""
Nhập vào cạnh hình vuông: 10
*  *  *  *  *  *  *  *  *  *  
*                          *  
*                          *  
*                          *  
*                          *  
*                          *  
*                          *  
*                          *  
*                          *  
*  *  *  *  *  *  *  *  *  *  
"""