import random

def generate_code(length=4):
    """Generate a random code of given length."""
    return [random.randint(1, 6) for _ in range(length)]

def get_feedback(code, guess):
    """Provide feedback on the guess compared to the code."""
    black_pegs = sum(c == g for c, g in zip(code, guess))
    white_pegs = sum(min(code.count(n), guess.count(n)) for n in set(guess)) - black_pegs
    return black_pegs, white_pegs

def main():
    print("Welcome to Logik (Mastermind)!")
    print("Try to guess the 4-digit code. Each digit is between 1 and 6.")
    print("Feedback: Black pegs = correct digit and position, White pegs = correct digit but wrong position.")
    
    code = generate_code()
    attempts = 0

    while True:
        guess = input("Enter your guess (e.g., 1234): ")
        if len(guess) != 4 or not guess.isdigit() or not all(1 <= int(d) <= 6 for d in guess):
            print("Invalid input. Please enter a 4-digit number with digits between 1 and 6.")
            continue
        
        guess = [int(d) for d in guess]
        attempts += 1
        black_pegs, white_pegs = get_feedback(code, guess)
        
        print(f"Feedback: {black_pegs} Black Peg(s), {white_pegs} White Peg(s)")
        
        if black_pegs == 4:
            print(f"Congratulations! You guessed the code {code} in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()