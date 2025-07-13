# Project Plan - Flashcard Quiz Game

---

# Goal
The Goal of this project is to create a Flashcard Quiz Game in Python. The game will quiz users using questions and answers stored in memory or a file. It will give feedback on each answer and track the user's score. The goal is to make a fun, simple, and interactive study tool.

---

# Functionalities & Breakdown

# 1. Load Flashcards
- Flashcards will be stored in a list of dictionaries
- Example: `{"question": "What is 2 + 2?", "answer": "4"}`
- (Optional) Load flashcards from an external `.txt` file later

# 2. Display Questions
- Shuffle flashcards randomly
- Print each question to the user using `print()`

# 3. Get and Check Answers
- Use `input()` to get user answers
- Use `.lower()` for case-insensitive comparison
- Give feedback: "Correct!" or "Incorrect. The answer is..."

# 4. Track Score
- Use a counter variable (e.g., `score = 0`)
- Increment score if answer is correct

# 5. Show Final Score
- At the end display: "You got 3 out of 5 correct!"

# 6. Replay Option
- Ask user if they want to play again
- Restart or exit based on input

---

## Resources

- Language: Python 3
- Editor: Visual Studio Code
- Version Control: Git + GitHub
- Modules:
  - `random` – to shuffle flashcards
  - (Optional) `csv` or file I/O – for loading from a file
- File(s):
  - `flashcard_game.py` – main code
  - `flashcards.txt` – optional for flashcard data
