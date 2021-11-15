import os
filename= "first_group.txt"
for filename in os.walk("C:\\Users\\Пользователь\\Desktop\\laba5\\first_group.txt"):
    print(filename)

    filename= "second_group.txt"
for filename in os.walk("C:\\Users\Пользователь\\Desktop\\laba5\\second_group.txt"):
    print(filename)