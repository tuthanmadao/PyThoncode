"""
    Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
    - Trường hợp 1: Chỉ tính đến các key có trong cả hai dict. Sử dụng nhanh toán tử in để tìm kiếm
    - Trường hợp 2: Cả cặp key - value đều phải có trong hai dict
    - Trong bài này ta cần đó là trường hợp 2.
"""
dict_01 = {
    1: "ga",
    2: 3.14,
    3: "vịt bầu"
}
dict_02 = {
    1: "ga",
    4: "bòng",
    2: "bưởi"
}
# ######################################################################################################################
# Trường hợp 1:
print("Các trường hợp có key xuất hiện trong cả hai dict")
for pt in dict_01:
    if pt in dict_02:
        print(f"{pt}:{dict_01[pt]}")
# ######################################################################################################################
# Trường hợp 2: cặp key-value phải xuất hiện trong cả hai dict
print("Các trường hợp có cặp key-value xuất hiện đông thời trong cả hai dict")
for pt in dict_01:
    if (pt in dict_02) and (dict_01[pt] == dict_02[pt]):
        print(f"{pt}:{dict_01[pt]}")
