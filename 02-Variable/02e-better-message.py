first_name = 'John'
last_name = 'Smith'
msg = f'{first_name} [{last_name}] is coder'
print(msg)


# length of string
print(len(msg))

# chuyển tất cả thành chữ thường lower()
print(msg.lower())


# chuyển tất cả thành in hoa upper()
print(msg.upper())

# số thứ tụ bắt đầu bằng 'Smith' trong chuỗi
# nếu không tìm thấy sẽ trả kết quả là -1
print(msg.find('Smith'))


# Thay thế chuỗi
# nếu không tìm thấy được chuỗi thì trả về ban đầu
print(msg.replace('coder', 'hacker'))
print(msg.replace('S', 'killer..'))

# Trên là các ví dụ về method của string
# Các method là:
# islower() là method trả về true or false
# title()
# find()
# replace()


print('killer' in msg)
# => false bc trong msg ban đầu không có killer (so với chuỗi msg ban đầu chứ
# khong phải chuỗi đã thay thế
# trả về giá trị True or False

print('coder' in msg)
