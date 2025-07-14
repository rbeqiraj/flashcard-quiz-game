# Part C – Pseudocode

---

## Top-Level Algorithm (Main Program)

main()
FUNCTION main():
    DISPLAY welcome message
    WHILE True:
        CALL play_game()
        ASK user if they want to play again
        IF user says no:
            DISPLAY "Thanks for playing!"
            BREAK loop
END FUNCTION

—--

play_game()
FUNCTION play_game():
    SHUFFLE the list of flashcards
    SET score to 0
    FOR each card in flashcards:
        DISPLAY card["question"]
        GET user_answer
        IF check_answer(user_answer, card["answer"]):
            DISPLAY "Correct!"
            INCREMENT score
        ELSE:
            DISPLAY "Incorrect. The correct answer is: card['answer']"
    DISPLAY final score out of total
END FUNCTION

—-- 

check_answer(user_input, correct_answer)
FUNCTION check_answer(user_input, correct_answer):
    IF user_input.lower() == correct_answer.lower():
        RETURN True
  ELSE:
        RETURN False
END FUNCTION

---

## ⚠️ Edge Cases & Error Handling

- If the user enters nothing:
  - Treat it as a blank string and mark as incorrect
- If flashcard list is empty:
  - Display message: "No flashcards found"
- (Optional) Try/Except for file loading
- Replay input is case-insensitive: Accept “Yes”, “yes”, “YES”, etc.
