import os

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name}: {self.grade}"

class StudentGradeManager:
    def __init__(self):
        self.students = {}
        self.load_data()

    def add_student(self, name, grade):
        self.students[name] = Student(name, grade)
        print(f"Added {name} with a grade of {grade}")
        self.save_data()

    def update_student(self, name, grade):
        if name in self.students:
            self.students[name].grade = grade
            print(f"Updated {name}'s grade to {grade}")
            self.save_data()
        else:
            print(f"{name} not found")

    def delete_student(self, name):
        if name in self.students:
            del self.students[name]
            print(f"Deleted {name}")
            self.save_data()
        else:
            print(f"{name} not found")

    def calculate_average(self):
        if self.students:
            total = sum(student.grade for student in self.students.values())
            average = total / len(self.students)
            print(f"Average Grade: {average:.2f}")
        else:
            print("No students to calculate average")

    def display_all_students(self):
        if self.students:
            for student in self.students.values():
                print(student)
        else:
            print("No students to display")

    def save_data(self):
        with open('student_grades.txt', 'w') as file:
            for student in self.students.values():
                file.write(f"{student.name},{student.grade}\n")

    def load_data(self):
        if os.path.exists('student_grades.txt'):
            with open('student_grades.txt', 'r') as file:
                for line in file:
                    name, grade = line.strip().split(',')
                    self.students[name] = Student(name, float(grade))

def main():
    manager = StudentGradeManager()

    while True:
        print('\nStudent Grade Management')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Calculate Average")
        print("5. View Students")
        print("6. Exit")

        choice = input("Enter Your Choice: ")
        if choice == '1':
            name = input("Enter Student Name: ")
            grade = float(input("Enter Student Grade: "))
            manager.add_student(name, grade)
        elif choice == '2':
            name = input("Enter Student Name: ")
            grade = float(input("Enter New Grade: "))
            manager.update_student(name, grade)
        elif choice == '3':
            name = input("Enter Student Name: ")
            manager.delete_student(name)
        elif choice == '4':
            manager.calculate_average()
        elif choice == '5':
            manager.display_all_students()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()


    while True:
        print('\nStudent Grade Management')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Calculate Average")
        print("5. View Students")
        print("6. Exit")

        choice = input("Enter Your Choice: ")
        if choice == '1':
            name = input("Enter Student Name: ")
            grade = float(input("Enter Student Grade: "))
            manager.add_student(name, grade)
        elif choice == '2':
            name = input("Enter Student Name: ")
            grade = float(input("Enter New Grade: "))
            manager.update_student(name, grade)
        elif choice == '3':
            name = input("Enter Student Name: ")
            manager.delete_student(name)
        elif choice == '4':
            manager.calculate_average()
        elif choice == '5':
            manager.display_all_students()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()

def generate_report_card(self):
    for student in self.students.values():
        with open(f"{student.name}_report_card.txt", 'w') as file:
            file.write(f"Report Card for {student.name}\n")
            file.write(f"Grade: {student.grade}\n")
            file.write(f"Pass/Fail: {'Pass' if student.grade >= 60 else 'Fail'}\n")
            print(f"Report card for {student.name} generated.")

     
            
        


