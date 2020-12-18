"""
File: hangman.py
Name: Chris Lee
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    When enters a alphabet, the computer will tell you if it is
    an alphabet in the correct random answer. If not, the console will not
    change, if correct, the computer will update your input onto
    the console. You will have N_TURNS chances to guess.
    """
    random_ans = random_word()
    # input random word's vocabulary (correct answer)
    dash = len(random_ans) * '-'
    # create dashes of the length of random_ans
    print('The word looks like: '+dash)
    # the console will show dashes of the length of random_ans
    real_ans = dash
    # create a box for real_ans & input real_ans's original value
    lives = N_TURNS
    # Create a box for lives
    while True:
        data = str(input('Your guess: '))
        # user entry
        data = data.upper()
        # case sensitive
        ans = ''
        # create an empty string for for in in range
        for i in range(len(random_ans)):
            """
            three situations: 
            (1) correct answer (add)
            (2) correct answer already in the real_ans
            (3) Not correct answer add (-)
            """
            if data == random_ans[i]:
                ans += data
            elif real_ans[i].isalpha():
                ans += real_ans[i]
            else:
                ans += '-'
        if random_ans.find(data) == -1:
            # if cannot find data in random_and will return -1
            lives = lives-1
            # nom matter what, lives will decrease 1 everytime
            print('There is no' + data + "'\'s in the word.")
            if lives == 0:
                # when lives become zero
                print('You are completely hung :(')
                print('The word was: '+random_ans)
                break
        else:
            print('You are correct!')
        real_ans = ans
        print('The word looks like: ' + real_ans)
        print('You have ' + str(lives) + ' guesses left.')

        if real_ans == random_ans:
            # when you win the game
            print('You are correct!')
            print('You win!!')
            print('The word was '+random_ans)
            break


    # print('The word looks like: ')
    # print('You have '+N_TURNS+' guesses left.')
    # print('There is no K\'s in the word.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
