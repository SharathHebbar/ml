import time
import threading


def sq(n):
    print("Square of 2 numbers")
    for i in n:
        time.sleep(0.2)
        print('Square: ', i**2)


def cub(n):
    print("Cube of 2 numbers")
    for i in n:
        time.sleep(0.2)
        print('Cube: ', i**3)


a = [2, 3, 8, 9]
t = time.time()
t1 = threading.Thread(target=sq, args=(a,))
t2 = threading.Thread(target=cub, args=(a,))

t1.start()
t2.start()

t1.join()
t2.join()
print("Done in: ", time.time()-t)
