import calendar
import sqlite3
from persiantools.jdatetime import JalaliDate

# Persian month names in Fingilish
persian_months = {
    1: "Farvardin", 2: "Ordibehesht", 3: "Khordad", 4: "Tir",
    5: "Mordad", 6: "Shahrivar", 7: "Mehr", 8: "Aban",
    9: "Azar", 10: "Dey", 11: "Bahman", 12: "Esfand"
}

# SQLite Database Setup
conn = sqlite3.connect("work_schedule.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS work_schedule (
    date TEXT PRIMARY KEY,
    shift_name TEXT,
    start_time TEXT,
    end_time TEXT
)
""")
conn.commit()

def get_month_weeks(year, month):
    """Get the list of weeks in a given month with weekdays"""
    weeks = calendar.monthcalendar(year, month)
    return [[(calendar.day_name[calendar.weekday(year, month, day)], day) if day != 0 else ("", 0) for day in week] for week in weeks]

def display_months():
    """Display months for selection"""
    for num, name in persian_months.items():
        print(f"{num}: {name}")
    return persian_months

def input_time(prompt):
    """Input time in HH:MM format"""
    while True:
        time = input(prompt)
        parts = time.split(":")
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            hour, minute = map(int, parts)
            if 0 <= hour < 24 and 0 <= minute < 60:
                return time
        print("⛔ Invalid time format! Please enter time in HH:MM format.")

def save_shifts(date, shifts):
    """Save shifts into SQLite"""
    for shift in shifts:
        cursor.execute("INSERT OR REPLACE INTO work_schedule (date, shift_name, start_time, end_time) VALUES (?, ?, ?, ?)",
                       (date, shift[0], shift[1], shift[2]))
    conn.commit()
    print("\n✅ Work schedule saved!")

def main():
    while True:
        print("\n📌 Main Menu:")
        print("1: Add a new work shift")
        print("2: Exit")

        choice = input("Please enter your choice: ")

        if choice == "1":
            print("\n📅 Please select a month:")
            months = display_months()

            try:
                month_choice = int(input("Enter month number (1-12): "))
                if month_choice not in months:
                    print("⛔ Invalid month!")
                    continue
            except ValueError:
                print("⛔ Please enter a valid number.")
                continue

            day_choice = int(input("\nPlease enter a day (1-31): "))
            year = JalaliDate.today().year

            try:
                jalali_date = JalaliDate(year, month_choice, day_choice)
                gregorian_date = jalali_date.to_gregorian()
            except ValueError:
                print("⛔ Invalid date!")
                continue

            date_key = f"{jalali_date.day} {months[jalali_date.month]} {jalali_date.year}"
            print(f"\n📆 Selected date: {date_key}")

            # Select and define shifts
            shifts = []
            start = input_time("⏳ Shift Start time (HH:MM): ")
            end = input_time("⏳ Shift End time (HH:MM): ")
            shifts.append(("Work Shift", start, end))

            # Save shifts to database
            if shifts:
                save_shifts(date_key, shifts)
            else:
                print("\n❌ No shifts were recorded!")

        elif choice == "2":
            print("\n👋 Exiting the program. Take care!")
            conn.close()
            break

        else:
            print("⛔ Invalid choice! Please select the correct option.")

if __name__ == "__main__":
    main()





# import calendar
# import sqlite3

# # English month names
# english_months = {
#     1: "January", 2: "February", 3: "March", 4: "April",
#     5: "May", 6: "June", 7: "July", 8: "August",
#     9: "September", 10: "October", 11: "November", 12: "December"
# }

# # SQLite Database Setup
# conn = sqlite3.connect("work_schedule.db")
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS work_schedule (
#     date TEXT PRIMARY KEY,
#     shift_name TEXT,
#     start_time TEXT,
#     end_time TEXT
# )
# """)
# conn.commit()


# def get_month_weeks(year, month):
#     """Get the list of weeks in a given month with weekdays"""
#     weeks = calendar.monthcalendar(year, month)
#     return [[(calendar.day_name[calendar.weekday(year, month, day)], day) if day != 0 else ("", 0) for day in week] for week in weeks]


# def display_months():
#     """Display months for selection"""
#     for num, name in english_months.items():
#         print(f"{num}: {name}")
#     return english_months


# def display_weeks(weeks):
#     """Display weeks of a month with weekdays"""
#     for i, week in enumerate(weeks, 1):
#         formatted_week = [f"{day_name} {day}" if day else "" for day_name, day in week]
#         print(f"Week {i}: {formatted_week}")


