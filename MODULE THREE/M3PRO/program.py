# Program that calculates students tuition fees
# 3/6/2025
# CSC-121 m3Pro - Purchases
# James Moore



from funtionlist import course_display, display_students, tuition_statement

stu_names = ["Zakari Watson", "Jerom Williams", "Dominique Ross", "Diana Shepard", "Yoko Mayo", "Rashad Ahmed", "Susan Jones"]
courses = ["MAT 035 (Concepts of Algebra)", "CTI 115 (Computer System Foundations)", "BAS 120 Intro to Analytics", "CSC 121 Python Programming"]
tuition = [460, 520.98, 500.00, 783.88]


def menu():
    """
    Main menu options.
    """
    print("-" * 20, " MENU ", "-" * 20)
    print("1)  Calculate Tuition for ALL Students")
    print("2)  Calculate Tuition for Specific Students")
    print("3)  Exit")
    print("-" * 20, " MENU ", "-" * 20)


def tuitionCalcAll(stu_names, courses, tuition):
    """
    Calculate and display the tuition for all students.

    Arguments:
        stu_names (list): List of student names.
        courses (list): List of course names.
        tuition (list): List of tuition fees corresponding to the courses.
    """
    totalTuition = 0
    studentTuitions = []
    for student in stu_names:
        studentTuition = 0
        student_courses = []
        for i in range(len(courses)):
            response = input(f"Is {student} taking {courses[i]}? Enter 'y' for yes: ")
            if response.lower() == 'y':
                studentTuition += tuition[i]
                student_courses.append((courses[i], tuition[i]))
        studentTuitions.append((student, studentTuition))
        totalTuition += studentTuition
    summery(studentTuitions)


def summery(studentTuitions):
    """
    Print a summary table of students and their total tuition.

    Arguments:
        studentTuitions (list): List of tuples containing student names and their total tuition.
    """
    print(f"\n{'Stu Name':<20} {'Tuition':<10}")
    for student, tuition in studentTuitions:
        print(f"{student:<20} ${tuition:.2f}")
    print("\n")


def specificStudentCalc(studentSpot, stu_names, courses, tuition):
    """
    Calculate and display the tuition for a specific student.

    Arguments:
        studentSpot (int): Index of the selected student.
        stu_names (list): List of student names.
        courses (list): List of course names.
        tuition (list): List of tuition fees corresponding to the courses.
    """
    student = stu_names[studentSpot]
    studentTuition = 0
    student_courses = []
    print(f"\nChecking courses for {student}:")
    for i in range(len(courses)):
        response = input(f"Is {student} taking {courses[i]}? Enter 'y' for yes: ")
        if response.lower() == 'y':
            studentTuition += tuition[i]
            student_courses.append((courses[i], tuition[i]))
    tuition_statement(student, student_courses, studentTuition)


def main():
    """
    Main function to run the program.
    """
    menuOption = ""
    while menuOption != "3":
        course_display(courses, tuition)
        menu()
        menuOption = input("Enter selection: ")
        if menuOption == "1":
            tuitionCalcAll(stu_names, courses, tuition)
        elif menuOption == "2":
            studentSpot = display_students(stu_names)
            if 0 <= studentSpot < len(stu_names):
                specificStudentCalc(studentSpot, stu_names, courses, tuition)


if __name__ == '__main__':
    main()