import requests

base_url = 'http://localhost:8000'

def test_get_root_check_status_code_equals_200():
     response = requests.get(f'{base_url}/')
     assert response.status_code == 200

def test_get_root_check_response_equals_hello_world():
     response = requests.get(f'{base_url}/')
     assert response.json() == {"Message": "Hello World"}

def test_post_weather_check_status_code_equals_201():
     response = requests.post(f'{base_url}/weather/', json={"user_id": "1"})
     assert response.status_code == 201

def test_post_weather_check_response_equals_weather_data_for_this_user_already_exists():
     response = requests.post(f'{base_url}/weather/', json={"user_id": "1"})
     assert response.json() == {'status': 'weather data for this user already exists'}

def test_post_weather_check_response_equals_request_to_collect_weather_data_was_successfully_registered():
     response = requests.post(f'{base_url}/weather/', json={"user_id": "2"})
     assert response.json() == {'status': 'request to collect weather data was successfully registered'}

def test_get_weather_check_status_code_equals_200():
     response = requests.get(f'{base_url}/weather/1')
     assert response.status_code == 200

def test_get_weather_check_status_code_equals_404():
     response = requests.get(f'{base_url}/weather/3')
     assert response.status_code == 404

def test_get_weather_check_response_equals_user_id():
     response = requests.get(f'{base_url}/weather/1')
     assert response.json()['User ID'] == '1'

def test_get_weather_check_response_progress_greater_than_zero():
     response = requests.get(f'{base_url}/weather/1')
     assert float(response.json()['Progress']) > 0