import os
import json
from dotenv import load_dotenv

import psycopg2


load_dotenv()


DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

class DatabaseConnector:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASS,
                database=DB_NAME,
                port=DB_PORT
            )
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)

    def create_weather_request(self, user_id: str, num_cities: int):
        query = f"INSERT INTO cities_weather_request (user_id, num_cities) VALUES ('{user_id}', {num_cities})"
        self.cursor.execute(query)
        self.connection.commit()

    def read_weather_request(self, user_id: str):
        query = f"SELECT * FROM cities_weather_request WHERE user_id='{user_id}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def weather_request_exists(self, user_id: str):
        query = f"SELECT EXISTS(SELECT * FROM cities_weather_request WHERE user_id='{user_id}')"
        self.cursor.execute(query)
        return self.cursor.fetchall()[0][0]

    def update_weather_request(self, user_id: str, weather_data: dict, num_progress: int, status: str = 'in_progress'):
        query =  f"UPDATE cities_weather_request SET cities_weather_data='{json.dumps(weather_data)}', "
        query += f"num_progress={num_progress}, status='{status}' WHERE user_id='{user_id}'"
        self.cursor.execute(query)
        self.connection.commit()
