#Made by zitrus2k

import random

randomR = random.randint(1,10)

rInput = int(input('Guess Number 1-10 : '))

if rInput == randomR:
    print('You Won!')
else:
    print('Wrong! The Right Number was:', randomR)
