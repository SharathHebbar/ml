# f = open("C:\\ml\\ml\\python tutorial\\files\\funny.txt", "r")
# f1 = open("C:\\ml\\ml\\python tutorial\\files\\funny1.txt", "w")
# # print(f.read())

# for l in f:
#     tokens = l.split(" ")
#     print(l)
#     print(str(tokens))
#     f1.write("word count: "+str(len(tokens))+" "+l)
#     print(len(tokens))

# f.close()
# f1.close()

with open("C:\\ml\\ml\\python tutorial\\files\\funny.txt", "r") as f:
    print(f.read())
print("Closed: ", f.closed)
