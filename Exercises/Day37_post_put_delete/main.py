import requests
import datetime

FINAL_GRAPHIC = "https://pixe.la/v1/users/simplestchau/graphs/graph1.html"
USERNAME = "simplestchau"
TOKEN = "iF9#f&Jzo6TJ#vg"
pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
today = datetime.datetime.now()
today = today.strftime('%Y%m%d')

#response = requests.post(url=pixela_endpoint, json=user_parameters)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    'id': 'graph1',
    'name': "Cycling gGraph",
    'unit': 'km',
    'type': 'float',
    'color': 'momiji'
}
headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoit = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel_parameters = {
    #"date": today,
    "quantity": "15"
}
#response = requests.post(url=pixel_endpoit, json=pixel_parameters, headers=headers)
#print(response.text)

updatepix_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"

#response = requests.put(url=updatepix_endpoint, json=pixel_parameters, headers=headers)


daletepix_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"
response = requests.delete(url=daletepix_endpoint, headers=headers)
print(response.text)