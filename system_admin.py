from user import User


class System_Admin(User):
    def __init__(self, user_id: int, name: str, password: str, email: str):
        super().__init__(user_id, name, password, email)
        self.__validated_answers = []  # Aggregation: List of Answer objects

    # Public Methods
    def validate_answer(self, answer):
        self.__validated_answers.append(answer)

    def delete_answer(self, answer):
        if answer in self.__validated_answers:
            self.__validated_answers.remove(answer)

    def __str__(self):
        return f"System_Admin({super().__str__()}, validated_answers_count={len(self.__validated_answers)})"
