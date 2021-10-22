import json
f = open("C://ml//ml//python tutorial//json//book.txt", "r")
s = f.read()

print(s)


book = json.loads(s)
# print(book)
# print(book['bob'])
# print(book['bob']['phone'])


for p in book:
    print(book[p])
