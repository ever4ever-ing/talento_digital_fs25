# Rock, Papers, Scissors


import random

import sys

import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

player = int(input(
    'Please choose your move: 1 is for Rock \u270a, 2 is for Paper \u270b, 3 is for Scissors \u270c. Pick a number: '))
computer = random.randint(1, 3)

if computer == 1 and player == 1:
    print('You chose: \u270a \nCPU chose: \u270a \nDraw!')
elif computer == 1 and player == 2:
    print('You chose: \u270b \nCPU chose: \u270a \nThe player won!')
elif computer == 1 and player == 3:
    print('You chose: \u270c \nCPU chose: \u270a \nCPU won!')
elif computer == 2 and player == 1:
    print('You chose: \u270a \nCPU chose: \u270b\nCPU won!')
elif computer == 2 and player == 2:
    print('You chose: \u270b \nCPU chose: \u270b \nDraw!')
elif computer == 2 and player == 3:
    print('You chose: \u270c \n CPU chose: \u270b \nThe player won!')
elif computer == 3 and player == 1:
    print('You chose: \u270a \nCPU chose: \u270c \nThe player won!')
elif computer == 3 and player == 2:
    print('You chose: \u270b \nCPU chose: \u270c \nCPU won!')
elif computer == 3 and player == 3:
    print('You chose: \u270c \nCPU chose: \u270c \nDraw!')
else:

    print('Enter a valid entry')
