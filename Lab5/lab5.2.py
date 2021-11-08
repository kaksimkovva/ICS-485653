import csv
import sys
print("Група 1")
filename = "first_group.txt"
text_file=open("first_group.txt", "r")
reader=csv.reader(text_file, delimiter="\t")
for str in reader:
    print(str)
text_file.close()

print("Група 2")
filename = "second_group.txt"
text_file=open("second_group.txt", "r")
reader=csv.reader(text_file, delimiter="\t")
for str in reader:
    print(str)
text_file.close()