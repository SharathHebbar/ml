
print("Second instance")


def process_file():

    try:
        f = open("C:\\ml\\ml\\python tutorial\\files\\funny.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("File error: ", e)
    finally:
        f.close()
        print("Closed: ", f.closed)


process_file()
print("End of second instance")


print("First instance")


def process_file():
    try:
        f = open("C:\\ml\\ml\\python tutorial\\files\\funny.txt")
        x = 1/0
    except FileNotFoundError as e:
        print(e)
    f.close()
    print("Closed: ", f.closed)


process_file()
print("End of first instance")
