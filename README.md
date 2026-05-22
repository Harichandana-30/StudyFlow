# StudyFlow

StudyFlow is a modern desktop-based study planner application developed using **Python**, **CustomTkinter**, and **SQLite**. The application is designed to help students efficiently manage their academic tasks, organize study schedules, monitor deadlines, and track overall study progress.

The main objective of StudyFlow is to provide a clean, simple, and interactive platform where students can manage their study workflow without confusion. The application offers task organization, deadline tracking, progress monitoring, and productivity-based features in one place.

---

## Project Overview

Managing studies across multiple subjects can often become difficult, especially when deadlines and pending work start increasing. StudyFlow was developed to solve this problem by allowing users to maintain all study-related tasks in a structured manner.

Using StudyFlow, students can:

- Add and organize study tasks
- Assign subjects to each task
- Set deadlines using an interactive calendar
- Mark completed tasks
- Monitor pending work
- Search tasks quickly
- View study statistics
- Track consistency through streak counting

The application stores all task information locally using SQLite database integration, ensuring data persistence even after closing the program.

---

## Features

### 1. Task Management

StudyFlow allows users to create and manage study tasks effectively.

Features include:

- Add study tasks
- Assign subjects to tasks
- Delete unnecessary tasks
- Mark tasks as completed
- View task information in an organized format

Each task contains:

- Task ID
- Task Name
- Subject Name
- Deadline
- Completion Status

---

### 2. Deadline Management

The application includes a deadline tracking system to help students stay consistent.

Features:

- Select deadlines using an interactive calendar
- Automatically store deadlines
- View deadlines inside task display section
- Receive upcoming deadline warnings

Example warning:

```txt
Upcoming Deadline: Revise DBMS
```

This helps students avoid missing important study schedules.

---

### 3. Progress Tracking

StudyFlow visually tracks study progress using a progress bar.

The application automatically calculates:

- Total completed tasks
- Pending tasks
- Percentage of completed work

Example:

```txt
Progress: 50% Completed
```

This feature helps students understand how much work has been finished.

---

### 4. Dashboard Statistics

A dashboard section is available to provide quick statistics.

The dashboard displays:

- Total Tasks
- Completed Tasks
- Pending Tasks

Example:

```txt
Total: 3
Completed: 2
Pending: 1
```

This provides a quick overview of academic progress.

---

### 5. Search Functionality

Users can search tasks by subject name.

Example:

```txt
Python
```

The application filters and displays only relevant tasks.

This makes it easier to focus on one subject at a time.

---

### 6. Study Streak Counter

StudyFlow includes a study streak feature that helps users remain motivated.

Features:

- Tracks consistency
- Updates streak count after task completion
- Encourages regular studying

Example:

```txt
Study Streak: 2 Days
```

---

### 7. Theme Customization

StudyFlow includes both:

- Dark Mode
- Light Mode

Users can switch themes dynamically according to preference.

This improves user experience and interface flexibility.

---

### 8. Modern User Interface

The application is built using **CustomTkinter** to provide a modern desktop UI.

UI improvements include:

- Rounded buttons
- Modern input fields
- Dashboard design
- Organized layout
- Scrollable sections
- Clean spacing and alignment

---

## Application Preview

![StudyFlow Preview](studyflow-preview.png)

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| CustomTkinter | GUI design |
| SQLite | Database management |
| TkCalendar | Deadline selection |
| Git & GitHub | Version control |

---

## Project Structure

```txt
StudyFlow/
│── main.py
│── database.py
│── requirements.txt
│── README.md
│── .gitignore
│── streak.txt
│── studyflow-preview.png
```

### File Description

#### `main.py`
Contains the main user interface and application logic.

#### `database.py`
Handles database-related operations such as:

- Creating database
- Adding tasks
- Deleting tasks
- Updating task completion
- Searching tasks

#### `requirements.txt`
Contains all required Python packages.

#### `streak.txt`
Stores study streak count.

#### `studyflow-preview.png`
Contains application preview image.

---

## Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/Harichandana-30/StudyFlow.git
```

### Step 2: Open Project Folder

```bash
cd StudyFlow
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python main.py
```

---

## How to Use

### Adding a Task

1. Enter task name
2. Enter subject name
3. Select deadline
4. Click **Add Task**

---

### Completing a Task

1. Enter task ID
2. Click **Mark Completed**

---

### Deleting a Task

1. Enter task ID
2. Click **Delete Task**

---

### Searching Tasks

1. Enter subject name
2. Click **Search Subject**
3. Click **Show All Tasks**

---

### Changing Theme

Click the theme toggle button to switch between:

- Dark Mode
- Light Mode

---

## Future Improvements

Planned features for future versions:

- Study analytics charts
- Reminder notifications
- Login system
- Export reports
- Cloud synchronization
- AI-powered study recommendations

---

## Learning Outcomes

This project helped in learning:

- Python GUI Development
- SQLite Database Integration
- File Handling
- Event-Driven Programming
- UI Design Principles
- Git and GitHub Workflow
- Application Structuring

---

## Author

**Hari Chandana**

GitHub Repository:  
https://github.com/Harichandana-30/StudyFlow

StudyFlow was developed as a productivity-focused desktop application to improve study planning and task management.