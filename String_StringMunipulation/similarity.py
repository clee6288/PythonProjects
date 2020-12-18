"""
File: similarity.py
Name: Chris Lee
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    When enter one long sequence and one short sequence,
    the computer will give you the best match of the
    DNA sequence within the long sequence.
    """
    long_sequence = input(str('Please give me a DNA sequence to search: '))
    long_sequence = long_sequence.upper()
    short_sequence = input(str('What DNA sequence would you like to match? '))
    short_sequence = short_sequence.upper()
    box = compare_two_sequences(long_sequence, short_sequence)
    print(box)


def compare_two_sequences(long_sequence, short_sequence):
    maximum = 0
    # maximum of different j sequence
    max_ans = ''
    # this is the box for the final answer
    for i in range(len(long_sequence)-len(short_sequence)+1):
        # ex 10 - 5 + 1 = 6
        count = 0
        # every j sequence's similarity
        ans = ''
        # the is the box for j sequence's answer
        for j in range(len(short_sequence)):
            ans += long_sequence[i+j]
            if short_sequence[j] == long_sequence[i+j]:
                count += 1
        if count > maximum:
            maximum = count
            max_ans = ans
    return max_ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
