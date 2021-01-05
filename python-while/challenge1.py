import random

number = random.randint(1, 5)
guess = 0
count = 0

while guess != number :
    guess = input('Guess a number between 1 and 5: ')
    count += 1
    if guess.isnumeric() == False:
        continue
    guess = int(guess)

print(f'You guessed it in {count} times!')
