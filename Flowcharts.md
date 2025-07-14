# Part D – Flowcharts

This section includes flowcharts describing the main program logic and individual functions in the Flashcard Quiz Game.

---

## Main Program Flowchart

```plaintext
+------------------------+
| Start Program          |
+------------------------+
           |
           v
+------------------------+
| Call play_game()       |
+------------------------+
           |
           v
+------------------------+
| Ask to play again?     |
+------------------------+
     | Yes        | No
     v            v
(play_game)     End Program

-------------

## Function-Level Flowchart: play_game()
+-----------------------------+
| Start play_game()          |
+-----------------------------+
           |
           v
+-----------------------------+
| Shuffle flashcards         |
+-----------------------------+
           |
           v
+-----------------------------+
| For each flashcard:        |
| - Display question         |
| - Get user input           |
| - Check answer             |
| - Show feedback            |
+-----------------------------+
           |
           v
+-----------------------------+
| Show final score           |
+-----------------------------+
           |
           v
| Return to main()           |
+-----------------------------+

------------

## Function-Level Flowchart: check_answer()
+---------------------------+
| check_answer(input, ans) |
+---------------------------+
           |
           v
+---------------------------+
| Convert input & answer   |
| to lowercase             |
+---------------------------+
           |
           v
+---------------------------+
| Compare input == answer? |
+---------------------------+
     | Yes         | No
     v             v
Return True     Return False
