# main
from datetime import datetime
from user import User
from alert import Alert
from courses import Courses
from question import Question
from answer import Answer
from student import Student
from system_admin import System_Admin

# Creating and printing objects

user = User(1, "John Doe", "password123", "john.doe@example.com")
print(user)

alert = Alert(1, "New assignment available", 1, datetime.now())
print(alert)

course = Courses(101, "Mathematics")
print(course)

question = Question(201, "Math Question", datetime.now(), "What is 2+2?")
print(question)

answer = Answer(301, "Math_Answer", datetime.now(), True, "The answer is 4")
print(answer)

student = Student(2, "Jane Doe", "securepass", "jane.doe@example.com", "XYZ University")
print(student)

admin = System_Admin(3, "Admin User", "adminpass", "admin@example.com")
print(admin)
