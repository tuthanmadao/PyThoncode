"""
    Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3. Bạn cần xây
    dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại.
    - list_music: là list id nhạc nhận được từ người dùng.
    - list_tg: là một list trung gian phục vụ cho quá trình sắp xếp mà không làm ảnh hưởng list gốc.
    - list_music_sort: là list kết quả của quá trình sắp xếp lại và loại bỏ các bài hát trùng nhau.
    - Bước 1: Ta tiến hánh chuyển list_music vào list_tg và sắp xếp theo thứ tự tăng dần.
    - Bước 2: Tiến hành loại bỏ các phần từ giống nhau bằng cách duyệt hết các phần tử.
        + Nếu phần tử đó chỉ xuất hiện 1 lần (dùng hàm list_tg.count(list_tg[i]) để kiểm tra) hoặc biến đếm có giá trị
        bằng với số lần xuất hiện của biến đó trong list - 1 (giải thích ở ý dưới) thì sẽ được gán vào list_music_sort.
        + Nếu phần tử có số lần xuất hiện trong list là >= 2 lúc này ta sẽ bỏ qua các lượt xuất hiện bằng cách sử dụng
        biến đếm. mỗi lần ta bỏ qua dem sẽ tăng lên 1 đơn vị. giả sử số lần xuất hiện bằng 2 ta sẽ có là phải bỏ qua 1
        lần. lúc này giá trị biến đếm sẽ tăng lên và bằng 1. lúc này theo điều kiện của ý 1 giá trị sẽ được gán vào
        list_music_sort
    - Bước 3: Khi đã sắp xếp được list mới ta chỉ cần dùng lệnh len(list_music_sort)
"""
list_music = [1, 2, 2, 3, 6, 7, 3, 8, 3, 5, 5, 6, 4, 7, 9, 10, 11, 12, 13, 11, 3, 10, 9, 20]
list_tg = list_music

# #####################################################################################################################
# Bước 1:
list_music_sort = []
list_tg.sort()
dem = 0

# #####################################################################################################################
# Bước 2
for i in range(len(list_tg)):
    if list_tg.count(list_tg[i]) == 1 or list_tg.count(list_tg[i]) - 1 == dem:
        list_music_sort.append(list_tg[i])
        dem = 0
    else:
        dem +=1
# #####################################################################################################################
# Bước 3:
print(list_tg)
print(list_music_sort)
print("Độ dài danh sách là: {}".format(len(list_music_sort)))

# Chuỗi list_tg và list_music_sort lần lượt là:
# [1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 9, 9, 10, 10, 11, 11, 12, 13, 20]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 20]
