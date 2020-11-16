"""
    Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
    - Duyệt từng chuỗi thuộc list sử dụng hàm for kytu in list_chuoi
    - lọc ra các ký tự phù hợp với điều kiện của đề bài bằng hàm if len(kytu) >= 2 and kytu[0] == kytu[-1]
    - Khi có các biến phù hợp ta tăng biến đếm lên 1.
    - Ngoài ra ta có thể lưu lại các chuỗi phù hợp với điều kiện vào một list, sau đó in ra để kiểm nghiệm kết quả.
"""
list_chuoi = ["1", "123", "mam", "121212121", "444", "12345", "plusplus", "Python"]
dem = 0
list_chuoi_dung = []
for kytu in list_chuoi:
    if len(kytu) >= 2 and kytu[0] == kytu[-1]:
        dem += 1
        list_chuoi_dung.append(kytu)
print("Số các chuỗi phù hợp điều kiện là: ",dem)
print("Các phần tử đó là:")
print(list_chuoi_dung)
