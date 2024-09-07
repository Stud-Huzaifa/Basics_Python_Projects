#Initializing dictionary
student_grades = { }

#Adding Element
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a {grade}")

#Update a Student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade

        print(f"{name} with marks are upaded {grade}")

    else:
        print(f"{name} is not Found!")

#Delete Student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been sucessfully deleted")
    else:
        print(f"{name} is not Found!") 

def display_all_student():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print(f"No Students found/added")


def main():
    while True:
        print('\nStudent Grade Management')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))
        
        if choice == 1:
            name = input("Enter Student Name: ")
            grade = int(input("Enter Student Grade: "))
            add_student(name, grade)
        
        elif choice == 2:
            name = input("Enter Student Name: ")
            grade = int(input("Enter New Grade: "))
            update_student(name, grade)
        
        elif choice == 3:
            name = input("Enter Student Name: ")
            delete_student(name)
        
        elif choice == 4:
            display_all_students()
        
        elif choice == 5:
            print("Closing the Program")
            break
        
        else:
            print("Invalid Choice")




     


