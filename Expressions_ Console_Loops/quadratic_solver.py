"""
File: quadratic_solver.py
Name: Chris Lee
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
"""

import math


def main():
	"""
	When user enters three numbers, the computer will calculate
	1. How many roots the equation has 2. x's value
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter C: '))
	discriminant = (b * b) - (4 * a * c)
	if discriminant < 0:
		print('No real root')
	elif discriminant > 0:
		y = math.sqrt((b * b) - (4 * a * c))
		x1 = (-b + y) / 2 * a
		x2 = (-b - y) / 2 * a
		print('Two roots: ' + str(x1) + ', ' + str(x2))
	elif discriminant == 0:
		y = math.sqrt((b * b) - (4 * a * c))
		x1 = (-b + y) / 2 * a
		print('One root: ' + str(x1))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
