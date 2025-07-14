import tkinter as tk
import random

# Flashcard data
flashcards = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What does CPU stand for?", "answer": "Central Processing Unit"}
]

random.shuffle(flashcards)

# Flashcard Game GUI
class FlashcardApp:
    def __init__(self, master):
        self.master = master
        master.title("Flashcard Quiz Game")

        self.index = 0
        self.score = 0

        self.question_label = tk.Label(master, text="", font=("Arial", 16), wraplength=400, justify="center")
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(master, font=("Arial", 14))
        self.answer_entry.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=5)

        self.feedback_label = tk.Label(master, text="", font=("Arial", 14))
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack(pady=5)

        self.score_label = tk.Label(master, text="", font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.show_question()

    def show_question(self):
        if self.index < len(flashcards):
            self.question_label.config(text=flashcards[self.index]["question"])
            self.answer_entry.delete(0, tk.END)
            self.feedback_label.config(text="")
        else:
            self.end_game()

    def check_answer(self):
        user_input = self.answer_entry.get().strip().lower()
        correct_answer = flashcards[self.index]["answer"].strip().lower()

        if user_input == correct_answer:
            self.feedback_label.config(text="✅ Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(
                text=f"❌ Incorrect! Correct answer: {flashcards[self.index]['answer']}", fg="red"
            )

    def next_question(self):
        self.index += 1
        self.show_question()

    def end_game(self):
        self.question_label.config(text="🎉 Quiz Complete!")
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()
        self.next_button.pack_forget()
        self.feedback_label.config(text="")
        self.score_label.config(text=f"Final Score: {self.score} / {len(flashcards)}")

# Launch the app
root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()
