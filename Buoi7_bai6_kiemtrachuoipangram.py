"""
    Viết hàm
        def is_pangram(str, alphabet)
    đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
    Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần
    bảng chữ cái anphabet: abcdefghijklmnopqrstuvwxyz
    - Cách 1: Ta
    
"""
string_test = input("Nhập vào một chuỗi bất kỳ: ")
string_anphabet = "abcdefghijklmnopqrstuvwxyz"


def is_pargram(str_test, alphabet):
    """
    Trước tiên ta so sánh độ dài chuỗi str_test với chuỗi anphabet. Nếu str_test có độ dài nhỏ hơn anphabet thì đây chắc
    chắn không phải chuỗi Pangram.
    Nếu độ dài str_test = anphabet, ta sẽ duyệt từng ký tự nhận được trong alphabet, xem các ký tự đó có trong str_test
    ko? Để duyệt hết các trường hợp ta chuyển str_test về dạng chữ thường.
    + Nếu kết quả duyệt toàn bộ chuỗi alphabet đều xuất hiện trong str_test thì sting_test là chuỗi Pangram.
    + Nếu không thì đây không phải là chuỗi Pangram
    :param str_test: Chuỗi cần test
    :param alphabet: Bảng chữ alphabet
    :return: trả lại kết quả True: chuỗi pangram. False: không phải chuỗi Pangram.
    """
    if len(str_test) < len(alphabet):
        return False
    else:
        for pt in alphabet:
            if pt not in str_test.lower():
                return False
    return True


if is_pargram(string_test, string_anphabet):
    print("Đây là chuỗi Pangram")
else:
    print("Đây ko phải chuỗi Pangram")
