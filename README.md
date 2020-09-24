# Elipse-v3
The text files are used to store your best creature yet. Destroy them to restart the process

An important thing for making it faster is changing the number of integers in "seb" on line 146. Each creature is a matrix of len(seb) so an extra value is very impactfult

How it calculates the answer from a matrix:


for x, y in itertools.product(range(0, len(self.__guts)), range(0, len(self.__guts))):
    guess = guess + self.__guts[x][y] * 100 ** (x - (len(self.__guts)) // 2) * tests ** (y - (len(self.__guts)) // 2)

Each number in the matrix is multiplied by height_of_elipse ^ row * width_of_elipse ^ collumn

In reality, row and collum have the length of the matrix divided by two subtracted from them


0 0 0
0 5 0
0 0 0

Would be answer = 5 * width ^ 0 * height ^ 0


0 0 0
0 0 0
0 0 16

Would be answer = 16 * width ^ 1 * height ^ 1

0 0 0
0 0 0
0 5 16

Would be answer = 16 * width ^ 1 * height ^ 1 + 5 * width ^ 0 * height ^ 1



