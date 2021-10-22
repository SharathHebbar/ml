import multiprocessing
import time

square_list = []


def sq(n):
    global square_list
    print("Square of 2 numbers")
    for i in n:
        print('Square: ', i**2)
        square_list.append(i**2)
    print("within process", square_list)


if __name__ == '__main__':
    a = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=sq, args=(a,))
    p1.start()
    p1.join()
    print(square_list)
    print("Done")
