import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox

# List of questions
free_text_questions = [
    "What is your favorite hobby, and can it be done with spaghetti?",
    "What is the best book you have read, and do you think a ghost wrote it?",
    "Where is your dream vacation, and would you go if it was underwater?",
    "What is your favorite movie, and do you think the characters talk to you through popcorn?",
    "What is your favorite food, and would you eat it if it was served in a cloud?",
    "What is the most interesting place you've visited, and do you think aliens built it?",
    "What is the last song you listened to, and could it be a dance spell?",
    "What is one thing you have always wanted to learn, and would it involve teaching squirrels chess?",
    "What is your biggest fear, and does it involve turning into a sock?",
    "What's a fun fact about yourself, and does it involve a secret world in your sock drawer?",
]

multiple_choice_questions = [
    ("Did you eat a cake with peanut butter and socks today?", ["Yes", "No", "Secret"]),
    ("Have you ever sung in the shower while wearing a wig?", ["Yes", "No", "Maybe"]),
    ("Do you believe in aliens that look like potatoes?", ["Yes", "No", "Maybe", "Bogos binted?"]),
    ("Do you like pineapple on pizza with pickles?", ["Yes", "No", "Maybe?"]),
    ("Have you ever been to space and eaten spaghetti?", ["Yes", "No", "I am Elon Musk"]),
    ("Have you ever run a marathon in your pajamas?", ["Yes", "No", "I am marathon"]),
    ("Do you think the moon is made of melted cheese and olives?", ["Yes", "No", "I am cheese"]),
    ("Did you ever dream about a fly making friends with a wasp?", ["Yes", "No", "ZMMM"]),
    ("Have you ever ridden a rollercoaster that goes upside down and sideways?", ["Yes", "No"]),
    ("Do you think time travel is possible if you wear mismatched socks?", ["Yes", "No", "Bogos Binted?"]),
    ("Have you ever made a mud pie with glitter and spaghetti?", ["Yes", "No", "I can't disclose that"]),
    ("Do you like to dance in the rain while wearing a tutu?", ["Yes", "No", "I hate rain"]),
    ("Do you like the smell of freshly cut grass mixed with hot chocolate?", ["Yes", "No", "I am grasscutter"]),
    ("Have you ever tried scuba diving in a bathtub?", ["Yes", "No", "Only in GTAV"]),
    ("Have you ever ridden a horse while wearing a cape?", ["Yes", "No", "Ich bin Pferd"]),
    ("Do you believe in ghosts that wear sunglasses at night?", ["Yes", "No", "Maybe"]),
    ("Do you own a pet that is also your best friend?", ["Yes", "I bark in Times New Roman"]),
    ("Do you play chess with live pieces?", ["Yes", "No", "With your pieces"]),
    ("Do you like to sing in your car while driving backwards?", ["Yes", "No", "Monkey does"]),
    ("Do you think robots will take over the world and start a rock band?", ["Yes", "No", "I am AI??"]),
]

# Randomly select 4-6 questions from both categories
selected_free_text_questions = random.sample(free_text_questions, random.randint(1, 2))
selected_multiple_choice_questions = random.sample(multiple_choice_questions, random.randint(4, 5))

# Combine the selected questions
random_questions = selected_free_text_questions + selected_multiple_choice_questions

# Initialize answers dictionary
answers = {}

# Create the main application window
root = tk.Tk()
root.title("Age Guessing Algorithm App")
root.state('zoomed')  # Set the window to full-screen
root.focus_force()

# Create the main frame
frame = tk.Frame(root, bg="lightblue")
frame.pack(fill="both", expand=True)

# Title label
title_label = tk.Label(frame, text="Answer these questions so I can find your age...", font=("Helvetica", 24, "bold"), bg="lightblue")
title_label.pack(pady=10)

# Questions frame
questions_frame = tk.Frame(frame, bg="lightblue")
questions_frame.pack(pady=10)

# Age question
age_label = tk.Label(questions_frame, text="How old are you?", font=("Helvetica", 18), bg="lightblue")
age_label.grid(row=0, column=0, sticky="w", pady=5)
age_var = tk.StringVar()
age_spinbox = ttk.Spinbox(questions_frame, from_=0, to=120, textvariable=age_var, font=("Helvetica", 14), width=5)
age_spinbox.grid(row=0, column=1, pady=5)

