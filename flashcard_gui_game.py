import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

# Create database tables if they do not exist
def create_tabels(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flashcard_sets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            set_id INTEGER NOT NULL,
            word TEXT NOT NULL,
            definition TEXT NOT NULL,
            FOREIGN KEY (set_id) REFERENCES flashcard_sets (id)
        )
    ''')
    conn.commit()

def add_flashcard_set(conn, set_name):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO flashcard_sets (name)
        VALUES (?)
    ''', (set_name,))
    conn.commit()
    return cursor.lastrowid

def add_flashcard(conn, set_id, word, definition):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO flashcards (set_id, word, definition)
        VALUES (?, ?, ?)
    ''', (set_id, word, definition))
    conn.commit()
    return cursor.lastrowid

def get_flashcard_sets(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM flashcard_sets')
    rows = cursor.fetchall()
    return {row[1]: row[0] for row in rows}

def get_flashcards(conn, set_id):
    cursor = conn.cursor()
    cursor.execute('SELECT word, definition FROM flashcards WHERE set_id = ?', (set_id,))
    rows = cursor.fetchall()
    return [(row[0], row[1]) for row in rows]

def delete_flashcard_set_data(conn, set_id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM flashcards WHERE set_id = ?', (set_id,))
    conn.commit()

def create_flashcard_set():
    set_name = set_name_vr.get()
    if set_name and set_name not in get_flashcard_sets(conn):
        set_id = add_flashcard_set(conn, set_name)
        populate_sets_combobox()
        set_name_vr.set("")
        word_vr.set("")
        definition_vr.set("")

def add_word():
    set_name = set_name_vr.get()
    word = word_vr.get()
    definition = definition_vr.get()
    if set_name and word and definition:
        sets = get_flashcard_sets(conn)
        set_id = sets.get(set_name) or add_flashcard_set(conn, set_name)
        add_flashcard(conn, set_id, word, definition)
        word_vr.set("")
        definition_vr.set("")
        populate_sets_combobox()

def populate_sets_combobox():
    sets_combobox['values'] = list(get_flashcard_sets(conn).keys())

def delete_flashcard_set():
    set_name = sets_combobox.get()

    if set_name:
        result = messagebox.askyesno(
            'Confirmation', 
            f'Are you sure you want to delete the flashcard set "{set_name}"? This action cannot be undone.'
        )
        if result == tk.YES:
            set_id = get_flashcard_sets(conn)[set_name]
            delete_flashcard_set_data(conn, set_id)
            populate_sets_combobox()
            sets_combobox.set('') # this clears the current selection from the combobox
            clear_flashcards_display() # also clears flashcard text if any

def select_flashcard_set():
    set_name = sets_combobox.get()
    if set_name:
        set_id = get_flashcard_sets(conn)[set_name]
        cards = get_flashcards(conn, set_id)
        if cards:
            display_flashcards(cards)
        else:
            word_label.config(text="No flashcards available in this set.")
            definition_label.config(text="")
    else:
        global current_cards, card_index
        current_cards = []
        card_index = 0
        clear_flashcards_display()

def display_flashcards(cards):
    global card_index, current_cards
    card_index = 0
    current_cards = cards
    if not cards:
        clear_flashcards_display()
    else:
        show_card()

def clear_flashcards_display():
    word_label.config(text="")
    definition_label.config(text="")

def show_card():
    global card_index, current_cards
    if current_cards:
        if 0 <= card_index < len(current_cards):
            word, definition = current_cards[card_index]
            word_label.config(text=word)
            definition_label.config(text="")
        else:
            clear_flashcards_display()
    else:
        clear_flashcards_display()

def flip_flashcard():
    global card_index, current_cards
    if current_cards:
        _, definition = current_cards[card_index]
        definition_label.config(text=definition)

def next_flashcard():
    global card_index, current_cards
    if current_cards:
        card_index = min(card_index + 1, len(current_cards) - 1)
        show_card()

def prev_card():
    global card_index, current_cards
    if current_cards:
        card_index = max(card_index - 1, 0)
        show_card()

# -------------------- GUI SETUP --------------------

if __name__ == "__main__":
    conn = sqlite3.connect('flashcards.db')
    create_tabels(conn)

    root = tk.Tk()
    root.title("Flashcard Quiz Game")
    root.geometry("600x400")

    style = Style(theme='flatly')
    style.configure('TButton', font=('Times New Roman', 16), foreground='white', background='#006778')
    style.map('TButton', background=[('active', '#00703C')])
    style.configure('TLabel', font=('Times New Roman', 16), foreground="#015F33")
    style.configure('TEntry', fieldbackground='#ffffff', foreground='#000000')

    set_name_vr = tk.StringVar()
    word_vr = tk.StringVar()
    definition_vr = tk.StringVar()

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    create_set_frame = ttk.Frame(notebook)
    notebook.add(create_set_frame, text="Create Set")

    ttk.Label(create_set_frame, text="Set Name:").pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=set_name_vr, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text="Word:").pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=word_vr, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text="Definition:").pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=definition_vr, width=30).pack(padx=5, pady=5)

    ttk.Button(create_set_frame, text="Add Word", command=add_word).pack(padx=5, pady=10)
    ttk.Button(create_set_frame, text="Save Set", command=create_flashcard_set).pack(padx=5, pady=10)

    select_set_frame = ttk.Frame(notebook)
    notebook.add(select_set_frame, text="Select Set")

    sets_combobox = ttk.Combobox(select_set_frame, state="readonly")
    sets_combobox.pack(padx=5, pady=5)

    ttk.Button(select_set_frame, text="Select Set", command=select_flashcard_set).pack(padx=5, pady=10)
    ttk.Button(select_set_frame, text="Delete Set", command=delete_flashcard_set).pack(padx=5, pady=10)

    flashcards_frame = ttk.Frame(notebook)
    notebook.add(flashcards_frame, text="Learn Mode")

    card_index = 0
    current_cards = []

    word_label = ttk.Label(flashcards_frame, text=" ", font=("Times New Roman", 24))
    word_label.pack(padx=5, pady=40)

    definition_label = ttk.Label(flashcards_frame, text="", font=("Times New Roman", 16))
    definition_label.pack(padx=5, pady=5)

    ttk.Button(flashcards_frame, text="Flip", command=flip_flashcard).pack(side='left', padx=5, pady=5)
    ttk.Button(flashcards_frame, text="Next", command=next_flashcard).pack(side='right', padx=5, pady=5)
    ttk.Button(flashcards_frame, text="Previous", command=prev_card).pack(side='right', padx=5, pady=5)

    populate_sets_combobox()

    root.mainloop()

