class User:
    def __init__(self, user_id: int, name: str, password: str, email: str):
        self._user_id = user_id
        self._name = name
        self._password = password
        self._email = email
        self._alerts = []  # Composition: List of Alert objects
        self._answers = []
        self._question = []

    # Public Methods
    def get_alerts(self):
        return self._alerts

    def sign_up(self):
        pass  # Implement sign-up logic

    def sign_in(self):
        pass  # Implement sign-in logic

    def search_question(self, question):
        pass  # Implement question search logic

    def search_answer(self, answer):
        pass  # Implement answer search logic

    def __str__(self):
        return f"User(id={self._user_id}, name={self._name}, email={self._email}, password={self._password})"
