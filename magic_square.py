import numpy as np


def calculateMagicConstant(size):
    return size * (size * size + 1) / 2

# Shuffle until we get a magic square (infinitely slow) but on average took ~100k iterations
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
def vedicMathsSolveMagicSquare(size, startNumber):
    numbers = np.arange(startNumber, startNumber + size * size)
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

    # print("Found magic square with magic constant: " + str(calculateMagicConstant(size)) + " validated: " + str(validation(magicSquare.flatten(), size)))
    # print(magicSquare)
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


# https://www.1728.org/magicsq3.htm
def singlyEvenMagicSquareSolve(size):
    if size % 4 == 0 or size % 2 != 0 or size == 2:
        print("Size must be divisble by 2 but not by 4 and should be larger than 2")
        return
    
    magicSquare = np.zeros((size,size))

    subSquareSize = int(size / 2)
    sub1 = vedicMathsSolveMagicSquare(subSquareSize, 1)
    sub2 = vedicMathsSolveMagicSquare(subSquareSize, 1 + 1 * subSquareSize * subSquareSize)
    sub3 = vedicMathsSolveMagicSquare(subSquareSize, 1 + 2 * subSquareSize * subSquareSize)
    sub4 = vedicMathsSolveMagicSquare(subSquareSize, 1 + 3 * subSquareSize * subSquareSize)
    magicSquare = np.vstack((np.hstack((sub1, sub3)), np.hstack((sub4, sub2))))
    print(magicSquare)

    temp = magicSquare[0, 0]
    magicSquare[0, 0] = magicSquare[3, 0]
    magicSquare[3, 0] = temp

    temp = magicSquare[2, 0]
    magicSquare[2, 0] = magicSquare[5, 0]
    magicSquare[5, 0] = temp

    temp = magicSquare[1, 1]
    magicSquare[1, 1] = magicSquare[4, 1]
    magicSquare[4, 1] = temp

    temp = np.hstack((magicSquare[:3, 5], magicSquare[3:, 5]))
    magicSquare[:, 5] = temp
    print(validation(magicSquare, size))

    # print("Found magic square with magic constant: " + str(calculateMagicConstant(size)) + " validated: " + str(validation(magicSquare.flatten(), size)))
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
# vedicMathsSolveMagicSquare(3, 10)
# doublyEvenMagicSquareSolve(8)
singlyEvenMagicSquareSolve(6)