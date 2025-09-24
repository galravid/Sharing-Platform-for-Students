from datetime import datetime


class Qs_And_As:
    def __init__(self, qas_id: int, title: str, upload_date: datetime):
        self._qas_id = qas_id
        self._title = title
        self._upload_date = upload_date

    def __str__(self):
        return f"Qs_And_As(id={self._qas_id}, title={self._title}, upload_date={self._upload_date})"

