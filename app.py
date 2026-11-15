import random


def play():
    print("Welcome to Number Guess Game".upper().center(50))

    i = 0
    while True:
        try:
            lower_limit = int(input("Enter lower limit: "))
            upper_limit = int(input("Enter upper limit: "))
            guess_limit = int(input("Enter guess limit: "))
        except:
            if i == 2:
                print("Counter reaches the limit. Goodbye!")
                quit()
            else:
                print("Please enter integer values!")
                i += 1
        else:
            break

    random_number = random.randint(lower_limit, upper_limit)

    i = 0
    while i < guess_limit:
        try:
            guess = int(input("Guess the number: "))
        except Exception as ex:
            print("Please enter a numeric value!")
            i += 1
        else:
            if guess == random_number:
                print("Correct")
                break
            elif guess > random_number:
                print("Down!")
            else:
                print("Up")
            i += 1

    if i == guess_limit:
        print("You didn't guess the number correctly!")


play()
