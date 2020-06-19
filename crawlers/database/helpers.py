# helpers.py

import sqlite3
from typing import Union

from .. import settings
from ..logger import get_logger

log = get_logger(__name__)


class Session:
    def __init__(self):
        self.session = None
    def __enter__(self):
        self.session = sqlite3.connect(settings.DB_NAME)
        self.cursor = self.session.cursor()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def execute(
    query: str,
    fetchall: bool = False,
    data: tuple = None
) -> Union[bool, list]:
    """
        Execute and commit SQL query
    """
    with Session() as conn:
        try:
            if data:
                conn.cursor.execute(query, data)
            else:
                conn.cursor.execute(query)
            conn.session.commit()
            if fetchall:
                return conn.cursor.fetchall()
            return True
        except sqlite3.Error as e:
            log.error(e, exc_info=True)
            conn.cursor.execute("rollback")
            return False
