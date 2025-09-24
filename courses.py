class Courses:
    def __init__(self, course_id: int, course_name: str):
        self.__course_id = course_id
        self.__course_name = course_name

    def __str__(self):
        return f"Courses(id={self.__course_id}, name={self.__course_name})"

