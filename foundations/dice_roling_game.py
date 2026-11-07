import random

roll_counter = 0

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == 'y':
        try:
            dice_count = int(input("How many dice do you want to roll?: "))
            for _ in range(dice_count):
                dice = random.randint(1, 6)
                print(f'({dice})')
                roll_counter += 1

            print(f"Total dice rolled so far this session: {roll_counter}")
        except ValueError:
            print("Please enter a valid number!")

    elif choice == 'n':
        print(f"Thanks for playing! You rolled a total of {roll_counter} dice in this session.")
        break
    else:
        print("Invalid choice!")