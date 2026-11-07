import random
lucky_num = (random.randint(1, 50))

while True:
    try:
        in_num = int(input("Guess the lucky number: "))

        if in_num > lucky_num:
            print("The given number is higher than the lucky number! Try again.")
        elif in_num < lucky_num:
            print("The given number is lower than the lucky number! Try again.")
        else:
            print("Congratulations!! You've guessed the lucky number!")
            break

    except ValueError:
        print("Please enter a valid number!")