"""Set of functions."""

import prompt


def welcome_user():
    """Welcome user my entered name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    return name