# Generate dynamic questions (multiple-choice or free-text)
question_vars = {}
for idx, question in enumerate(random_questions, start=1):
    if isinstance(question, str):  # Free-text question
        question_label = tk.Label(questions_frame, text=question, font=("Helvetica", 18), bg="lightblue")
        question_label.grid(row=idx, column=0, sticky="w", pady=5)
        question_var = tk.StringVar()
        question_entry = ttk.Entry(questions_frame, textvariable=question_var, font=("Helvetica", 14), width=20)
        question_entry.grid(row=idx, column=1, pady=5)
        question_vars[question] = question_var
    else:  # Multiple-choice question
        question_text, options = question
        question_label = tk.Label(questions_frame, text=question_text, font=("Helvetica", 18), bg="lightblue")
        question_label.grid(row=idx, column=0, sticky="w", pady=5)
        var = tk.StringVar()
        question_vars[question_text] = var
        
        # Place radio buttons in the next available column
        for opt_idx, option in enumerate(options, start=1):
            radio_button = tk.Radiobutton(questions_frame, text=option, variable=var, value=option, font=("Helvetica", 14), bg="lightblue")
            radio_button.grid(row=idx, column=opt_idx, padx=5)

# Next button handler
def handle_next():
    # Validate age input
    if not age_var.get().isdigit() or int(age_var.get()) < 0 or int(age_var.get()) > 120:
        messagebox.showerror("Error", "Please enter a valid age.")
        return

    # Check for unanswered questions (free-text and multiple-choice)
    unanswered = [q for q, var in question_vars.items() if not var.get()]
    if unanswered:
        missing_questions = ', '.join(unanswered)
        messagebox.showerror("Error", f"Please answer all questions! Missing: {missing_questions}")
        return

    # Collect answers
    answers["How old are you?"] = age_var.get()
    for question, var in question_vars.items():
        answers[question] = var.get()

    # Start thinking animation
    thinking_texts = [
        "Decoding neural processes...",
        "Synthesizing conclusions...",
        "Analyzing your answers...",
        "Processing algorithms...",
        "Generating insights...",
        "Correlating data points...",
        "Performing quantum computations...",
        "Gathering cosmic signals...",
        "Finalizing results..."
    ]

    thinking_label = tk.Label(frame, text="", font=("Helvetica", 20, "italic"), fg="blue", bg="lightblue")
    thinking_label.pack(pady=20)

    def cycle_thinking_texts(index=0):
        if index < len(thinking_texts):
            thinking_label.config(text=thinking_texts[index])
            root.after(1000, cycle_thinking_texts, index + 1)
        else:
            display_result()

    cycle_thinking_texts()

# Display the result
def display_result():
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Choose a random question and generate a random irrelevant fact
    answered_questions = [q for q in question_vars if answers[q]]
    chosen_question = random.choice(answered_questions) if answered_questions else "an unanswered question"
    irrelevant_fact = random.choice([
        "you ate a cake with peanut butter.",
        "you believe in unicorns.",
        "you once danced in the rain.",
        "you think time travel is possible.",
        "you enjoy pineapple on pizza.",
        "you are a secret ninja.",
        "you have a hidden talent for juggling.",
        "you dream of being an astronaut.",
        "you think the earth is flat.",
        "you enjoy chocolate ice cream at midnight."
    ])

    # Display result
    tk.Label(frame, text="YOUR AGE IS:", font=("Helvetica", 26, "bold"), fg="green", bg="lightblue").pack(pady=20)
    tk.Label(frame, text=answers["How old are you?"], font=("Helvetica", 40, "bold"), fg="red", bg="lightblue").pack(pady=20)

    result_text = (
        f"Based on your answer to '{chosen_question}'\n"
        f"and the fact that {irrelevant_fact}."
    )
    tk.Label(frame, text=result_text, font=("Helvetica", 20), bg="lightblue", justify="center").pack(pady=10)

# Next button
next_button = tk.Button(frame, text="Next", command=handle_next, font=("Helvetica", 16), bg="lightgreen", activebackground="green")
next_button.pack(pady=20, side="bottom")

# Run the application
root.mainloop()
