import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_no TEXT,
    attendance INTEGER DEFAULT 0,
    performance REAL DEFAULT 0.0
)
""")

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    cursor.execute("INSERT INTO students (name, roll_no) VALUES (?, ?)", (name, roll_no))
    conn.commit()
    print("✅ Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    print("\n--- Student List ---")
    for row in result:
        print(f"ID: {row[0]}, Name: {row[1]}, Roll No: {row[2]}, Attendance: {row[3]}%, Performance: {row[4]}%")
    print("---------------------")

def update_student():
    roll_no = input("Enter roll number to update: ")
    attendance = int(input("Enter updated attendance (%): "))
    performance = float(input("Enter updated performance (%): "))
    cursor.execute("UPDATE students SET attendance=?, performance=? WHERE roll_no=?",
                   (attendance, performance, roll_no))
    conn.commit()
    print("✅ Student record updated!")

def delete_student():
    roll_no = input("Enter roll number to delete: ")
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    conn.commit()
    print("🗑️ Student record deleted.")

def menu():
    while True:
        print("\n=== Student Information Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Record")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    menu()
    cursor.close()
    conn.close()