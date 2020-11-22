"""
    Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
    Ví dụ:
        dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
        keys = ["name", "salary"]
        Output: {'name': 'Kelly', 'salary': 8000}
    - Duyệt các phần tử trong list keys bằng for. Sau đó ta gán cho dict mới với key thuộc list keys. Value được lấy từ
    dict gốc theo các key được đề cập đến trong list keys
"""
sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
new_dict = {}
# ######################################################################################################################
# Duyệt key trong list keys.
# Tạo dict mới sử dụng key trong list key và value trong dict gốc
for pt in keys:
    new_dict[pt] = sampleDict[pt]
# In ra dict mới tạo được
print(new_dict)
