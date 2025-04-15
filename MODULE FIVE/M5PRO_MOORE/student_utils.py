"""
Module: student_utils
Description:
    This module provides utility functions for managing student and course data.
    It includes functions to load student and course lists from a CSV file, write
    student data to a file in a tabular format, display a list of students for user
    selection, and display the content of a tuition statement file.
"""

import csv
import os

# Tuition rates for each course in a simple dictionary.
tuition_rates = {
    "MAT 035(Concepts of Algebra)": 460,
    "CTI 115(Computer System Foundations)": 520.98,
    "BAS 120 Intro to Analytics": 500,
    "CSC 121 Python Programming": 783.88
}

def load_student_and_course_lists(filename="stu_courses.csv"):
    """
    Loads student names and course names from a CSV file.
    
    The CSV file should have the first row containing course names.
    Each subsequent row may contain one or more student names.
    
    Args:
        filename (str): The name of the CSV file to read from (default is "stu_courses.csv").
    
    Returns:
        tuple: A tuple containing two lists:
            - student_names: A list of unique student names.
            - courses: A list of course names.
    """
    student_names = []  # List to store student names.
    courses = []        # List to store course names.
    
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        courses = next(reader)  # First row is courses
        
        # Each remaining row could contain one or more student names.
        for row in reader:
            for name in row:
                name = name.strip()
                if name != "" and name not in student_names:
                    student_names.append(name)
    
    return student_names, courses

def write_to_file(students_data):
    """
    Writes student data to a file in a tabular format.
    
    The output file is named "stu_courses.txt". The file will contain a header
    and each student's name, average grade, and tuition fees.
    
    Args:
        students_data (dict): A dictionary with student names as keys and another
                              dictionary with "avg" and "tuition" as values.
    """
    filename = "stu_courses.txt"
    
    # If no student data is available, notify the user and exit the function.
    if len(students_data) == 0:
        print("\nNo student data available. Please select courses first.")
        return
    
    f = open(filename, "w", encoding="utf-8")
    # Write the header for the table.
    f.write("Student Name         Average Grade   Tuition\n")
    f.write("=" * 55 + "\n")
    
    # Write each student's information.
    for student_name, details in students_data.items():
        avg = details.get("avg", 0)
        tuition = details.get("tuition", 0)
        # Left justify the student name and average; tuition is shown with a dollar sign.
        f.write(student_name.ljust(25) + str(format(avg, ".2f")).ljust(15) + "$" + str(format(tuition, ".2f")) + "\n")
    
    f.close()
    print("\nStudent data has been successfully written to 'stu_courses.txt'.")

def display_students(stu_names):
    """
    Displays a list of students and allows the user to choose one by entering a number.
    
    Args:
        stu_names (list): A list of student names.
    
    Returns:
        str: The chosen student's name.
    """
    print("\nList of students:")
    for i in range(len(stu_names)):
        print(str(i + 1) + ". " + stu_names[i])
    
    # Continue prompting for input until a valid number is entered.
    while True:
        try:
            choice = int(input("Select a student by entering their number: ")) - 1
            if choice >= 0 and choice < len(stu_names):
                return stu_names[choice]
            else:
                print("Invalid selection. Please choose a number from the list.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def display_student_info():
    """
    Displays the content of 'student.txt', which contains a tuition statement.
    
    If 'student.txt' exists, its contents are read and printed to the console.
    Otherwise, a message is displayed to inform the user that the file is missing.
    """
    filename = "student.txt"
    if os.path.exists(filename):
        print("\nReading contents of 'student.txt'...\n")
        f = open(filename, "r", encoding="utf-8")
        content = f.read()
        print(content)
        f.close()
    else:
        print("\nNo 'student.txt' file found. Please run your tuition calculation option first.")
