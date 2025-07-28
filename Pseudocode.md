## Pseudocode – Flashcard Quiz Game

This section outlines the logical structure of the main functions in the Flashcard Quiz Game.

---

### start_quiz()

```
function start_quiz():
    get selected flashcard set from dropdown
    if no set is selected:
        show error message and return

    retrieve flashcards for that set
    if no flashcards:
        show info message and return

    initialize quiz_index = 0
    initialize quiz_score = 0

    enable quiz input and buttons
    call show_quiz_question()
```

---

### show_quiz_question()

```
function show_quiz_question():
    if quiz_index is within range of quiz_cards:
        display the definition
        clear previous answer and feedback
    else:
        show final score
        disable input and submit button
```

---

### submit_quiz_answer()

```
function submit_quiz_answer():
    if quiz_index is out of range:
        return

    get user input and convert to lowercase
    get correct word and convert to lowercase

    if user input matches correct word:
        display "Correct" message
        increase score
    else:
        display "Incorrect" and show correct answer

    increase quiz_index by 1
    wait 1 second, then call show_quiz_question()
```

---

### add_flashcard()

```
function add_flashcard():
    get set name, word, and definition

    if word or definition is too long:
        show error and return

    if set doesn't exist:
        create new set

    insert flashcard into database
    clear input fields
    refresh set list
```

---

### delete_flashcard_set()

```
function delete_flashcard_set():
    ask user to confirm deletion

    if confirmed:
        delete all flashcards with that set_id
        delete the flashcard set itself
        reset selection and refresh UI
```

---
