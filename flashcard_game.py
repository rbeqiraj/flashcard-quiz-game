import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style
import tkinter.font as tkFont

current_theme = "flatly"  # Start with default light theme

# Create database tabels if they do not exist
def create_tabels(conn):
    cursor = conn.cursor()

    # Create flashcard_sets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flashcard_sets (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL UNIQUE
    )
    ''')
    
    # Create flashcards table with foreign key refrenece to flashcard_sets
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flashcards (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   set_id INTEGER NOT NULL,
                   word TEXT NOT NULL,
                   definition TEXT NOT NULL,
                   FOREIGN KEY (set_id) REFERENCES flashcard_sets (id)
            )
    ''')

    # Add a new flashcard set to the database
def add_flashcard_set(conn, name):
    cursor = conn.cursor()

    # Insert the set name into flashcard_sets table
    cursor.execute('''
        INSERT INTO flashcard_sets (name)
         VALUES (?)
    ''', (name,))

    set_id = cursor.lastrowid
    conn.commit()
    
    return set_id

# Function to add a flashcard to the database
def add_flashcard(conn, set_id, word, definition):
    cursor = conn.cursor()

    # Execute SQL query to insert a new flashcard into the database
    cursor.execute('''
        INSERT INTO flashcards (set_id, word, definition)
        VALUES (?, ?, ?)   
    ''', (set_id, word, definition))

    # Get the ID of the newly added flashcard
    card_id = cursor.lastrowid
    conn.commit()

    return card_id

# Function to retrieve all flashcard sets from the database
def get_sets(conn):
    cursor = conn.cursor()

    # Execute SQL query to select all flashcard sets
    cursor.execute('''
        SELECT id, name FROM flashcard_sets
    ''')
    
    rows = cursor.fetchall()
    sets = {row[1]: row[0] for row in rows}  # Create a dictionary of sets with ID as key and name as value
  
    return sets

# Function to retrieve flashcards for a specific set
def get_flashcards(conn, set_id):
    cursor = conn.cursor()

    cursor.execute('''
        SELECT word, definition FROM flashcards 
        WHERE set_id = ?
    ''', (set_id,))

    rows = cursor.fetchall()
    flashcards = [(row [0], row[1]) for row in rows]  # Create a list of flashcards (word, definition
    
    return flashcards

# Function to delete a flashcard set from the database - ISSUE OCCURED WHEN TRYING TO DELETE A SET

def delete_flashcard_set(conn, set_id):
    cursor = conn.cursor()

    # First delete the flashcards in that set
    cursor.execute('''
        DELETE FROM flashcards
        WHERE set_id = ?
    ''', (set_id,)) 

    # Then delete the flashcard set itself
    cursor.execute('''
        DELETE FROM flashcard_sets
        WHERE id = ?
    ''', (set_id,))

    conn.commit()

    # Clear UI and refresh
    sets_combobox.set('')  
    clear_flashcards_display()
    populate_sets_combobox()

    # Clear the current_cards list and reset the card_index - The UI wasn't refreshing properly after deleting a set so adding these lines of code fixed the issue.
    global current_cards, card_index
    current_cards = []
    card_index = 0

# Function to create a new flashcard set 
def create_flashcard_set():
    set_name = set_name_var.get()
    if set_name:
         if set_name not in get_sets(conn):
            set_id = add_flashcard_set(conn, set_name)
            populate_sets_combobox()
            set_name_var.set('') 
            
            # Clear the input fields
            set_name_var.set('')
            word_var.set('')
            definition_var.set('')

def load_demo_set():
    demo_name = "Demo"
    if demo_name not in get_sets(conn):
        set_id = add_flashcard_set(conn, demo_name)
        add_flashcard(conn, set_id, "Flip", "Click the flip button to see the definition.")
        add_flashcard(conn, set_id, "Next", "Use next to see the next card.")
        add_flashcard(conn, set_id, "Enjoy!", "You're ready to study.")
    populate_sets_combobox()
    sets_combobox.set(demo_name)
    select_flashcard_set()

        
