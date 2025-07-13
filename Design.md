# 🧠 Part B – Design

---

## 🖥️ User Interface

This game will be **text-based**, using the terminal for interaction. The user will see:

- A welcome message
- A series of flashcard questions
- Prompts to enter answers
- Instant feedback (Correct/Incorrect)
- A final score summary
- A “Play again?” prompt at the end

---

## 💾 Data Handling

### Data Structures:
- Flashcards stored as a list of dictionaries:
  ```python
  flashcards = [
      {"question": "What is 2 + 2?", "answer": "4"},
      {"question": "What is the capital of France?", "answer": "Paris"},
  ]
