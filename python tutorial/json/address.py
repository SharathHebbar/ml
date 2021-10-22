

import json
book = {}

book['Tom'] = {
    'name': 'tom',
    'address': 'somewhere',
    'phone': 9898989898
}

book['bob'] = {

    'name': 'bob',
    'address': 'somewhere',
    'phone': 9768989898
}

s = json.dumps(book)
# print(s)

with open("C://ml//ml//python tutorial//json//book.txt", "w") as f:
    f.write(s)
