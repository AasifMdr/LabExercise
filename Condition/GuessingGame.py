import random
random_num = random.randint(1 , 10)
attempts = 3

while attempts > 0:
    attempts -= 1
    guess = int(input("Guess a number: "))
    if guess == random_num:
        print('You got it right.')
        break
    else:
        print('You got it wrong.')