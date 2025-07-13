# Part B – Design

---

## User Interface

This game will be **text-based**, using the terminal for interaction. The user will see:

- A welcome message
- A series of flashcard questions
- Prompts to enter answers
- Instant feedback (Correct/Incorrect)
- A final score summary
- A “Play again?” prompt at the end

---

## Data Handling

### Data Structures:
- Flashcards stored as a list of dictionaries:
  ```python
  flashcards = [
      {"question": "What is 2 + 2?", "answer": "4"},
      {"question": "What is the capital of France?", "answer": "Paris"},
  ]

Variables:
score: tracks number of correct answers

total_questions: optional, could be len(flashcards)

File Input (optional for now):
Future feature: load flashcards from flashcards.txt or .csv file

--
## Modules and Functions

### `main()`
- Purpose: Controls the overall game flow
- Input: None
- Output: None
- Description: Runs the game loop, calls `play_game()`, and handles replay logic

### `play_game()`
- Purpose: Runs one full round of the flashcard quiz
- Input: None
- Output: None
- Description:
  - Shuffles flashcards
  - Asks each question
  - Checks answers and tracks score
  - Prints feedback and results

### `check_answer(user_input, correct_answer)`
- Purpose: Compares the user’s input with the correct answer
- Input: `user_input` (string), `correct_answer` (string)
- Output: `True` or `False`
- Description: Returns whether the input matches the correct answer (case-insensitive)

### `load_flashcards()`
- Purpose: Loads flashcards from an external file
- Input: File path (optional: `.txt` or `.csv`)
- Output: List of dictionaries
- Description: Reads questions and answers from a file and returns a list in the form:
  ```python
  [{"question": "What is...", "answer": "..."}, ...]

-- 
Input & Output Specs
✅ Input:
User answers via input() (text)

Replay prompt: “Do you want to play again? yes/no”

✅ Output:
Printed questions

Printed feedback: “✅ Correct!” or “❌ Incorrect…”

Final score: “You got 4/5 correct”

Option to restart or quit
