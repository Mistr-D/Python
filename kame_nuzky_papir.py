
print("pick between rock, paper, scissors")
print("1. rock")
print("2. paper")
print("3. scissors")

choice = int(input("pick a number:"))
if choice == 1:
    if choice == 1:
        print("rock")
    if choice == 2:
        print("paper")
    if choice == 3:
        print("scissors")

import random
computer_choice = random.randint(1, 3)
if computer_choice == 1:
    print("computer chose rock")
if computer_choice == 2:
    print("computer chose paper")
if computer_choice == 3:
    print("computer chose scissors")

if choice == computer_choice:
        print("draw")
if choice == 1 and computer_choice == 2:
    print("you lose")
if choice == 2 and computer_choice == 3:
    print("you lose")
if choice == 3 and computer_choice == 1:
    print("you lose")
elif choice == 1 and computer_choice == 3:
    print("you win")
elif choice == 2 and computer_choice == 1:
    print("you win")
elif choice == 3 and computer_choice == 2:
    print("you win")