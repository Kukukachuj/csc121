# 4/14/2025
# CSC-121 M6Lab 
# James Moore

"""
Program: Course and Tuition Information System (M6Lab)
Description:
  This program shows course information, lets you look up a course,
  and displays tuition details for students and for each course.
  In this version, the output is written to files.
"""

import csv

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


def writeCourseInfo(cs):
    """
    Option 1:
      1. Write course information into a text file .
         File name: "course_info.txt"
      2. Write course information into a CSV file.
         File name: "courseInfo_CSV.csv"
    """
    # Write text file
    with open("course_info.txt", "w") as fout:
        header = f"{'Code':<10}{'Description':<35}{'Tuition':>10}\n"
        fout.write(header)
        fout.write("-" * 55 + "\n")
        for code, info in cs.items():
            line = f"{code:<10}{info['desc']:<35}{info['tuition']:>10.2f}\n"
            fout.write(line)
        fout.write("-" * 55 + "\n")
    # Write CSV file
    overall_total = sum(info["tuition"] for info in cs.values())
    with open("courseInfo_CSV.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Code", "Description", "Tuition"])
        for code, info in cs.items():
            writer.writerow([code, info["desc"], f"${info['tuition']:.2f}"])
        writer.writerow(["", "", f"${overall_total:.2f}"])
    print("Course information written to 'course_info.txt' and 'courseInfo_CSV.csv'.\n")


def lookupCourse(cs):
    """
    Option 2: Search by course
      1. The user enters a course code 
      2. If found, write course information into a text file.
         The file name is based on the course code.
    """
    user_input = input("Enter course code to search: ")
    code = user_input.upper()
    if code in cs:
        info = cs[code]
        file_name = code.replace("-", "_") + ".txt"
        with open(file_name, "w") as fout:
            header = f"{'Code':<10}{'Description':<35}{'Tuition':>10}\n"
            fout.write(header)
            fout.write("-" * 55 + "\n")
            line = f"{code:<10}{info['desc']:<35}{info['tuition']:>10.2f}\n"
            fout.write(line)
            fout.write("-" * 55 + "\n")
        print(f"Course information written to '{file_name}'.\n")
    else:
        print("Course code not found.\n")


def writeStudentTuitionInfo(studs, cs):
    """
    Option 3: Courses and Tuition for a Specific Student
       1. Ask the user to enter a student name
       2. Search for a match  If multiple are found, let the user choose.
       3. Write the student's courses and tuition to a CSV file.
    """
    search_str = input("Enter student name: ").lower()
    matching = [name for name in studs if search_str in name.lower()]
    
    if not matching:
        print("No students found.\n")
        return

    if len(matching) == 1:
        chosen_student = matching[0]
    else:
        print("Matching student names:")
        for i, name in enumerate(matching):
            print(f"{i+1}) {name}")
        choice = input("Select a student by number: ")
        if choice.isdigit():
            index = int(choice) - 1
            if index < 0 or index >= len(matching):
                print("Invalid selection.\n")
                return
            chosen_student = matching[index]
        else:
            print("Invalid input.\n")
            return

    student_courses = studs[chosen_student]
    overall_total = 0
    file_name = chosen_student.replace(" ", "_") + "_tuition.csv"
    with open(file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Course Code", "Description", "Tuition"])
        for course in student_courses:
            if course in cs:
                info = cs[course]
                tuition = info["tuition"]
                writer.writerow([course, info["desc"], f"${tuition:.2f}"])
                overall_total += tuition
        writer.writerow(["", "", f"${overall_total:.2f}"])
    print(f"Tuition information for {chosen_student} written to '{file_name}'.\n")


def writeTuitionAll(studs, cs):
    """
    Option 4: Display tuition for all students.
      Write the information into two files:
        1. Text file named "stu_tuition.txt"
        2. CSV file named "stu_csv_tuition.csv".
    """
    overall_total = 0
    student_data = []
    for student, clist in studs.items():
        total = 0
        for course in clist:
            if course in cs:
                total += cs[course]["tuition"]
        overall_total += total
        student_data.append((student, len(clist), total))
    
    # Write text file
    with open("stu_tuition.txt", "w") as fout:
        header = f"{'Student Name':<25}{'# Courses':<12}{'Tuition':>10}\n"
        fout.write(header)
        fout.write("-" * 55 + "\n")
        for name, count, total in student_data:
            fout.write(f"{name:<25}{str(count):<12}{total:>10.2f}\n")
        fout.write("-" * 55 + "\n")
        fout.write(f"{'Overall Total:':<37}{overall_total:>10.2f}\n")
    
    # Write CSV file
    with open("stu_csv_tuition.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Student Name", "# Courses", "Tuition"])
        for name, count, total in student_data:
            writer.writerow([name, count, f"${total:.2f}"])
        writer.writerow(["", "", f"${overall_total:.2f}"])
    
    print("Written to 'stu_tuition.txt' and 'stu_csv_tuition.csv'.\n")


def writeNumStudents(cs, studs):
    """
    Option 5: Display Number of Students Registered by Course.
       Write the information into two files:
         1. Text file named "course_cnt_tuition.txt"
         2. CSV file named "course_cnt_tui_csv.csv"
    """
    data = []
    for code, details in cs.items():
        count = sum(1 for clist in studs.values() if code in clist)
        total = count * details["tuition"]
        data.append((code, count, total))
    
    # Write text file
    with open("course_cnt_tuition.txt", "w") as fout:
        header = f"{'Course Code':<12}{'# of Stu':<10}{'Tuition Generated':>20}\n"
        fout.write(header)
        fout.write("-" * 45 + "\n")
        for code, count, total in data:
            fout.write(f"{code:<12}{str(count):<10}{total:>20.2f}\n")
        fout.write("-" * 45 + "\n")
    
    # Write CSV file
    with open("course_cnt_tui_csv.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Course Code", "# of Stu", "Tuition Generated"])
        for code, count, total in data:
            writer.writerow([code, count, f"${total:.2f}"])
    
    print("Written to 'course_cnt_tuition.txt' and 'course_cnt_tui_csv.csv'.\n")


def menu():
    """
    Display the menu and return the user's selection.
    """
    print("-------------- MENU --------------")
    print("1) Display Course Information")
    print("2) Search by Course")
    print("3) Display Courses and Tuition for a Specific Student")
    print("4) Display Tuition for All Students")
    print("5) Display # of Students and Tuition for All Courses")
    print("6) Exit")
    print("----------------------------------")
    return input("Enter your selection: ")


def main():
    """
    Main function: runs the menu loop until the user chooses to exit.
    """
    choice = menu()
    while choice != "6":
        if choice == "1":
            writeCourseInfo(courses)
        elif choice == "2":
            lookupCourse(courses)
        elif choice == "3":
            writeStudentTuitionInfo(students, courses)
        elif choice == "4":
            writeTuitionAll(students, courses)
        elif choice == "5":
            writeNumStudents(courses, students)
        else:
            print("Invalid option! Please try again.\n")
        choice = menu()
    
    print("Program will now stop. Goodbye!")


main()