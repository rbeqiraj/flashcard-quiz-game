# Part D – Flowcharts

This section includes flowcharts describing the main program logic and individual functions in the Flashcard Quiz Game.

+-----------------------------+
|   Start start_quiz()        |
+-----------------------------+
           |
           v
+-----------------------------+
| Get selected flashcard set |
+-----------------------------+
           |
           v
+-----------------------------+
| Fetch flashcards from DB   |
+-----------------------------+
           |
           v
+-----------------------------+
| If empty: show message     |
+-----------------------------+
           |
           v
+-----------------------------+
| Initialize quiz variables  |
+-----------------------------+
           |
           v
|  Call show_quiz_question() |
+-----------------------------+


--


+------------------------------------+
|     Start submit_quiz_answer()     |
+------------------------------------+
                |
                v
+------------------------------------+
|  Get and lowercase user input      |
+------------------------------------+
                |
                v
+------------------------------------+
| Get correct answer and lowercase  |
+------------------------------------+
                |
                v
+------------------------------------+
|  Compare input == correct answer   |
+------------------------------------+
         | True             | False
         v                  v
+----------------+    +----------------------+
| Show ✅ Correct |    | Show ❌ Incorrect     |
+----------------+    +----------------------+
         |                  |
         +--------+---------+
                  |
                  v
+------------------------------------+
|  Increment index & call next card  |
+------------------------------------+
