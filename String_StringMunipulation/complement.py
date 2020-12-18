"""
File: complement.py
Name: Chris Lee
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
The program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    When enters a DNA strand (assumes that the user will only
    enter A, C, T, or G, and the APP is case sensitive), the computer
    will tell you the complement matches.
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    dna = dna.upper()
    new_dna = build_complement(dna)
    print(new_dna)


def build_complement(dna):
    """
    When enters 'A', the computer will give you 'T';
    When enters 'T', the computer will give you 'A';
    When enters 'C', the computer will give you 'G';
    When enters 'G', the computer will give you 'C';
    and then return the value to the main function.
    """
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
