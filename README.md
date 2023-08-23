## Magic square finding algorithms

This repo contains some algorithm implementations of solving [ordinary magic squares](https://en.wikipedia.org/wiki/Magic_square#Classification_of_magic_squares)

I don't claim to be an author of any of the algorithms, these are just my implementations using NumPy. The script contains a main method for testing and the following algorithms defined as seperate functions:

0. **validate(numbers, size)** - validates whether a given matrix is an ordinary magic square
1. **calculateMagicConstant(size)** - calculates the magic constant, given the size of the matrix
2. **bogoSolveMagicSquare(size)** - shuffles the matrix until a magic square is found (very slow)
3. **oddMagicSquareSolve(size, startNumber)** - given the size and starting number, finds a magic square. Only works with odd values of n. Based on https://www.1728.org/magicsq1.htm
4. **oddMagicSquareSolve2(size)** - given the size, finds a magic square. Only works with odd values of n. Based on https://www.geeksforgeeks.org/magic-square/
5. **doublyEvenMagicSquareSolve(size)** - given the size, finds a magic square. Only works with doubly-even (divisible by 4) values of n. Based on https://www.1728.org/magicsq2.htm
6. **singlyEvenMagicSquareSolve(size)** - given the size, finds a magic square. Only works with singly-even (divisible by 2 but not by 4) values of n. Based on https://www.1728.org/magicsq3.htm



Size in the function definitions correspond to n
