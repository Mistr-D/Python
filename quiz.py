def run_quiz():
    questions = {
        "Easy": [
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What color is the sky on a clear day?", "answer": "blue"}
        ],
        "Medium": [
            {"question": "What is the capital of France?", "answer": "paris"},
            {"question": "What is 5 * 6?", "answer": "30"}
        ],
        "Hard": [
            {"question": "What is the square root of 144?", "answer": "12"},
            {"question": "Who developed the theory of relativity?", "answer": "einstein"}
        ]
    }

    print("Welcome to the Quiz!")
    print("Choose a difficulty: Easy, Medium, Hard")
    difficulty = input("Enter difficulty: ").capitalize()

    if difficulty not in questions:
        print("Invalid difficulty. Please restart the quiz.")
        return

    score = 0
    for q in questions[difficulty]:
        answer = input(q["question"] + " ").strip().lower()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"You got {score}/{len(questions[difficulty])} questions correct.")

if __name__ == "__main__":
    run_quiz()