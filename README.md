Flashcard Quiz Game coded in Python
# Flashcard Quiz Game

A GUI-based flashcard application built with Python, SQLite, and Tkinter (with ttkbootstrap) to help users study using flashcards in **Learn Mode** or **Quiz Mode**. Users can create sets, add flashcards, test their memory, and even switch themes for a personalized experience.

---

## Features

- Create, save, and delete flashcard sets
- Add flashcards with word/definition pairs
- Learn Mode with flip & navigation buttons
- Quiz Mode with input-based scoring
- Streak counter & score tracking
- Demo set for first-time users
- Light/Dark themes with ttkbootstrap

---

## Technologies Used

- Python 3.x
- Tkinter
- ttkbootstrap (for styling)
- SQLite (local database)

---

## Folder Structure

```
flashcard-quiz-game/
│
├── flashcard_game.py           # Main app logic
├── flashcard_gui_game.py       # GUI structure (Tkinter)
├── flashcards.db               # SQLite database
├── README.md                   # This file
└── assets/                     # Images or themes (optional)
```

---

## Setup Instructions

### 1. Install Required Software

#### Install Python
- Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Install the latest version for your OS
- **IMPORTANT:** ✅ During installation, check the box that says **“Add Python to PATH”**

#### Install VS Code
- Download from: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Install it and open it once to complete setup

---

### 2. Clone This Project from GitHub

#### Option A: Using VS Code GUI
- Open VS Code
- Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac)
- Type: `Git: Clone`
- Paste this link:

```bash
https://github.com/rbeqiraj/flashcard-quiz-game.git


1. Clone this repo (Mac Users):

###   git clone https://github.com/rbeqiraj/flashcard-quiz-game.git
   
   cd flashcard-quiz-game

2. Install dependencies (optional):
   pip install ttkbootstrap (Needs to be installed via pip)
   sqlite3 is built into Python - no install needed

4. Run the app:
   python flashcard_game.py


---

## How to Use

1. Go to the **Create Set** tab to name your set and add flashcards.
2. Switch to **Select Set** to choose a set and load it.
3. Use **Learn Mode** to flip and review cards.
4. Use **Quiz Mode** to test your knowledge and get scored.
5. Switch themes in **Settings** to customize the look.

---

## Acknowledgments

- FGCU – Intro to Computer Science (COP 1500)
- ttkbootstrap by Tom Schaul – [GitHub](https://github.com/israel-dryer/ttkbootstrap)
- https://www.youtube.com/watch?v=eOdbvneI33M
- https://discord.gg/python

---

## License

This project is licensed for educational use.

---
