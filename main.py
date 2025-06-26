def show_menu():
    print("n====== student management system ======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("2. Delete student")
    print("5. Save & Exit")

students = []
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")
            
main()

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
    