def add_word():
    set_name = set_name_var.get()
    word = word_var.get()
    definition = definition_var.get()

    if len(word) > 30:
        messagebox.showerror("Too Long", "Word must be under 30 characters.")
        return

    if len(definition) > 100:
        messagebox.showerror("Too Long", "Definition must be under 100 characters.")
        return

    if set_name and word and definition:
        if set_name not in get_sets(conn):
            set_id = add_flashcard_set(conn, set_name)
        else:
            set_id = get_sets(conn)[set_name]

        add_flashcard(conn, set_id, word, definition)

        word_var.set("")
        definition_var.set("")
        
        populate_sets_combobox()

def populate_sets_combobox():
     sets_combobox['values'] = tuple(get_sets(conn).keys())

    # Function to delete a selected flashcard set
def handle_delete_flashcard_set():
    set_name = sets_combobox.get()

    if set_name:
        result = messagebox.askyesno(
            'Confirmation', f'Are you sure you want to delete the flashcard set "{set_name}"? This action cannot be undone.'
        )

        if result == tk.YES:
            set_id = get_sets(conn)[set_name]
            delete_flashcard_set(conn, set_id)
            populate_sets_combobox()
            clear_flashcards_display()

def select_flashcard_set():
    global current_cards, card_index
    set_name = sets_combobox.get()

    if set_name:
        set_id = get_sets(conn)[set_name]
        cards = get_flashcards(conn, set_id)
                          
        if cards:
            current_cards = cards  # Store cards globally for use in quiz too
            card_index = 0
            display_flashcards(cards)
        else:
            word_label.config(text="No flashcards in this set.")
            definition_label.config(text="")
    else:
        current_cards = []
        card_index = 0  
        clear_flashcards_display()


def display_flashcards(cards):
    global card_index
    global current_cards

    card_index = 0
    current_cards = cards
    quiz_cards = []
    quiz_index = 0
    quiz_score = 0

    # Clear the display
    if not cards:
        clear_flashcards_display()
    else:
        show_card()

    show_card()

def create_flashcard_display():
    word_label.config(text= '')
    definition_label.config(text='')

def apply_theme():
    global current_theme, style
    selected = theme_var.get()
    current_theme = selected
    style = Style(theme=selected)

    # Reapply custom styling (optional)
    style.configure('TButton', font=('Times New Roman', 16), foreground='white', background='#006778')
    style.map('TButton', background=[('active', '#00703C')])
    style.configure('TLabel', font=('Times New Roman', 16), foreground="#015F33")
    style.configure('TEntry', fieldbackground='#ffffff', foreground='#000000')


# Function to display the current flashcards word
def show_card():    
    global card_index
    global current_cards

    if current_cards:
        if 0 <= card_index < len(current_cards):
            word, _ = current_cards[card_index]
            word_label.config(text=word)
            definition_label.config(text='')
        else:
            clear_flashcards_display()
    else:
        clear_flashcards_display()

# Function to flip the current card and display its definition
def flip_flashcard():
    global card_index
    global current_cards

    if current_cards:
       _, definition = current_cards[card_index]
    definition_label.config(text=definition)
    
# Function to move to the next card
def next_flashcard():
    global card_index
    global current_cards

    if current_cards:
        card_index = min(card_index + 1, len(current_cards) - 1)
        show_card()

# Function to move to the previous card
def prev_flashcard():
    global card_index
    global current_cards

    if current_cards:
        card_index = max(card_index - 1, 0)
        show_card()

import random
mc_cards = []
mc_index = 0
mc_score = 0
correct_mc_answer = ""

