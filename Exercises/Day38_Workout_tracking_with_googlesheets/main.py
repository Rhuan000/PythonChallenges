import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("HOME")
API_KEY = os.environ.get("API_ID")
print(API_KEY, APP_ID)
'''exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
user_answer = input('Tell me which exercises you did: ')
params= {"query": user_answer}
sheet_endpoint = os.environ.get("sheet_endpoint")
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}
now_date = datetime.datetime.now().strftime('%d/%m/%Y')
now_time = datetime.datetime.now().strftime("%H:%M:%S")

post_params = {
    "workout": {
        "date": "",
        "time": "",
        "exercise": "",
        "duration": "",
        "calories": "",
        "name": ""
    }
}
header_sheet = {
    "Authorization": "Bearer ASDKASKDPAOSK123ASPL"
}

response1 = requests.post(url=exercise_endpoint, json=params, headers=header)
print(response1.text)
data = response1.json()

for exercise in data['exercises']:
    post_params['workout']['time'] = now_time
    post_params['workout']['date'] = now_date
    post_params['workout']['exercise'] = exercise['name']
    post_params['workout']['calories'] = exercise['nf_calories']
    post_params['workout']['duration'] = exercise['duration_min']
    response_sheets = requests.post(url=sheet_endpoint, json=post_params, headers=header_sheet)
    print(response_sheets.text)
'''