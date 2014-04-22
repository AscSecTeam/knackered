__all__ = ["Cursor", "Database"]

import sqlite3


class Cursor(object):
    __slots__ = ["connection", "cursor"]

    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def __iter__(self):
        for row in self.cursor:
            yield row

    def __enter__(self):
        return self.cursor

    def __exit__(self, type, value, traceback):
        self.cursor.close()
        if isinstance(value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()


class Database(object):
    __slots__ = ["source", "connection"]

    def __init__(self, source=":memory:"):
        self.source = source
        self.connection = sqlite3.connect(source)

    def cursor(self):
        return Cursor(self.connection)
