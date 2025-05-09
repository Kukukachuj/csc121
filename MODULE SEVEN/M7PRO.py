import csv

class Course:
    """
    Course class that stores a course's code, description, and tuition cost.
    """

    def __init__(self, code, description, tuition):
        self._code = code
        self._description = description
        self._tuition = tuition

    def get_code(self):
        """Return the course code."""
        return self._code

    def get_description(self):
        """Return the course description."""
        return self._description

    def get_tuition(self):
        """Return the tuition cost."""
        return self._tuition
                
    def __repr__(self):
        return f"Course Code: {self._code} | Description: {self._description} | Tuition: ${self._tuition}"
    
class Student:
    """
    Student class that stores the student's name and their courses.
    Can add courses, drop courses, and list what they're taking.
    """

    def __init__(self, name, stu_courses=None):
        self._name = name
        self._stu_courses = stu_courses if stu_courses is not None else []

    def drop_course(self, course_code):
        """Drop a course from the student's list, if they have it."""
        if course_code in self._stu_courses:
            self._stu_courses.remove(course_code)
            print(f"Dropped {course_code} :)")
        else:
            print(f"{course_code} not found in your courses")

    def get_name(self):
        """Return the student's name."""
        return self._name

    def get_stu_courses(self):
        """Return a list of the student's course codes."""
        return self._stu_courses

    def set_stu_courses(self, course_code):
        """Add a course code to the student's courses (if it's valid)."""
        if isinstance(course_code, str) and course_code.strip():
            self._stu_courses.append(course_code)
        else:
            print("Invalid course code, try again.")

    def get_enrolled_courses(self, courses):
        """
        Return a list of course details the student is enrolled in.
        Needs the full 'courses' dictionary to look stuff up.
        """
        enrolled_courses = []
        for course_code in self._stu_courses:
            if course_code in courses:
                course = courses[course_code]
                enrolled_courses.append(f"{course.get_code()} | {course.get_description()} | ${course.get_tuition()}")
            else:
                enrolled_courses.append(f"Course {course_code} not found.")
        return enrolled_courses

def write_students_to_csv(students, filename):
    with open(filename, "w", newline="") as file:  # Use "w" to write data
        writer = csv.writer(file)
        writer.writerow(["Name", "Courses"])
        for student in students:
            writer.writerow([student.get_name(), ", ".join(student.get_stu_courses())])

def read_students_from_csv(filename):
    students =[]
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name, courses = row
            courses_list = courses.split(", ")
            students.append(Student(name, courses_list))
    return students

def create_instances(stu_dict, course_dict):
    courses = {}
    for course_code , course_data in course_dict.items():
        description = course_data["description"]
        tuition = course_data["tuition"]
        courses[course_code] = Course(course_code, description, tuition)
    students = {}
    for name, course_codes in stu_dict.items():
        students[name] = Student(name, course_codes)
    return students, courses

def write_courses(courses, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Course Code", "Description", "Tuition"])
        for course in courses.values():
            writer.writerow([course.get_code(), course.get_description(), course.get_tuition()])


def write_stu(students, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Courses"])  # Header row
        for student in students:
            writer.writerow([student.get_name(), ", ".join(student.get_stu_courses())])


def lookup_student(student_name, students):
    student_name = student_name.title()
    if student_name in students:
        filename = f"{student_name.split()[-1]}.csv"
        write_stu({student_name: students[student_name]}, filename)
        print(f"Student details saved to {filename}.")
    else:
        print(f"Student {student_name} not found!")

def lookup_course(course_code, courses):
    """
    Lookup a course by its code and save the info to a text file.
    Files are named like 'abc123.txt'.
    """
    course_code = course_code.upper()
    if course_code in courses:
        file_name = course_code.lower().replace("-", "_") + ".txt"
        with open(file_name, "w") as file:
            file.write(f"Course Code: {courses[course_code].get_code()}\n")
            file.write(f"Description: {courses[course_code].get_description()}\n")
            file.write(f"Tuition: ${courses[course_code].get_tuition()}\n")
        print(f"Saved course info to {file_name}!")
    else:
        print("uhh course not found, check spelling?")

def drop_course_for_student(student_name, course_code, students):
    student_name = student_name.title()
    if student_name in students:
        filename_backup = f"{student_name.split()[-1]}_bck_up.csv"
        write_stu(students, filename_backup)
        
        students[student_name].drop_course(course_code)
        
        filename_updated = f"{student_name.split()[-1]}_updated.csv"
        write_stu(students, filename_updated)
        print(f"Course dropped. Backup saved to {filename_backup}, updated file saved to {filename_updated}.")
    else:
        print(f"Student {student_name} not found!")


ef main():
    """
    Main function to run a simple menu for managing student courses.
    """
    courses = {
        "CSE101": Course("CSE101", "Intro to Computer Science", 500),
        "MTH202": Course("MTH202", "Calculus II", 450),
        "ENG150": Course("ENG150", "English Literature", 400)
    }
    student = Student("Alex")

    choice = ""
    while choice != "6":
        print("-------------- MENU --------------")
        print("1) Display Course Information")
        print("2) Lookup Course")
        print("3) Display Courses and Tuition for a Specific Student")
        print("4) Display Tuition for All Students")
        print("5) Display # of Students and Tuition for All Courses")
        print("6) Exit")
        print("----------------------------------")
        choice = input("Enter your selection: ")

        if choice == "1":
            print("\nAvailable Courses:")
            for code, course in courses.items():
                print(f"{code} | {course.get_description()} | ${course.get_tuition()}")

        elif choice == "2":
            code = input("Enter course code to add: ").upper()
            if code in courses:
                student.set_stu_courses(code)
            else:
                print("Course not found.")

        elif choice == "3":
            code = input("Enter course code to drop: ").upper()
            student.drop_course(code)

        elif choice == "4":
            print("\nYour Courses:")
            enrolled = student.get_enrolled_courses(courses)
            for course_info in enrolled:
                print(course_info)

        elif choice == "5":
            code = input("Enter course code to lookup: ").upper()
            lookup_course(code, courses)

        elif choice != "6":
            print("Not a valid option, try again.")

    print("Goodbye :)")

if __name__ == "__main__":
    main()

            

            