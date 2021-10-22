import multiprocessing


def sq(n):
    print("Square of 2 numbers")
    for i in n:
        print('Square: ', i**2)


def cub(n):
    print("Cube of 2 numbers")
    for i in n:
        print('Cube: ', i**3)


if __name__ == '__main__':
    a = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=sq, args=(a,))
    p2 = multiprocessing.Process(target=cub, args=(a,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
