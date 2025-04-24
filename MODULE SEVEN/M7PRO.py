class Course:
    def __init__(self, code, description, tuition):
        self._code = code
        self._description = description
        self._tuition = tuition

    def get_tuition(self): 
        return self._tuition

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

    def get_enrolled_courses(self,course_list):
        for course_code in self._stu_courses:
            if course_code in course_list:
                course = course_list[course_code]
                print(f"{course.get_code()} | {course.get_description()} | ${course.get_tuition()}")
            else:
                print(f"Course {course_code} not found!")


# Creating a Student instance
student1 = Student("James")

# Printing the student's name using the getter method
print(student1.get_name())  # Expected output: "James"

# Checking initial courses (should be empty)
print(student1.get_stu_courses())  # Expected output: []

# Adding a course using the setter method
student1.set_stu_courses("CTI-110")

# Checking if the course was added
print(student1.get_stu_courses())  # Expected output: ["CTI-110"]
