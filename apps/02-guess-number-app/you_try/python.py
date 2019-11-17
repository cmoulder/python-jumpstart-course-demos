import random

print("-------------------------------------")
print("       GUESS THAT NUMBER GAME")
print("-------------------------------------")
print()

the_number = random.randint(0, 100)
guess = -1

while guess != the_number:
    guess_text = input("Guess a number between 0 and 100: ")
    guess = int(guess_text)

    if guess < the_number:
        print("Your guess of {} is too low".format(guess))
    elif guess > the_number:
        print("Your guess of {} is too high".format(guess))

print("You got it, the number was {}".format(the_number))
