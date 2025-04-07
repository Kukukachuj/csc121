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

def menu():
    """
    Main menu options.
    """
    print("-" * 20, " MENU ", "-" * 20)
    print("1)  Select Courses, Course Grade and Calc Tuition")
    print("2)  Calculate Tuition for Specific Student")
    print("3)  Display Average and Total Tuition (All students)")
    print("4)  Display Student Info")
    print("5) Exit")
    print("-" * 20, " MENU ", "-" * 20)