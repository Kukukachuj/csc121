import os




        


def display_avg_total_tuition():
    filename = "stu_courses.txt"

    if os.path.exists(filename):  # Check if the file exists
        print("\nReading contents of 'stu_courses.txt'...\n")
        with open(filename, "r") as file:
            print(file.read())  # Display file content
    else:
        print("\nNo 'stu_courses.txt' file found. Please run Option 1 first to generate tuition data.")
    
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
        print(f"{i+1}. {student}")
    
    student_choice = int(input("Select a student by entering their number: ")) -1
    return student_choice

