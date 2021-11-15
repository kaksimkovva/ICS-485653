filename = "first_group.txt"
text_file=open("first_group.txt", "a+")
text_file.write("Дозапис працює")
text_file.close()

filename = "second_group.txt"
text_file=open("second_group.txt", "a")
text_file.write("Дозапис працює")
text_file.close()