"""
File: caesar.py
Name: Chris Lee
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    When enters a secret number and a ciphered string,
    the computer will give you the encrypted string.
    """
    number = int(input('Secret Number: '))
    data = input('What\'s the ciphered string? ')
    data = data.upper()
    new_data = decipher(data, number)
    print(new_data)


def decipher(data, number):
    ans = ''
    for i in range(len(data)):
        if data[i].isalpha():
            box = ALPHABET.find(data[i])
            ans += ALPHABET[box+number-len(ALPHABET)]
        else:
            ans += data[i]
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
