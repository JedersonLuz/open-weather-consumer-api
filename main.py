import os
import requests
from dotenv import load_dotenv

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

from utils.database_connector import DatabaseConnector

load_dotenv()

API_KEY = os.getenv("API_KEY")

with open('cities_id_list.txt', 'r') as f:
    CITIES_ID_LIST = f.read().splitlines()
    TOTAL_CITIES = len(CITIES_ID_LIST)

db = DatabaseConnector()

class User(BaseModel):
    user_id: str


app = FastAPI()


def get_weather_data(user_id: str):
    cities_weather_data = {}
    cities_weather_data['cities'] = []
    try:
        db.create_weather_request(user_id, TOTAL_CITIES)
        for num_cities, city_id in enumerate(CITIES_ID_LIST, 1):
            citie_weather_data = {}
            citie_weather_data['city_id'] = city_id
            
            url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            
            temprature = response.json()['main']['temp']
            humidity = response.json()['main']['humidity']
            
            citie_weather_data['temprature'] = temprature
            citie_weather_data['humidity'] = humidity
            cities_weather_data['cities'].append(citie_weather_data)

            db.update_weather_request(user_id, cities_weather_data, num_cities)
        print(f'Weather data for user {user_id} was successfully collected')
    except Exception as e:
        print(f'Weather data for user {user_id} was not completely collected')
        print(e)


@app.get("/")
async def root():
    return {"Message": "Hello World"}


@app.post("/weather/")
async def create_weather_request(background_tasks: BackgroundTasks, user: User):
    background_tasks.add_task(get_weather_data, user.user_id)
    return {'status': 'request to collect weather data was successfully registered'}


@app.get("/weather/{user_id}")
async def read_weather_request_progress(user_id: str):
    return {"User ID": user_id}