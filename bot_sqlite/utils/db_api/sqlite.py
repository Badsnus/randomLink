import sqlite3
from sqlite3.dbapi2 import connect


class Database:
    def __init__(self, path_to_db="../db.sqlite3"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE if not exists Users (
        user_id int NOT NULL,
        PRIMARY KEY (user_id)
        );
        """
        self.execute(sql, commit=True)

    def create_table_links(self):
        sql = """
        CREATE TABLE if not exists Links (
        link_name varchar(20) not NULL,
        user_id int NOT NULL,
        links text not null,
        count_visits int not null,
        PRIMARY KEY (link_name)
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, user_id: int):
        sql = "INSERT INTO Users(user_id) VALUES(?)"
        parameters = (user_id,)
        self.execute(sql, parameters=parameters, commit=True)

    def add_link(self, link_name: str, user_id: int, links: str, count_visits=0):
        sql = "INSERT INTO Links(link_name, user_id, links, count_visits) VALUES(?, ?, ?, ?)"
        parameters = (link_name, user_id, links, count_visits)
        self.execute(sql, parameters=parameters, commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def select_links(self, **kwargs):
        sql = "SELECT * FROM Links WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users", fetchone=True)

    def delete_link(self, link_name):
        sql = "DELETE FROM Links WHERE link_name = ?"
        return self.execute(sql, parameters=(link_name, ), commit=True)

