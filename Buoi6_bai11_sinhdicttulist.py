"""
    Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
    Ví dụ:
        Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
        Output: {'item1': 1150, 'item2': 300}
    - Ý tưởng của bài đó là đưa tất cả các đối tượng về một dict mới trong đó key của dict là các "item" và value là
    các "amount" của key đó.
    - Để làm được đầu tiên ta lọc ra các phần tử item lưu vào một list. Dùng kết hợp for và not in với duyệt phần tử có
    key 'item'. Đưa các phần tử item ko trùng lặp vào list mới, sau đó sắp xếp list để cho việc lưu trữ theo dõi sau
    này.
    - Sau khi đã có list các item ta duyệt các item có trong list, so sánh nếu có item trùng lặp ta sẽ cộng "amount" của
    chúng lại với nhau. sau đó chuyển vào dict mới để lưu trữ.
"""
list_goc = [{'item': 'item1', 'amount': 400},
            {'item': 'item2', 'amount': 300},
            {'item': 'item1', 'amount': 750},
            {'item': 'item2', 'amount': 250},
            {'item': 'item3', 'amount': 150},
            {'item': 'item4', 'amount': 650},
            {'item': 'item3', 'amount': 550},
            {'item': 'item4', 'amount': 350}
            ]
list_item = []
dict_luu = {}
amount = 0
# ######################################################################################################################
# Lọc các item
for pt in list_goc:
    if pt['item'] not in list_item:
        list_item.append(pt['item'])
# ######################################################################################################################
# Lấy các amount
for pt in list_item:
    for key in list_goc:
        if pt == key['item']:
            amount += key['amount']
    dict_luu[pt] = amount
    amount = 0
print(dict_luu)