def start_quiz():
    global quiz_cards, quiz_index, quiz_score
    set_name = sets_combobox.get()

    if not set_name:
        messagebox.showerror("No Set Selected", "Please select a flashcard set first.")
        return

    sets_dict = get_sets(conn)
    if set_name not in sets_dict:
        messagebox.showerror("Set Error", "Selected set not found.")
        return

    set_id = sets_dict[set_name]
    quiz_cards = get_flashcards(conn, set_id)

    if not quiz_cards:
        messagebox.showinfo("Empty Set", "This set has no flashcards.")
        return

    quiz_index = 0
    quiz_score = 0
    quiz_input.config(state="normal")  # Allow input
    submit_button.config(state="normal")  # Re-enable Submit
    show_quiz_question()


def show_quiz_question():
    if 0 <= quiz_index < len(quiz_cards):
        definition = quiz_cards[quiz_index][1]
        quiz_def_label.config(text=f"Definition:\n{definition}")
        quiz_input.delete(0, tk.END)
        quiz_feedback_label.config(text="")
    else:
        quiz_def_label.config(text="Quiz Complete!")
        quiz_feedback_label.config(text=f"Your Score: {quiz_score}/{len(quiz_cards)}")
        quiz_input.config(state="disabled")
        submit_button.config(state="disabled")
        
def submit_quiz_answer():
    global quiz_index, quiz_score, quiz_cards

    if quiz_index >= len(quiz_cards):
        return  # Prevent going out of range

    user_input = quiz_input.get().strip().lower()
    correct_word = quiz_cards[quiz_index][0].strip().lower()

    if user_input == correct_word:
        quiz_feedback_label.config(text="✅ Correct!", foreground="green")
        quiz_score += 1
    else:
        quiz_feedback_label.config(text=f"❌ Incorrect. Answer: {correct_word}", foreground="red")

    quiz_index += 1
    root.after(1000, show_quiz_question)


