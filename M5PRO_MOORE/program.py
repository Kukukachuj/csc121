"""
Program: Student Tuition Calculator
Description:
    This program manages student course selections, calculates tuition fees based
    on the courses taken, computes average grades, displays student information,
    and writes the data to a file. The user can choose to process data for all
    students or for a specific student.

Modules:
    - student_utils: Provides helper functions for loading student/course lists,
                     writing data to a file, and displaying student selections.
"""

import os
from student_utils import load_student_and_course_lists, write_to_file, display_students, display_student_info

# Load student names and courses from a CSV file (assumes correct format)
stu_names, courses = load_student_and_course_lists()
# Create a simple dictionary to store student data (initially empty)
students_data = {}
for name in stu_names:
    students_data[name] = {}  # Start with an empty dict for each student

# Set up tuition fees for each course (by order)
tuition_list = [460, 520.98, 500, 783.88]
tuition_rates = {}
for i in range(len(courses)):
    # For simplicity, assume the order of courses matches tuition_list order
    tuition_rates[courses[i]] = tuition_list[i]

def menu():
    """
    Displays the main menu options.

    Options:
        1) Select Courses, Enter Grades, and Calculate Tuition
        2) Calculate Tuition for a Specific Student
        3) Display Average and Total Tuition (All Students)
        4) Display Basic Student Info
        5) Exit
    """
    print("-" * 20, " MENU ", "-" * 20)
    print("1) Select Courses, Enter Grades, and Calculate Tuition")
    print("2) Calculate Tuition for a Specific Student")
    print("3) Display Average and Total Tuition (All Students)")
    print("4) Display Basic Student Info")
    print("5) Exit")

def select_courses():
    """
    For each student in the list, asks which courses they are taking,
    prompts for the grade, calculates total tuition and average grade,
    updates the global 'students_data' dictionary, and writes the data to a file.
    """
    for student in stu_names:
        print("\nSelecting courses for " + student)
        student_courses = {}  # To hold course grades for this student
        total_tuition = 0     # Sum of tuition fees for courses taken
        course_count = 0      # Count how many courses the student takes
        
        for course in courses:
            answer = input("Is " + student + " taking " + course + "? (y/n): ")
            if answer.lower() == "y":
                grade_input = input("Enter grade for " + course + ": ")
                try:
                    grade = float(grade_input)
                except:
                    grade = 0
                student_courses[course] = grade
                total_tuition += tuition_rates.get(course, 0)
                course_count += 1
        
        # Calculate average grade if any courses were taken; else 0.
        if course_count > 0:
            average = sum(student_courses.values()) / course_count
        else:
            average = 0
        
        # Save the student data to our dictionary
        students_data[student] = {"avg": round(average, 2), "tuition": round(total_tuition, 2)}
    
    print("\nAll student data:")
    print(students_data)
    write_to_file(students_data)

def calculate_tuition():
    """
    Calculates tuition for a specific student.

    Process:
       - Prompts the user to select a student from the list.
       - For the chosen student, it asks if they are taking each course.
       - For each course taken, it prompts for the grade and adds the course's tuition.
       - Computes the average grade if courses are taken.
       - Updates the global 'students_data', displays a tuition statement, and writes it to student.txt.
    """
    # Ask the user to choose a student from the list
    student = display_students(stu_names)
    print("\nNow enter the courses for " + student + ".")
    
    # Create an empty dictionary for this student's courses and set total cost to 0
    student_courses = {}
    total = 0  # Total tuition for courses taken
    
    # Loop over each course and ask if the student is taking it
    for course in courses:
        answer = input("Is " + student " taking " + course + "? (y/n): ")
        if answer.lower() == "y":
            grade_input = input("Enter grade for " + course + ": ")
            try:
                grade = float(grade_input)
            except:
                grade = 0
            student_courses[course] = grade
            # Add the tuition fee for that course from our tuition_rates dictionary
            total += tuition_rates.get(course, 0)
    
    # Calculate average grade if at least one course was taken, otherwise 0
    if len(student_courses) > 0:
        average = sum(student_courses.values()) / len(student_courses)
    else:
        average = 0
    
    # Update the global students_data with this student's info
    students_data[student] = {"avg": round(average, 2), "tuition": round(total, 2)}
    
    # Display tuition statement on the screen
    print("\nTuition statement for " + student)
    print("Course".ljust(40) + "Tuition")
    print("-" * 50)
    for course in student_courses:
        cost = tuition_rates.get(course, 0)
        print(course.ljust(40) + "$" + format(cost, ".2f"))
    print("-" * 50)
    print("Total cost".ljust(40) + "$" + format(total, ".2f"))
    
    # Write the tuition statement to a file named student.txt
    f = open("student.txt", "w", encoding="utf-8")
    f.write("Tuition statement for " + student + "\n")
    f.write("Course".ljust(40) + "Tuition\n")
    f.write("-" * 50 + "\n")
    for course in student_courses:
        cost = tuition_rates.get(course, 0)
        f.write(course.ljust(40) + "$" + format(cost, ".2f") + "\n")
    f.write("-" * 50 + "\n")
    f.write("Total cost".ljust(40) + "$" + format(total, ".2f") + "\n")
    f.close()
    
    print("\nTuition data written to student.txt")

def main():
    """
    The main loop that displays the menu and executes the user's selected option.

    Options:
      1) Select Courses, Enter Grades, and Calculate Tuition for all students.
      2) Calculate Tuition for a Specific Student.
      3) Display Average and Total Tuition from the stu_courses.txt file.
      4) Display Basic Student Info.
      5) Exit the program.
    """
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            select_courses()
        elif choice == "2":
            calculate_tuition()
        elif choice == "3":
            filename = "stu_courses.txt"
            if os.path.exists(filename):
                f = open(filename, "r", encoding="utf-8")
                print("\nContents of stu_courses.txt:\n")
                print(f.read())
                f.close()
            else:
                print("File stu_courses.txt not found. Run Option 1 first.")
        elif choice == "4":
            display_student_info()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()