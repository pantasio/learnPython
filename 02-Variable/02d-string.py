course = "python's Course for Beginer"
#         1234567889            -2 -1
#
print(course)
string2 = 'Python for "Beginners"'
print(string2)

# multi-line string
meg = '''
Hi pantasio,

Here is your big change to learn python.
Wish you have nice programing.
'''
print(meg)

# print the first character of course variable
print(course[0])

# print the last character of course variable
print(course[-1])

# print kí tự thứ 2 tính từ cuối của biến course
print(course[-2])

# print kí tự đầu tiên đến 3 kí tự tiếp theo của biến course
# 0 là kí tự bắt đầu
# 3 là số kí tự tiếp theo
print(course[0:5])


# print kí tự thứ 7 đến cuối chuỗi của biến course
print(course[7:])

# copy string to another
next_string = course[9:]
print(next_string)
