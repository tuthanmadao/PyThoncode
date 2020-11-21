"""
    Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
    - Ta duyệt các phần tử trong tuple. Kiểm tra xem kiểu tra xem các phần tử đó có giống nhau không.
        + Nếu xuất hiện một cặp bất kỳ không giống nhau => kết luận có phần tử khác nhau trong tuple
        + Nếu ko xuất hiện cặp bất kỳ không giống nhau => kết luận tất cả các phần tử của tuple đều giống nhau
"""
# my_tuple = (0, 3.14, 11, "my", "love", ["pi", 3.124])
# my_tuple = ("ha", "ha", "ha", "ha")
my_tuple = ([1, 2], [1, 2], [1, 2], [1, 2])
# my_tuple = ([1, 2], [1, 2], [1, 2], [1, 23])
kt = False
for i in range(0, len(my_tuple) - 1, 2):
    if my_tuple[i] != my_tuple[i+1]:
        kt = True
        break
if kt:
    print(f"Tuple {my_tuple} có phần tử khác nhau")
else:
    print(f"Tuple {my_tuple} có tất cả các phần tử giống nhau")
