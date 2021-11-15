from operator import itemgetter
output=[]
for i in open("/Users/vladimirnikiforov/Downloads/laba5/first_group.txt"):
    output.append([i.split(None, -1)[0], i.split(None, -1)[1], float(i.split(None, -1)[2])])
output= sorted(output, key=itemgetter(2) )
print(output)