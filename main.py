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


def computer_guess(ending_range):
    low = 1
    high = ending_range
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess_c = random.randint(low, high)
        else:
            guess_c = low
        feedback = input(f"is the number {guess_c} too high (h), too low (l) or correct (c)")

        if feedback == 'h':
            high = guess_c - 1
        elif feedback == 'l':
            low = guess_c + 1
    print("Yay! Computer guessed my number")


computer_guess(100)
