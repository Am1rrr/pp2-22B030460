
import random
name = input("Hello! What is your name? ")
number = random.randint(1, 20)
attempts = 0
print(f'Well, {name}, I am thinking of a number between 1 and 20.')
while True:
    guess = int(input("Take a guess\n"))
    attempts += 1
    if guess == number:
        print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
        break
    elif guess < number:
        print('Your guess is too low')
    else:
        print('Your guess is too high')