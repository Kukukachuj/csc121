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

    def set_descrtiption(self, newValue):
        if newValue > 0:
            self._description = newValue
        else:
            print("inalid description")

    def set_code(self, newValue):
        if newValue > 0:
            self._code = newValue
        else:
            print("invalid")
                
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
    
    def set_name(self, newValue):
        if isinstance(newValue, str) and newValue.strip():  # Ensures it's a valid string
            self._name = newValue
        else:
            print("Invalid name! Must be a non-empty string.")

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




# Creating Course instances
course1 = Course("CTI-110", "Intro to Programming", 500)
course2 = Course("MAT-171", "Precalculus Algebra", 450)

# Creating a dictionary of available courses
course_list = {
    "CTI-110": course1,
    "MAT-171": course2
}

# Creating a Student instance
student1 = Student("James", ["CTI-110", "MAT-171", "ENG-101"])  # ENG-101 doesn't exist

# Testing get_enrolled_courses()
print(student1.get_enrolled_courses(course_list))  