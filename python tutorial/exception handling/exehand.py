
x = input()
y = input()

try:
    z = int(x) / (y)
except ZeroDivisionError as e:
    print(e)
    z = None
except TypeError as e:
    print(e)
    z = None
print(z)
