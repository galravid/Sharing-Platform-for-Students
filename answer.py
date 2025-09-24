from datetime import datetime
from qs_and_as import Qs_And_As


class Answer(Qs_And_As):
    def __init__(self, qas_id: int, title: str, upload_date: datetime, is_valid: bool, answer_content):
        super().__init__(qas_id, title, upload_date)
        self.__is_valid = is_valid
        self.__answer_content = answer_content

    def ai_inconsistency(self):
        pass  # Implement AI inconsistency logic

    def __str__(self):
        return f"Answer({super().__str__()}, is_valid={self.__is_valid}, answer_content={self.__answer_content})"
