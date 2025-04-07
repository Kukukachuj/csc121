import csv
from  Functionlist import course_display, menu





def main():
    stuNames = ["Zakari Watson", "Jerom Williams", "Dominique Ross", "Diana Shepard", "Yoko Mayo", "Rashad Ahmed", "Susan Jones"]
    courses = ["MAT 035 (Concepts of Algebra)", "CTI 115 (Computer System Foundations)", "BAS 120 Intro to Analytics", "CSC 121 Python Programming"]
    tuition = [460, 520.98, 500,783.88]
    course_display(courses, tuition)
    menu(int option)
    students = {}
    """
    with open('courses.csv', 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        courses = next(csv_reader)  # First row contains course names

    # Iterate through each row in the CSV
        for row in csv_reader:
            for course, student_name in zip(courses, row):
             if student_name:  # Only process non-empty student names
                if student_name not in students:
                    students[student_name] = []  # Initialize the student's course list
                students[student_name].append(course)  # Add the course to the student's list
    
            menu()
            selection = input("Enterr your selection here: ")
            while selection != '5':
    
                if selection == '1':
                    for student_name in students:
                        print(student_name)

    

"""
if __name__ == "__main__":
    main()