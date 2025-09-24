from user import User
from courses import Courses
from question import Question
from answer import Answer


class Student(User):
    def __init__(self, user_id: int, name: str, password: str, email: str, academic_institution: str):
        super().__init__(user_id, name, password, email)
        self.__academic_institution = academic_institution
        self.__courses = []  # Aggregation: List of Courses objects
        self.__my_questions = []  # Aggregation: List of Question objects
        self.__my_answers = []  # Aggregation: List of Answer objects

    # Public Methods
    def enter_courses_manually(self, course):
        self.__courses.append(course)

    def upload_question(self, question):
        self.__my_questions.append(question)

    def upload_answer(self, answer):
        self.__my_answers.append(answer)

    def __str__(self):
        return f"Student({super().__str__()}, institution={self.__academic_institution}"
