import customtkinter as ctk
from tkcalendar import DateEntry
from database import (
    create_database,
    add_task,
    get_tasks,
    complete_task,
    delete_task
)
# Theme settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create app window
app = ctk.CTk()
main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

left_frame = ctk.CTkFrame(main_frame)
left_frame.pack(side="left", fill="both", padx=20, pady=20)

right_frame = ctk.CTkFrame(main_frame)
right_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

app.title("StudyFlow")
app.geometry("1000x700")

def save_task():
    task = task_entry.get()
    subject = subject_entry.get()
    deadline = deadline_entry.get()

    if task and subject:
        add_task(task, subject, deadline)

        task_entry.delete(0, "end")
        subject_entry.delete(0, "end")

        display_tasks()

def mark_completed():
    task_id = task_id_entry.get()

    if task_id:
        complete_task(int(task_id))

        task_id_entry.delete(0, "end")

        display_tasks()


def remove_task():
    task_id = task_id_entry.get()

    if task_id:
        delete_task(int(task_id))

        task_id_entry.delete(0, "end")

        display_tasks()

def display_tasks():

    task_list.delete("0.0", "end")

    tasks = get_tasks()

    for task in tasks:
        task_text = (
    f"ID: {task[0]}\n"
    f"Task: {task[1]}\n"
    f"Subject: {task[2]}\n"
    f"Deadline: {task[3]}\n"
    f"Status: {task[4]}\n"
    f"{'-'*30}\n"
)

        task_list.insert("end", task_text)

# Heading
heading = ctk.CTkLabel(
    left_frame,
    text="StudyFlow",
    font=("Arial", 30, "bold")
)
heading.pack(pady=20)

# Subtitle
subtitle = ctk.CTkLabel(
    left_frame,
    text="Plan Your Study Tasks",
    font=("Arial", 16)
)
subtitle.pack(pady=5)

# Task input
task_entry = ctk.CTkEntry(
    left_frame,
    width=350,
    placeholder_text="Enter study task"
)
task_entry.pack(pady=10)

# Subject input
subject_entry = ctk.CTkEntry(
    left_frame,
    width=350,
    placeholder_text="Enter subject"
)
subject_entry.pack(pady=10)

deadline_label = ctk.CTkLabel(
    left_frame,
    text="Select Deadline"
)
deadline_label.pack(pady=5)

deadline_entry = DateEntry(
    left_frame,
    width=25,
    background="darkblue",
    foreground="white",
    borderwidth=2
)
deadline_entry.pack(pady=10)

task_id_entry = ctk.CTkEntry(
    left_frame,
    width=350,
    placeholder_text="Enter Task ID"
)
task_id_entry.pack(pady=10)

# Add task button
add_button = ctk.CTkButton(
    left_frame,
    text="Add Task",
    width=200,
    command=save_task
)
add_button.pack(pady=20)

complete_button = ctk.CTkButton(
    left_frame,
    text="Mark Completed",
    command=mark_completed
)
complete_button.pack(pady=5)

delete_button = ctk.CTkButton(
    left_frame,
    text="Delete Task",
    command=remove_task
)
delete_button.pack(pady=5)

task_label = ctk.CTkLabel(
    right_frame,
    text="Your Study Tasks",
    font=("Arial", 24, "bold")
)
task_label.pack(pady=10)

task_list = ctk.CTkTextbox(
    right_frame,
    width=500,
    height=550
)
task_list.pack(pady=20)
create_database()
display_tasks()
# Run app
app.mainloop()