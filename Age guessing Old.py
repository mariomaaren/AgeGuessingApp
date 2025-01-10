import tkinter as tk
from tkinter import ttk
import random

# List of questions
questions = [
    "Did you eat a cake with peanut butter today?",
    "Have you ever sung in the shower?",
    "Do you believe in aliens?",
    "Do you like pineapple on pizza?",
    "Have you ever been to space?",
    "Have you ever run a marathon?",
    "Do you think the moon is made of cheese?",
    "Did you ever dream about flying?",
    "Have you ever ridden a rollercoaster?",
    "Do you think time travel is possible?",
    "Have you ever made a mud pie?",
    "Do you like to dance in the rain?",
    "Do you like the smell of freshly cut grass?",
    "Have you ever tried scuba diving?",
    "Have you ever ridden a horse?",
    "Do you believe in ghosts?",
    "Do you own a pet?",
    "Do you play chess?",
    "Do you like to sing in your car?",
    "Do you think robots will take over the world?"
]

# Randomly select 4-6 questions
random_questions = random.sample(questions, random.randint(4, 6))

# Initialize answers dictionary
answers = {}

# Create the main application window
root = tk.Tk()
root.title("Age Guessing App")
root.state('zoomed')  # Set the window to full-screen
root.focus_force()

# Create the main frame
frame = tk.Frame(root, bg="lightblue")
frame.pack(fill="both", expand=True)

# Title label
title_label = tk.Label(frame, text="I can guess your age!", font=("Helvetica", 24, "bold"), bg="lightblue")
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

# Generate irrelevant questions dynamically
question_vars = {}
for idx, question in enumerate(random_questions, start=1):
    question_label = tk.Label(questions_frame, text=question, font=("Helvetica", 18), bg="lightblue")
    question_label.grid(row=idx, column=0, sticky="w", pady=5)
    question_var = tk.StringVar()
    question_entry = ttk.Entry(questions_frame, textvariable=question_var, font=("Helvetica", 14), width=20)
    question_entry.grid(row=idx, column=1, pady=5)
    question_vars[question] = question_var

# Next button handler
def handle_next():
    # Validate answers
    if not age_var.get().isdigit() or int(age_var.get()) < 0 or int(age_var.get()) > 120:
        tk.messagebox.showerror("Error", "Please enter a valid age.")
        return

    unanswered = [q for q, var in question_vars.items() if not var.get()]
    if unanswered:
        tk.messagebox.showerror("Error", f"Please answer all questions! Missing: {', '.join(unanswered)}")
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