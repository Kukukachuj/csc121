import csv

class Course:
    def __init__(self, code, description, tuition):
        self._code = code
        self._description = description
        self._tuition = tuition

    def get_tuition(self): 
        return self._tuition
    
    def get_description(self):
        return self._description
    
    def get_code(self):
        return self._code

    def set_tuition(self, newValue):
        if newValue > 0:
            self._tuition = newValue
        else:
            print("Invalid tuition amount! Must be positive.")

   
                
    def __repr__(self):
        return f"Course Code: {self._code} | Description: {self._description} | Tuition: ${self._tuition}"
    
class Student:
    def __init__(self, name, stu_courses=None):
        self._name = name
        self._stu_courses = stu_courses if stu_courses is not None else []


    def get_name(self):
        return self._name
    
    def get_stu_courses(self):
        return self._stu_courses
    

    def set_stu_courses(self, new_course_code):
        if isinstance(new_course_code, str) and new_course_code.strip():
            self._stu_courses.append(new_course_code)  # Append course instead of replacing list
        else:
            print("Invalid course code! Must be a non-empty string.")

    def get_enrolled_courses(self, course_list):
        enrolled_courses = []
        for course_code in self._stu_courses:
            if course_code in course_list:
                course = course_list[course_code]
                enrolled_courses.append(f"{course.get_code()} | {course.get_description()} | ${course.get_tuition()}")
            else:
                enrolled_courses.append(f"Course {course_code} not found!")
        return enrolled_courses

def write_students_to_csv(students, filename):
    with open(filename, "w", newline="") as file:  # Use "w" to write data
        writer = csv.writer(file)
        writer.writerow(["Name", "Courses"])
        for student in students:
            writer.writerow([student.get_name(), ", ".join(student.get_stu_courses())])




            

            