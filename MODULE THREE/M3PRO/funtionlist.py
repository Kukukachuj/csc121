def course_display(courses, tuition):
    """
    Display the list of courses and their corresponding tuition fees.

    Args:
        courses (list): List of course names.
        tuition (list): List of tuition fees corresponding to the courses.
    """
    print(f"{'Course name':<40} {'Tuition':<10}")
    print("-" * 50)
    for i in range(len(courses)):
        if i < len(tuition):
            print(f"{courses[i]:<40} ${tuition[i]:<10}")
    print("-" * 50)


def display_students(stu_names):
    """
    Display the list of students and prompt the user to select one.

    Args:
        stu_names (list): List of student names.

    Returns:
        int: Index of the selected student.
    """
    print("List of students:")
    for i, student in enumerate(stu_names):
        print(f"{i + 1}. {student}")
    student_choice = int(input("Select a student by entering their number: ")) - 1
    return student_choice


def tuition_statement(student, student_courses, totalTuition):
    """
    Print a tuition statement for a specific student.

    Args:
        student (str): Name of the student.
        student_courses (list): List of tuples containing course names and their fees.
        totalTuition (float): Total tuition fee for the student.
    """
    print(f"\nTuition statement for {student}\n")
    print(f" {'Course':<40} {'Tuition':<10}")
    print("-" * 50)
    for course, fee in student_courses:
        print(f"{course:<40} ${fee:.2f}")
    print("-" * 50)
    print(f"Total cost {' ' * 30}${totalTuition:.2f}\n\n")