import customtkinter as ctk
from database import create_database, add_task, get_tasks
# Theme settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create app window
app = ctk.CTk()

app.title("StudyFlow")
app.geometry("700x500")

def save_task():
    task = task_entry.get()
    subject = subject_entry.get()

    if task and subject:
        add_task(task, subject)

        task_entry.delete(0, "end")
        subject_entry.delete(0, "end")

        display_tasks()

def display_tasks():

    task_list.delete("0.0", "end")

    tasks = get_tasks()

    for task in tasks:
        task_text = (
            f"Task: {task[1]}\n"
            f"Subject: {task[2]}\n"
            f"Status: {task[3]}\n"
            f"{'-'*30}\n"
        )

        task_list.insert("end", task_text)

# Heading
heading = ctk.CTkLabel(
    app,
    text="StudyFlow",
    font=("Arial", 30, "bold")
)
heading.pack(pady=20)

# Subtitle
subtitle = ctk.CTkLabel(
    app,
    text="Plan Your Study Tasks",
    font=("Arial", 16)
)
subtitle.pack(pady=5)

# Task input
task_entry = ctk.CTkEntry(
    app,
    width=350,
    placeholder_text="Enter study task"
)
task_entry.pack(pady=10)

# Subject input
subject_entry = ctk.CTkEntry(
    app,
    width=350,
    placeholder_text="Enter subject"
)
subject_entry.pack(pady=10)

# Add task button
add_button = ctk.CTkButton(
    app,
    text="Add Task",
    width=200,
    command=save_task
)
task_list = ctk.CTkTextbox(
    app,
    width=500,
    height=200
)
task_list.pack(pady=20)
add_button.pack(pady=20)

create_database()
display_tasks()
# Run app
app.mainloop()