from datetime import datetime


class Alert:
    def __init__(self, alert_id: int, message: str, recipient_id: int, timestamp: datetime):
        self.__alert_id = alert_id
        self.__message = message
        self.__recipient_id = recipient_id
        self.__timestamp = timestamp

    def __str__(self):
        return f"Alert(id={self.__alert_id}, message={self.__message}, recipient_id={self.__recipient_id}, timestamp={self.__timestamp})"