if __name__ == "__main__":
    # Connect to the SQLite database and create tabels 
    conn = sqlite3.connect('flashcards.db')
    create_tabels(conn)

    # Create the main GUI window
    root = tk.Tk()
    root.title("Flashcard Quiz Game")
    root.geometry("600x400")

    # Define theme_var for theme selection
    theme_var = tk.StringVar(value=current_theme)

    # Apply styling to the GUI elements
    style = Style(theme='flatly')

    # FGCU CUSTOM COLORS
    style.configure('TButton', font=('Times New Roman', 16), foreground = 'white', background = '#006778') # FGCU Blue
    style.map('TButton', background=[('active', '#00703C')])  # FGCU Green on hover

    style.configure('TLabel', font=('Times New Roman', 16), foreground = "#015F33") # FGCU Green 
    style.configure('TEntry', fieldbackground='#ffffff', foreground = '#000000') #optional: white entry field

    # Storing user input and feedback
    set_name_var = tk.StringVar()
    word_var = tk.StringVar()
    definition_var = tk.StringVar()  

    # Create a notebook for manage tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create the "Create Flashcard Set" tab and its content
    create_set_frame = ttk.Frame(notebook)
    notebook.add(create_set_frame, text= "Create Set" )

    # Label and Entry widget for entering the flashcard set name, word and definition
    ttk.Label(create_set_frame, text= "Set Name: ").pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=set_name_var, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text= "Word: ").pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=word_var, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text= "Definition: ").pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=definition_var, width=30).pack(padx=5, pady=5)

    # Button to add a word to the set 
    ttk.Button(create_set_frame, text="Add Word", command=add_word).pack(padx=5, pady=10)

    # Button to save the set
    ttk.Button(create_set_frame, text="Save Set", command=create_flashcard_set).pack(padx=5, pady=10) 
    
    # Create the "Select Set" tab and its content
    select_set_frame = ttk.Frame(notebook)
    notebook.add(select_set_frame, text="Select Set")

    # Combobox widget for selecting existing flashcard sets
    sets_combobox = ttk.Combobox(select_set_frame, state="readonly", )
    sets_combobox.pack(padx=5, pady=40)
    sets_combobox.bind("<<ComboboxSelected>>", lambda e: select_flashcard_set())

    # Button to select a set
    ttk.Button(select_set_frame, text="Select Set", command=select_flashcard_set).pack(padx=5, pady=5)
     
    # Button to delete a flashcard set
    ttk.Button(select_set_frame, text="Delete Set", command=handle_delete_flashcard_set).pack(padx=5, pady=5)   

    #Create the "Learn Mode" tab and its content
    flashcards_frame = ttk.Frame(notebook)
    notebook.add(flashcards_frame, text="Learn Mode")

    # Create the "Quiz Mode" tab and its content
    quiz_frame = ttk.Frame(notebook)
    notebook.add(quiz_frame, text="Quiz Mode")

    # Label to display the definition/question in quiz mode
    quiz_def_label = ttk.Label(quiz_frame, text="", font=("Times New Roman", 16))
    quiz_def_label.pack(padx=5, pady=20)

    # Entry for user to input their answer
    quiz_input = ttk.Entry(quiz_frame, width=30)
    quiz_input.pack(padx=5, pady=5)

    # Feedback label for quiz answers
    quiz_feedback_label = ttk.Label(quiz_frame, text="", font=("Times New Roman", 14))
    quiz_feedback_label.pack(padx=5, pady=5)

    # Button to submit quiz answer
    submit_button = ttk.Button(quiz_frame, text="Submit", command=submit_quiz_answer)
    submit_button.pack(padx=5, pady=10)

    # Button to start quiz
    ttk.Button(quiz_frame, text="Start Quiz", command=start_quiz).pack(padx=5, pady=10)

    # Create the "Settings" tab
    settings_frame = ttk.Frame(notebook)
    notebook.add(settings_frame, text="Settings")

    # Label for theme selector
    ttk.Label(settings_frame, text="Choose a Theme:").pack(pady=10)

    # Dropdown of available themes
    theme_var = tk.StringVar()
    theme_combobox = ttk.Combobox(settings_frame, textvariable=theme_var, state="readonly")
    theme_combobox['values'] = ("flatly", "darkly", "superhero", "journal", "morph")
    theme_combobox.current(0)  # Default to first option
    theme_combobox.pack(pady=5)

    # Apply theme button
    ttk.Button(settings_frame, text="Apply Theme", command=apply_theme).pack(pady=10)

    # Initialize the flashcards list for tracking card index and current cards
    card_index = 0
    current_tabs = []   

    # Label to display the word on flashcards
    word_label = ttk.Label(flashcards_frame, text=" ", font=("Times New Roman", 24))
    word_label.pack(padx=5, pady=40, anchor='center')

    # Label to display the definition on flashcards
    definition_label = ttk.Label(flashcards_frame, text="")
    definition_label.pack(padx=5, pady=5, anchor='center')

    # Create a frame to hold the navigation buttons
    nav_frame = ttk.Frame(flashcards_frame)
    nav_frame.pack(pady=20)

    # Button to flip the flashcard 
    ttk.Button(flashcards_frame, text="Flip", command=flip_flashcard).pack(side='left', padx=5,)
        
    # Button to view the next flashcard
    ttk.Button(flashcards_frame, text="Next", command=next_flashcard).pack(side='right', padx=5,)

    # Button to view the previous flashcard
    ttk.Button(flashcards_frame, text="Previous", command=prev_flashcard).pack(side='right', padx=5,)

    # Button to load a demo flashcard set
    ttk.Button(select_set_frame, text="Load Demo", command=load_demo_set).pack(padx=5, pady=5)

# Function to clear the flashcards display
def clear_flashcards_display():
    word_label.config(text="")
    definition_label.config(text="")

# Populate dropdown at startup
populate_sets_combobox()

# After you call populate_sets_combobox()
if sets_combobox['values']:
    sets_combobox.set(sets_combobox['values'][0])  # Auto-select first set

# Start the GUI loop
root.mainloop()

