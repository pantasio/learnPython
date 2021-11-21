""" biểu thức điều kiện có 3 loại syntax:
Loại 1: <bieu-thuc-dk> là đúng (True) thì sẽ thực hiện <chuoi-hanh-dong-1>
if <bieu-thuc-dk>:
    <chuoi-hanh-dong-1>

Loại 2: <bieu-thuc-dk> là Đúng (True) thì sẽ thực hiện <chuoi-hanh-dong-1>
        <bieu-thuc-dk> là Sai (False) thì sẽ thực hiện <chuoi-hanh-dong-2> 
if <bieu-thuc-dk>:
    <chuoi-hanh-dong-1>
else:
    <chuoi-hanh-dong-2>

Loại 3: 

# Chúng ta có thể kết hợp với toán tử AND và OR
# hay dùng toán tử so sánh ==  != >= <=
"""


is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    Print("An kem chuối hem")
elif is_cold:
    print("It's a cool day")
    print("trời lạnh thì ăn lẩu")
else:
    print("It's a lovely day")
    print("Đi bơi là tuyệt")

print("Dù một ngày như thế nào ta luôn vui vẻ.")

print("#################")

# bài tập
# Nếu em khánh đã nấu cơm => cho đi chơi vũng tàu
# Nếu em khánh đã quét nhà => chỉ cho đi chơi thú nhúng
# Nếu em khánh vừa nấu cơm vừa quét nhà => đi chơi vũng tàu và ăn ghẹ
