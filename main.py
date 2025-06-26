def show_menu():
    print("\n====== student management system ======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete student")
    print("5. Save & Exit")

students = []

# adding students

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter the roll number: ")
    class_name = input("Enter the class name: ")
    
    student = {
        "name": name,
        "roll": roll,
        "class": class_name
    }
    students.append(student)
    print(f"Student {name} added successfully.")
    
# funtion to view all students
    
def view_students():
    if not students:
        print("No students found. ")
    else:
        print("\n======= List of Students ======")
        
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['name']}, Roll: {student['roll']}, Class: {student['class']}")
            
# function to search for a student

def search_student():
    roll_to_search = input("Enter the roll number to search: ")
    found = False

    for student in students:
        if student['roll'] == roll_to_search:
            print("\nStudent Found: ")
            print(f"Name: {student['name']}, Roll: {student['roll']}, Class: {student['class']}")
            found = True
            break
    if not found:
        print("Student not found with that roll number.")
            
            
# function to delete a student

def delete_student():
    roll_to_delete = input("Enter the roll number to delete: ")
    found = False
    
    for student in students:
        if student['roll'] == roll_to_delete:
            students.remove(student)
            print("Student deleted successfully.")
            found = True
            break
    if not found:
        print("No student found with that roll number to delete,")
       
            
    
# main function to run the program
            
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
            break
        else:
            print("Invalid choice, please try again.")
    main()


            
    