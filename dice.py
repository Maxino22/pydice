import random
import time
min = 1

max = 6

roll_again = 'yes'

while roll_again == 'yes' or roll_again == 'y':
    print('Rolling the dice...')
    time.sleep(1.5)
    print('The values are ....')
    time.sleep(1.5)
    print(random.randint(min, max))

    print(random.randint(min, max))

    roll_again = input('roll the dice again?').lower()
