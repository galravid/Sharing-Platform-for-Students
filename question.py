from datetime import datetime
from qs_and_as import Qs_And_As


class Question(Qs_And_As):
    def __init__(self, qas_id: int, title: str, upload_date: datetime, question_content):
        super().__init__(qas_id, title, upload_date)
        self.__question_content = question_content

    def __str__(self):
        return f"Question({super().__str__()}, question_content={self.__question_content})"
