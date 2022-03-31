"""
Hexlet: Project 1.

Studing module
"""

from brain_games.cli import welcome_user
import prompt
import random

def main():
    """Run an example code."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while True:
        question = random.randint(1, 20)
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        is_even = (question % 2 == 0)
        if (is_even and answer == 'yes') or (not is_even and answer == 'no'):
            print('Correct!')
            i += 1
        else:
            correct_answer = ('yes' if is_even else 'no')
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, correct_answer))
            print("Let's try again, {0}!".format(user_name))
            break
        if i == 3:
            print('Congratulations, {0}!'.format(user_name))
            break


if __name__ == '__main__':
    main()