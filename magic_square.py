import numpy as np

def calculateMagicConstant(size):
    return size * (size * size + 1) / 2


def bogoSolveMagicSquare(size):
    numbers = np.arange(1, size * size + 1)
    iterations = 0
    while not validation(numbers, size):
        np.random.shuffle(numbers)
        iterations = iterations + 1
        print(iterations)

    print("Found magic square in " + str(iterations) + " iterations with magic constant: " + str(calculateMagicConstant(size)) + " validated: " + str(validation(numbers, size)))
    numbers = np.reshape(numbers, (-1, size))
    print(numbers)
    return numbers


# https://www.geeksforgeeks.org/magic-square/
# Only for odd sized magic squares
def positionCalcuateSolveMagicSquare(size):
    numbers = np.arange(1, size * size + 1)
    magicSquare = np.zeros((size, size))
    elementPos = [int(size / 2), size - 1]
    magicSquare[elementPos[0], elementPos[1]] = numbers[0]

    for i in range(1, len(numbers)):
        elementPos = [elementPos[0] - 1, elementPos[1] + 1]

        if elementPos[0] == -1 and elementPos[1] == size:
            elementPos = [0, size - 2]
        elif elementPos[0] == -1:
            elementPos[0] = size - 1

        if elementPos[1] == size:
            elementPos[1] = 0

        if magicSquare[elementPos[0], elementPos[1]] != 0:
            elementPos = [elementPos[0] + 1, elementPos[1] - 2]

        magicSquare[elementPos[0], elementPos[1]] = numbers[i]

    print("Found magic square with magic constant: " + str(calculateMagicConstant(size)) + " validated: " + str(validation(magicSquare.flatten(), size)))
    print(magicSquare)
    return magicSquare


# https://www.geeksforgeeks.org/magic-square/
# Only for odd sized magic squares
def vedicMathsSolveMagicSquare(size):
    numbers = np.arange(1, size * size + 1)
    magicSquare = np.zeros((size, size))
    elementPos = [int(size / 2), size - 1]
    magicSquare[elementPos[0], elementPos[1]] = numbers[0]

    for i in range(1, len(numbers)):
        elementPos = [elementPos[0] + 1, elementPos[1] + 1]
        if elementPos[0] == size and elementPos[1] == size:
            elementPos = [elementPos[0] - 1, elementPos[1] - 2]
        elif elementPos[1] == size and elementPos[0] < size:
            elementPos[1] = 0
        elif elementPos[0] == size and elementPos[1] < size:
            elementPos[0] = 0

        if magicSquare[elementPos[0], elementPos[1]] != 0:
            elementPos = [elementPos[0] - 1, elementPos[1] - 2]

        magicSquare[elementPos[0], elementPos[1]] = numbers[i]

    print("Found magic square with magic constant: " + str(calculateMagicConstant(size)) + " validated: " + str(validation(magicSquare.flatten(), size)))
    print(magicSquare)
    return magicSquare

# https://www.1728.org/magicsq2.htm
def doublyEvenMagicSquareSolve(size):
    if size % 4 != 0:
        print("Size must be divisble by 4")
        return
    
    magicSquare = np.arange(1, size * size + 1)
    magicSquare = np.reshape(magicSquare, (-1, size))

    padding = int(size / 4)
    magicSquare[0 : padding, padding : size - padding] = 0
    magicSquare[size - padding : size, padding : size - padding] = 0
    magicSquare[padding : size - padding, 0 : padding] = 0
    magicSquare[padding :size - padding, size - padding : size] = 0

    index = size * size
    for i in range(0, size):
        for j in range(0, size):
            if magicSquare[i, j] == 0:
                magicSquare[i, j] = index
            index = index - 1
            
    print("Found magic square with magic constant: " + str(calculateMagicConstant(size)) + " validated: " + str(validation(magicSquare.flatten(), size)))
    print(magicSquare)
    return magicSquare

def validation(numbers, size):
    magicConstant = calculateMagicConstant(size)
    arr = np.reshape(np.copy(numbers), (-1, size))
    for i in range(0, size):
        if np.sum(arr[i, :]) != magicConstant: return False
        if np.sum(arr[:, i]) != magicConstant: return False
    if np.trace(arr) != magicConstant: return False
    if np.trace(np.flip(arr, -1)) != magicConstant: return False
    return True
    

# bogoSolveMagicSquare(3)
# positionCalcuateSolveMagicSquare(5)
# vedicMathsSolveMagicSquare(7)
doublyEvenMagicSquareSolve(8)