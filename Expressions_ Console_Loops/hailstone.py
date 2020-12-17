"""
File: hailstone.py
Name: Chris Lee
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter.
"""


def main():
    """
    When enters a number, the computer will calculate how
    many steps it takes to reach 1 according to Hailstone sequence.
    """
    print('This program computes Hailstone sequences.')
    print('')
    data = int(input('Enter a number:'))
    data2 = data
    count = 0
    while True:
        if data == 1:
            print('It took ' + str(count) + ' steps to reach 1.')
            break
        else:
            if data % 2 == 1:
                data2 = int(3 * data + 1)
                print(str(data)+' is odd, so I make 3n+1: '+str(data2))
                data = data2
            if data % 2 == 0:
                data2 = int(data / 2)
                print(str(data) + ' is even, so I make n/2: '+str(data2))
                data = data2
            count = count + 1


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
