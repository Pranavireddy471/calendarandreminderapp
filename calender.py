import tkinter as tk
from tkinter import messagebox, simpledialog
import calendar
import datetime

# Dictionary to store reminders
reminders = {}

# Function to show the calendar
def show_calendar(year, month):
    for widget in calendar_frame.winfo_children():
        widget.destroy()

    cal = calendar.monthcalendar(year, month)
    tk.Label(calendar_frame, text=f"{calendar.month_name[month]} {year}", font=("Arial", 16, "bold"), bg="#d1c4e9").grid(row=0, column=0, columnspan=7, pady=10)

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for idx, day in enumerate(days):
        tk.Label(calendar_frame, text=day, font=("Arial", 12, "bold"), bg="#b39ddb", width=6).grid(row=1, column=idx)

    for row_idx, week in enumerate(cal, start=2):
        for col_idx, day in enumerate(week):
            if day == 0:
                tk.Label(calendar_frame, text="", width=6).grid(row=row_idx, column=col_idx)
            else:
                btn = tk.Button(calendar_frame, text=str(day), width=6,
                                command=lambda d=day: open_reminder_window(year, month, d))
                date_key = f"{year}-{month:02d}-{day:02d}"
                if date_key in reminders:
                    btn.config(bg="#f48fb1")  # Highlight if reminder exists
                btn.grid(row=row_idx, column=col_idx)

# Function to open reminder window
def open_reminder_window(year, month, day):
    date_str = f"{year}-{month:02d}-{day:02d}"
    reminder_text = reminders.get(date_str, "")
    new_reminder = simpledialog.askstring("Set Reminder", f"Reminder for {date_str}:", initialvalue=reminder_text)
    if new_reminder is not None:
        if new_reminder.strip():
            reminders[date_str] = new_reminder
        elif date_str in reminders:
            del reminders[date_str]
        show_calendar(year, month)

# Function to navigate months
def next_month():
    global current_year, current_month
    if current_month == 12:
        current_month = 1
        current_year += 1
    else:
        current_month += 1
    show_calendar(current_year, current_month)

def prev_month():
    global current_year, current_month
    if current_month == 1:
        current_month = 12
        current_year -= 1
    else:
        current_month -= 1
    show_calendar(current_year, current_month)

# Main window
root = tk.Tk()
root.title("📅 Calendar & Reminder App")
root.geometry("500x500")
root.configure(bg="#ede7f6")

top_frame = tk.Frame(root, bg="#ede7f6")
top_frame.pack(pady=10)

tk.Button(top_frame, text="<< Previous", command=prev_month, bg="#9575cd", fg="white", font=("Arial", 10)).grid(row=0, column=0, padx=10)
tk.Button(top_frame, text="Next >>", command=next_month, bg="#9575cd", fg="white", font=("Arial", 10)).grid(row=0, column=1, padx=10)

calendar_frame = tk.Frame(root, bg="#ede7f6")
calendar_frame.pack()

# Initial date
today = datetime.date.today()
current_year = today.year
current_month = today.month

show_calendar(current_year, current_month)

root.mainloop()
