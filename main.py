import os
import requests
from dotenv import load_dotenv

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel


load_dotenv()

API_KEY = os.getenv("API_KEY")


class User(BaseModel):
    user_id: str


app = FastAPI()


def get_weather_data(user_id: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?id=3439525&appid={API_KEY}&units=metric"
    response = requests.get(url)
    print(response.json())
    return response.json()


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