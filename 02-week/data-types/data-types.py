age = 16
name = "John Jane"
isStudent = True 
hobbies = ["Learning", "soccer", "Swimming"]

class Student:
    def __init__(self, school_name, grade):
        self.schoolName = school_name
        self.grade = grade


student_object = Student(school_name="BCH", grade=66)

print(age)
print(name)
print(isStudent)
print(hobbies)
print(student_object.schoolName, student_object.grade)

print(type(age))
print(type(name))
print(type(isStudent))
print(type(hobbies))
print(type(Student))
