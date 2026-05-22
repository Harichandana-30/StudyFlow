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

        task_list.insert("end", f"ID: {task[0]}\n")
        task_list.insert("end", f"Task: {task[1]}\n")
        task_list.insert("end", f"Subject: {task[2]}\n")
        task_list.insert("end", f"Deadline: {task[3]}\n")

        if task[4] == "Completed":
            task_list.insert("end", "Status: Completed\n", "completed")
        else:
            task_list.insert("end", "Status: Pending\n", "pending")

        task_list.insert("end", "-" * 30 + "\n")

    task_list.tag_config("completed", foreground="lightgreen")
    task_list.tag_config("pending", foreground="red")

    update_progress()
def update_progress():

    tasks = get_tasks()

    total_tasks = len(tasks)

    completed_tasks = 0

    for task in tasks:
        if task[4] == "Completed":
            completed_tasks += 1

    if total_tasks > 0:
        progress = completed_tasks / total_tasks
    else:
        progress = 0

    progress_bar.set(progress)

    progress_label.configure(
        text=f"Progress: {int(progress * 100)}% Completed"
    )

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
task_entry.pack(pady=12)

# Subject input
subject_entry = ctk.CTkEntry(
    left_frame,
    width=350,
    placeholder_text="Enter subject"
)
subject_entry.pack(pady=12)

deadline_frame = ctk.CTkFrame(
    left_frame,
    fg_color="#2b2b2b",
    corner_radius=12
)
deadline_frame.pack(pady=15)

deadline_label = ctk.CTkLabel(
    deadline_frame,
    text="📅 Select Deadline",
    font=("Arial", 16, "bold")
)
deadline_label.pack(pady=(10, 5))

deadline_entry = DateEntry(
    deadline_frame,
    width=22,
    font=("Arial", 12),
    date_pattern="dd-mm-yyyy",
    background="#1f6aa5",
    foreground="white",
    borderwidth=0
)
deadline_entry.pack(pady=(0, 10), padx=15)

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

progress_label = ctk.CTkLabel(
    right_frame,
    text="Progress: 0% Completed",
    font=("Arial", 18, "bold")
)
progress_label.pack(pady=10)

progress_bar = ctk.CTkProgressBar(
    right_frame,
    width=400
)
progress_bar.pack(pady=10)

progress_bar.set(0)

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
update_progress()
# Run app
app.mainloop()