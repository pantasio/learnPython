This is follow tutorial with [Mosh](https://www.youtube.com/watch?v=_uQrJ0TkZlc)

Cac vi du ve ham trong python bang tieng viet https://viettuts.vn/python-number

## Cac nguyen tac dat ten cho bien

## Các đặc điểm của Python cần biết:
### Đặc điểm 1: Comment trong Python
```
# đây là comment 1 dòng

print "Hello Python" # Comment trên cùng dòng lệnh không khuyến khích dùng.

"""
Đây là comment
nhiều dòng
    Các dòng comment tất nhiên không bị ảnh hưởng bởi nguyên tắc đóng khối dòng lệnh
    sẽ được nói đến ở đặc điểm 2 bên dưới đây.
"""
```

### Đặc điểm 2: 
Python không dùng dấu `()` hay `{}` để đóng khối lệnh mà dùng độ thụt dòng code 
(indentation) để đóng khối lệnh. Điều này là bắc buộc. Tôi dùng tab= 3 khoảng trắng 
để nhận biết khối lệnh.

### Đặc điểm 3:
Khi một dòng lệnh quá dài nên dùng dấu `\` để thể hiện sự liên tục của một dòng lệnh.
Bạn cũng có dùng để trình bày cho dễ đọc lệnh hơn.
Ví dụ
```
total = item_one + \
        item_two + \
        item_three
```
Khi bạn muốn trình bày nhiều dòng lệnh trên 1 dòng lệnh đơn: hãy dùng dấu chấm phẩy `;`
Ví dụ: 
```
print("Tôi đi học"); print("hôm nay trên lớp dạy python"); print("Rất vui khi được học python")
```

### Đặc điểm 4:
Dưới đây là tất cả các trích dẫn hợp lệ:
```
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
```


### Đặc điểm 5:
Các nhóm lệnh đa dòng (còn được gọi là suite) trong Python
Một nhóm các lệnh đơn, mà tạo một khối code đơn, được gọi là suite trong Python. 
Các lệnh phức hợp như if, while, def, và class cần một dòng header và một suite.
  
Các dòng header bắt đầu lệnh (với từ khóa) và kết thúc với một dầu hai chấm (:) 
và được theo sau bởi một hoặc nhiều dòng để tạo nên một suite. Ví dụ như:


