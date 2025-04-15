
# 4/14/2025
# CSC-121 m4Pro 
# James Moore

"""Program: Course and Tuition Information System
Description:
  This program shows course information, lets you look up a course,
  and displays tuition details for students and for each course.
"""

courses = {
    "MAT-035": {"desc": "Concepts of Algebra", "tuition": 460},
    "CTI-115": {"desc": "Computer System Foundations", "tuition": 520.98},
    "BAS-120": {"desc": "Intro to Analytics", "tuition": 500},
    "CSC-121": {"desc": "Python Programming", "tuition": 783.88}
}

students = {
    "Zakari Watson": ["CTI-115", "CSC-121"],
    "Jerom Williams": ["CTI-115", "CSC-121", "MAT-035", "BAS-120"],
    "Dominique Ross": ["CTI-115", "CSC-121", "MAT-035"],
    "Diana Shepard": ["MAT-035", "CTI-115", "BAS-120", "CSC-121"],
    "Yoko Mayo": ["MAT-035"],
    "Rashad Ahmed": ["MAT-035", "BAS-120"],
    "Susan Jones": ["BAS-120", "CSC-121"]
}


def displayCourseInfo(cs):
    """
    Display all courses with their code, description, and tuition.
    """
    print("Course Information:")
    print(f"{'Code':<10}{'Description':<35}{'Tuition':>10}")
    print("-" * 55)
    for code, info in cs.items():
        print(f"{code:<10}{info['desc']:<35}{info['tuition']:>10.2f}")
    print("-" * 55 + "\n")


def courseList(cs):
    """
    Perform a lookup of a course based on user input.
    """
    print("Course Lookup")
    course_code = input("Enter course code: ")
    if course_code in cs:
        info = cs[course_code]
        print(f"{info['desc']} - Tuition: ${info['tuition']:.2f}\n")
    else:
        print("Course code not found.\n")


def displayStudentTuitionInfo(studs, cs):
    """
    Display a numbered list of students, let the user select one,
    and then show the selected student's courses and total tuition.
    """
    student_names = list(studs.keys())
    print("Students:")
    for i in range(len(student_names)):
        print(f"{i+1}) {student_names[i]}")
    print("-" * 30)
    
    selection = input("Select a student by number: ")
    if selection.isdigit():
        index = int(selection) - 1
        if index < 0 or index >= len(student_names):
            print("Invalid selection!")
            return
    else:
        print("You did not enter a valid number.")
        return

    chosen_student = student_names[index]
    print(f"\nSelected Student: {chosen_student}")
    
    student_courses = studs[chosen_student]
    total = 0
    print(f"\n{chosen_student}'s Courses and Tuition:")
    print(f"{'Course':<10}{'Description':<35}{'Tuition':>10}")
    print("-" * 55)
    for course in student_courses:
        if course in cs:
            info = cs[course]
            tuition_fee = info["tuition"]
            print(f"{course:<10}{info['desc']:<35}${tuition_fee:>9.2f}")
            total = total + tuition_fee
    print("-" * 55)
    print(f"Overall Total                                ${total:,.2f}\n")


def displayTuitonAll():
    """
    Display the total tuition for each student.
    """
    overall_total = 0
    print("Tuition For Each Student:")
    print(f"{'Student Name':<25}{'# Courses':<12}{'Tuition':>10}")
    print("-" * 55)
    
    for student, course_list in students.items():
        count = len(course_list)
        student_total = 0
        for course in course_list:
            if course in courses:
                student_total = student_total + courses[course]["tuition"]
        overall_total = overall_total + student_total
        print(f"{student:<25}{str(count):<12}${student_total:>9.2f}")
    
    print("-" * 55)
    print(f"Overall Total:                    ${overall_total:>9.2f}\n")


def displayNumStudents():
    """
    Display the number of students and total tuition generated for each course.
    (This version does not include the course description.)
    """
    print("Students and Tuition by Course:")
    print(f"{'Course Code':<12}{'# of Stu':<10}{'Tuition Generated':>20}")
    print("-" * 45)
    
    for code, details in courses.items():
        student_count = 0
        for slist in students.values():
            if code in slist:
                student_count = student_count + 1
        course_total = student_count * details["tuition"]
        print(f"{code:<12}{str(student_count):<10}{'$':>5}{course_total:>14.2f}")
    print("-" * 45 + "\n")


def menu():
    """
    Display the menu and return the user's selection.
    """
    print("-------------- MENU --------------")
    print("1) Display Course Information")
    print("2) Lookup Course")
    print("3) Display Courses and Tuition for a Specific Student")
    print("4) Display Tuition for All Students")
    print("5) Display # of Students and Tuition for All Courses")
    print("6) Exit")
    print("----------------------------------")
    choice = input("Enter your selection: ")
    return choice


def main():
    """
    Main function that runs the menu loop until the user chooses to exit.
    """
    choice = menu()
    
    while choice != "6":
        if choice == "1":
            displayCourseInfo(courses)
        elif choice == "2":
            courseList(courses)
        elif choice == "3":
            displayStudentTuitionInfo(students, courses)
        elif choice == "4":
            displayTuitonAll()
        elif choice == "5":
            displayNumStudents()
        else:
            print("Invalid option! Please try again.\n")
        choice = menu()
    
    print("Program will now stop. Goodbye!")


main()