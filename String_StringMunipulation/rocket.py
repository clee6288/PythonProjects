"""
File: rocket.py
Name: Chris Lee
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
"""

# This constant determines rocket size.
SIZE = 10


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	# This is the function of the rocket's head part.
	for i in range(SIZE):
		for j in range(SIZE-i):
			print(' ', end='')
		print('/' * (i+1) + '\\' * (i+1))


def belt():
	# This is the function of the rocket's belt part.
	print('+', end='')
	print('==' * SIZE, end='')
	print('+')


def upper():
	# This is the function of the rocket's upper part.
	for i in range(SIZE):
		print('|', end='')
		for j in range(SIZE - 1 - i):
			print('.', end='')
		for j in range(i+1):
			print('/\\', end='')
		for j in range(SIZE - 1 - i):
			print('.', end='')
		print('|')


def lower():
	# This is the function of the rocket's lower part.
	for i in range(SIZE):
		print('|', end='')
		for j in range(i):
			print('.', end='')
		for j in range(SIZE-i):
			print('\\/', end='')
		for j in range(i):
			print('.', end='')
		print('|')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()