import psycopg2
from config import host, user, password, db_name

class DatabaseSingleton():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_db()
        return cls._instance
    

    def init_db(self):
        try:
            self.connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
            )
            self.connection.autocommit = True
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Ticket(
                    id serial PRIMARY KEY,
                    contact_information VARCHAR,
                    complain_text VARCHAR NOT NULL);"""
                    )
        except Exception as _ex:
                print(f"ошибка при работе с бд: {_ex}")

    
    def insert_ticket(self,contact_information:str,complain_text:str):
        try:
            with self.connection.cursor() as cursor:
                query = """INSERT INTO Ticket (contact_information, complain_text)VALUES (%s, %s)"""
                cursor.execute(query, (contact_information, complain_text))
                print("данные сохранены")
        except Exception as _ex:
                print(f"ошибка при работе с бд: {_ex}")