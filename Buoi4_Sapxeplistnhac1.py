"""
    Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3. Bạn cần xây
    dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại.
    - Bước 1: tìm tất cả các chỉ số có các phần tử trùng nhau gán vào list_index
        + Dùng hàm list_music.count để đếm các phần tử trong list. Nếu kết quả bằng 1 tức là chuỗi không bị trùng
        nếu kết quả lớn hơn bằng 2 ta chuyển sang ý hai
        + Lúc này ta sẽ tìm tất cả các phần tử trùng với phần tử list_music[i] và lấy chỉ số đó gán vào list_index
    - Bước 2: gán tất cả các phẩn tử có chỉ số không nằm trong list_index vào chuỗi mới
"""
list_music = [1, 2, 2, 3, 6, 7, 3, 8, 3, 5, 5, 6, 4, 7, 9, 10, 11, 12, 13, 11, 3, 10, 9, 20]
list_music_sort = []
list_index = []
# #####################################################################################################################
# Bước 1:
for i in range(len(list_music)):
    if list_music.count(list_music[i]) == 1:
        continue
    else:
        j = i + 1
        while j < len(list_music):
            if list_music[i] == list_music[j]:
                list_index.append(j)
            j += 1
# #####################################################################################################################
# Bước 2:
for i in range(len(list_music)):
    if i in list_index:
        continue
    else:
        list_music_sort.append(list_music[i])
# ####################################################################################################################

print("độ dài list nhạc là: ",len(list_music_sort))
print(list_music_sort)
