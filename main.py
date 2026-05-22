import customtkinter as ctk

# Theme settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create app window
app = ctk.CTk()

app.title("StudyFlow")
app.geometry("700x500")

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
    width=200
)
add_button.pack(pady=20)

# Run app
app.mainloop()