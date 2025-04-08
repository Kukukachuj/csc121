import os
from functions import  display_avg_total_tuition, display_students


students_data = {}

# Student Data
stuNames = ["Zakari Watson", "Jerom Williams", "Dominique Ross", "Diana Shepard", "Yoko Mayo", "Rashad Ahmed", "Susan Jones"]
courses = ["MAT 035 (Concepts of Algebra)", "CTI 115 (Computer System Foundations)", "BAS 120 Intro to Analytics", "CSC 121 Python Programming"]
tuition = [460, 520.98, 500, 783.88]
def display_student_info():
    for i in range(len(stuNames)):
        print(f"\nStudent: {stuNames[i]}")
        print(f"Course: {courses[i % len(courses)]}")  # Assigns courses dynamically
        print(f"Tuition: ${tuition[i % len(tuition)]:.2f}")
        
def select_courses():
   
    for student_name in stuNames:
        student_courses = {}
        total_tuition = 0

        print(f"\nSelecting courses for {student_name}:")
        for i in range(len(courses)):
            response = input(f"Is {student_name} taking {courses[i]}? Enter 'y' for yes: ")
            if response.lower() == 'y':
                grade = float(input(f"What grade did {student_name} get in {courses[i]}? "))
                student_courses[courses[i]] = grade
                total_tuition += tuition[i]  # Ensures correct tuition assignment

        if student_courses:
            avg_grade = sum(student_courses.values()) / len(student_courses)
        else:
            avg_grade = 0

        students_data[student_name] = {
            **student_courses,
            "avg": round(avg_grade, 2),
            "tuition": round(total_tuition, 2)
        }

    # Print dictionary for testing purposes
    print("\nCurrent Student Data Dictionary:")
    print(students_data)
    write_to_file(students_data)


def write_to_file(students_data):
    with open("stu_courses.txt", "w") as file:
        # Write headers
        file.write(f"{'Student Name':<25}{'Average Grade':<15}{'Tuition':>10}\n")
        file.write("=" * 55 + "\n")  # Separator line

        # Write student data
        for student_name, details in students_data.items():
            avg_grade = details["avg"]
            tuition = details["tuition"]
            file.write(f"{student_name:<25}{avg_grade:<15.2f}${tuition:>9.2f}\n")

    print("\nStudent data has been successfully written to 'stu_courses.txt'.")
def calculate_tuition():
    student_index = display_students(stuNames)  # Prompt user to select a student

    if 0 <= student_index < len(stuNames):  # Ensure valid selection
        student_name = stuNames[student_index]
        student_courses = {}  # Store selected courses
        total_tuition = 0

        print(f"\nChecking courses for {student_name}:")

        for i in range(len(courses)):
            response = input(f"Is {student_name} taking {courses[i]}? Enter 'y' for yes: ")
            if response.lower() == 'y':
                student_courses[courses[i]] = tuition[i]  # Link course to its tuition
                total_tuition += tuition[i]  # Accumulate tuition cost

        # Writing tuition data to student.txt
        with open("student.txt", "w") as file:
            file.write(f"\nTuition statement for {student_name}\n")
            file.write(f"{'Course':<40}{'Tuition':>10}\n")
            file.write("-" * 50 + "\n")

            for course, cost in student_courses.items():
                file.write(f"{course:<40}${cost:>9.2f}\n")

            file.write("-" * 50 + "\n")
            file.write(f"{'Total cost':<40}${total_tuition:>9.2f}\n")

        print("\nTuition data successfully written to 'student.txt'.")
    else:
        print("Invalid selection. Please enter a valid number.")


# Menu Display
def menu():
    """Main menu options."""
    print("-" * 20, " MENU ", "-" * 20)
    print("1) Select Courses, Course Grade, and Calc Tuition")
    print("2) Calculate Tuition for Specific Student")
    print("3) Display Average and Total Tuition (All students)")
    print("4) Display Student Info")
    print("5) Exit")
    print("-" * 20, " MENU ", "-" * 20)

# Placeholder Functions


# Main Loop
def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            select_courses()
        elif choice == "2":
                calculate_tuition()  # Call function to display tuition
          

        elif choice == "3":
            display_avg_total_tuition()
        elif choice == "4":
            display_student_info()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
