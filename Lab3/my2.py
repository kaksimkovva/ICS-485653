a = 30
b = 46
def f():
    global a
    a = a + 213
    print (a)

f()
print(a)