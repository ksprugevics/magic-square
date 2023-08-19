# https://www.geeksforgeeks.org/magic-square/
import random
import numpy as np

def bogoSolveMagicSquare(size, numbers):
    magicConstant = size * (size * size + 1) / 2
    iterations = 0
    while not validation(numbers, size, magicConstant):
        random.shuffle(numbers)
        iterations = iterations + 1
        print(iterations)

    print("found magic square in " + str(iterations) + " iterations with magic constant: " + str(magicConstant))
    arr = np.array(numbers)
    arr = np.reshape(arr, (-1, size))
    print(arr)


def validation(numbers, size, magicConstant):
    arr = np.array(numbers)
    arr = np.reshape(arr, (-1, size))
    # for now only works on 3x3 because of manual index
    if (np.sum(arr[0, :]) != magicConstant): return False
    if (np.sum(arr[1, :]) != magicConstant): return False
    if (np.sum(arr[2, :]) != magicConstant): return False
    if (np.sum(arr[:, 0]) != magicConstant): return False
    if (np.sum(arr[:, 1]) != magicConstant): return False
    if (np.sum(arr[:, 2]) != magicConstant): return False
    if (np.trace(arr) != magicConstant): return False
    if (np.trace(np.flip(arr, -1)) != magicConstant): return False
    return True
    

bogoSolveMagicSquare(3, [1, 2, 3, 4, 5, 6, 7, 8, 9])