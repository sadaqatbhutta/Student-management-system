students = []

def show_menu():
    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save & Exit")
    

# Function to add a new student

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    class_name = input("Enter class: ")

    student = {
        "name": name,
        "roll": roll,
        "class": class_name
    }

    students.append(student)
    print("✅ Student added successfully!")
    
    
# Function to view all students

def view_students():
    if not students:
        print("⚠ No students found.")
    else:
        print("\n--- Student List ---")
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['name']}, Roll: {student['roll']}, Class: {student['class']}")

# Function to search a student by roll number

def search_student():
    roll_to_search = input("Enter roll number to search: ")
    found = False

    for student in students:
        if student['roll'] == roll_to_search:
            print("\n✅ Student Found:")
            print(f"Name: {student['name']}, Roll: {student['roll']}, Class: {student['class']}")
            found = True
            break

    if not found:
        print("❌ No student found with that roll number.")
        
        
        
# Function to delete a student by roll number

def delete_student():
    roll_to_delete = input("Enter roll number to delete: ")
    found = False

    for student in students:
        if student['roll'] == roll_to_delete:
            students.remove(student)
            print("🗑 Student deleted successfully!")
            found = True
            break

    if not found:
        print("❌ No student found with that roll number.")
        
        
        
# Function to save students to a JSON file

import json
def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
        print("students saved to 'students.json'.")
        
        

# Main function to run the program

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            save_students()
            print("📁 Exiting program and saving students...")
            break
        else:
            print("Invalid choice. Try again.")

main()