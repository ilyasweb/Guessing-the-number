import random


def guess(ending_num):

    random_num = random.randint(1, ending_num)
    guess_num = 0

    while guess_num != random_num:
        guess_num = int(input(f"Enter your guess between 1 and {ending_num}? "))
        if guess_num > random_num:
            print("Guess is high try again")
        elif guess_num < random_num:
            print("Guess is low, try again")
    print(f"You have guessed the number {guess_num} correctly")


guess(50)
