import random

def roll_dice(sides=6):
    """Roll a dice with the specified number of sides."""
    return random.randint(1, sides)

def main():
    print("Welcome to the Digital Dice Roller!")
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice (or type 0 to quit): "))
            if sides == 0:
                print("Thanks for playing! Goodbye!")
                break
            if sides < 2:
                print("A dice must have at least 2 sides. Try again.")
                continue
            result = roll_dice(sides)
            print(f"You rolled a {result} on a {sides}-sided dice!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
