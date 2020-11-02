# Nhúng giá trị vào trong chuỗi
"""
    Lệnh print() là lệnh in ra màn hình một chuỗi ký tự được đặt trong dấu nháy kép hoặc nháy đơn
    Lệnh print() cũng in được ra giá trị của một biến. Giá trị này đặt ngoài dấu nháy
    Để in ra một chuỗi có kèm giá trị của các biến ta dùng các cú pháp sau
    print("nội dung chuỗi",biến) hoặc print("nội dung chuỗi %d" %(biến)
    hoặc print("chuỗi {}".format(biến)).
    Các lệnh sẽ được trình bày rõ bằng các ví dụ bên dưới
"""
name, py = 'Py', "Thon"
print('Xin chao %s. Toi la %s' % (name, py))
# In ra màn hình doạn văn bản "Xin chao %s. Toi la %s " trong đó %s là thẻ định dạng ký tự
# Tại các thẻ định dạng này chương trình sẽ thay thế các thẻ này bằng các biến "name", "py" theo thứ tự
# Khi này đoạn văn bản sẽ được in ra có dạng là:"Xin chao Py. Tôi là Thon"

x, y = 123, 456
print("Gia tri cua x la {}, y la {} và trung binh la: {}".format(x, y, (x+y)/2))
# In ra màn hình đoạn "giá trị của x là {}, y là {} và trung bình là : {}"
# Trong đó các giá trị trong lệnh format(x, y, (x+y)/2 ) là x, y, (x+y)/2 sẽ được thay thế vào các dấu "{}"
# theo đúng thứ tự.

print("I love {0} and {1}".format('Python', 'JavaScript'))
# Tương tự như trên trong đó {0} sẽ được thay thế bằng cuỗi tại vị trí 0 là 'Python'
# {1} sẽ được thay thế bởi chuỗi tại vị trí 1 là 'JavaScript' được đặt trong lênh format('Python', 'JavaScript')

print("I love {1} and {0}".format('Python', 'JavaScript'))
# Tương tự như lện bên trên. Ở đây ta thấy được ta có thể sắp xếp vị trí hiển thị
# các phần tử trong lênh format('Python', 'JavaScript') chỉ cần thay đổi vị trí đặt của {1} và {o}
# Trong đó chữ số trong {} chính là số thứ tự các biến đặt trong lệnh format()

print("Hello {f_name}. I am {my_name}.".format(f_name='John', my_name='PyCore'))
# Tương tự lệnh trên. Khác ở đây ta đặt trong {} là tên các biến được gán giá trị ở trong lênh format
# Ở đây là biến f_name='John' và my_name='PyCore'
