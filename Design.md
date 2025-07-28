# Design Overview

## Overview
The Flashcard Quiz Game is an interactive GUI application built with Python using `tkinter` and `ttkbootstrap`. It allows users to create, manage, and quiz themselves on custom flashcard sets.

---

## 🖥️ Key Features

- Create flashcard sets with custom words and definitions
- Store flashcards using SQLite
- Learn mode: flip through flashcards and view definitions
- Quiz mode: test knowledge by typing answers and receiving feedback
- Theme settings with Bootstrap-inspired themes
- Character limits to improve UX (30 for words, 100 for definitions)
- Demo mode with preloaded cards
- Visual feedback for correct/incorrect answers
- Responsive styling using `ttkbootstrap` themes (Flatly, Darkly, Superhero, etc.)

---

## Modules Used

- `tkinter` – GUI framework
- `ttkbootstrap` – Styled widget theme
- `sqlite3` – Local database
- `tkinter.font` – Font customization

---

## GUI Layout

**Tabs:**
- `Create Set`: Add new sets, words, and definitions
- `Select Set`: Choose a set and delete or load demo cards
- `Learn Mode`: Flip through cards to learn
- `Quiz Mode`: Input answers and get feedback
- `Settings`: Change the theme

---

## Quiz Logic

- Quiz pulls cards from the selected set
- Compares user input (case-insensitive) with correct word
- Tracks score and provides visual feedback
- Disables quiz input after completion

---

## Theme Support

Users can choose from:
- Flatly (default)
- Darkly
- Superhero
- Journal
- Morph

---

## Database Schema

- **flashcard_sets**: `(id, name)`
- **flashcards**: `(id, set_id, word, definition)`

---

## To Do / Improvements

- Add font customization (coming soon)
- Export/import flashcards
- Flashcard progress tracking