# def input_time(prompt):
#     """Input time in HH:MM format"""
#     while True:
#         time = input(prompt)
#         parts = time.split(":")
#         if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
#             hour, minute = map(int, parts)
#             if 0 <= hour < 24 and 0 <= minute < 60:
#                 return time
#         print("⛔ Invalid time format! Please enter time in HH:MM format.")


# def select_shift():
#     """Select work shifts"""
#     shifts = []

#     while True:
#         print("\nSelect a shift:")
#         print("1: Shift 1")
#         print("2: Shift 2")
#         print("0: End and save")

#         shift_choice = input("Please enter your choice (1, 2, or 0 to exit): ")

#         if shift_choice == "1":
#             start = input_time("⏳ Shift 1 - Start time (HH:MM): ")
#             end = input_time("⏳ Shift 1 - End time (HH:MM): ")
#             shifts.append(("Shift 1", start, end))

#         elif shift_choice == "2":
#             start = input_time("⏳ Shift 2 - Start time (HH:MM): ")
#             end = input_time("⏳ Shift 2 - End time (HH:MM): ")
#             shifts.append(("Shift 2", start, end))

#         elif shift_choice == "0":
#             break

#         else:
#             print("⛔ Invalid choice! Please try again.")

#     return shifts


# def save_shifts(date, shifts):
#     """Save shifts into SQLite"""
#     for shift in shifts:
#         cursor.execute("INSERT OR REPLACE INTO work_schedule (date, shift_name, start_time, end_time) VALUES (?, ?, ?, ?)",
#                        (date, shift[0], shift[1], shift[2]))
#     conn.commit()
#     print("\n✅ Work schedule saved!")


# def print_schedule():
#     """Print all saved shifts from SQLite"""
#     cursor.execute("SELECT * FROM work_schedule ORDER BY date")
#     rows = cursor.fetchall()

#     if not rows:
#         return "📌 No shifts have been recorded yet."

#     schedule_str = "\n📅 Recorded Work Schedule:"
#     for row in rows:
#         date, shift_name, start_time, end_time = row
#         schedule_str += f"\n\n📆 Date: {date}\n🕒 {shift_name}: {start_time} - {end_time}"
#     print("\n")
#     schedule_str += "\n\n✅ End of work schedule"
#     return schedule_str


# def main():
#     year = 2024  # Change year if needed

#     while True:
#         print("\n📌 Main Menu:")
#         print("1: Add a new work shift")
#         print("2: Display all recorded shifts")
#         print("3: Exit")

#         choice = input("Please enter your choice: ")

#         if choice == "1":
#             print("\n📅 Please select a month:")
#             months = display_months()

#             try:
#                 month_choice = int(input("Enter month number (1-12): "))
#                 if month_choice not in months:
#                     print("⛔ Invalid month!")
#                     continue
#             except ValueError:
#                 print("⛔ Please enter a valid number.")
#                 continue

#             print(f"\n📆 Selected month: {months[month_choice]}")

#             # Get and display weeks
#             weeks = get_month_weeks(year, month_choice)
#             print("\n📅 Weeks of this month:")
#             display_weeks(weeks)

#             try:
#                 week_choice = int(input("\nEnter week number (1-5): "))
#                 if week_choice < 1 or week_choice > len(weeks):
#                     print("⛔ Invalid week!")
#                     continue
#             except ValueError:
#                 print("⛔ Please enter a valid number.")
#                 continue

#             selected_week = weeks[week_choice - 1]
#             valid_days = [(day_name, day) for day_name, day in selected_week if day != 0]

#             print("\n📆 Days of this week:")
#             for day_name, day in valid_days:
#                 print(f"{day_name}: {day}")

#             try:
#                 day_choice = int(input("\nPlease select a day: "))
#                 if day_choice not in [day for _, day in valid_days]:
#                     print("⛔ Invalid day!")
#                     continue
#             except ValueError:
#                 print("⛔ Please enter a valid number.")
#                 continue

#             selected_day_name = [day_name for day_name, day in valid_days if day == day_choice][0]
#             date_key = f"{selected_day_name}, {months[month_choice]} {day_choice}, {year}"
#             print(f"\n📆 Selected date: {date_key}")

#             # Select and define shifts
#             work_shifts = select_shift()

#             # Save shifts to database
#             if work_shifts:
#                 save_shifts(date_key, work_shifts)
#             else:
#                 print("\n❌ No shifts were recorded!")

#         elif choice == "2":
#             print(print_schedule())  # Display the work schedule

#         elif choice == "3":
#             print("\n👋 Exiting the program. Take care!")
#             conn.close()
#             break

#         else:
#             print("⛔ Invalid choice! Please select the correct option.")


# if __name__ == "__main__":
#     main()
