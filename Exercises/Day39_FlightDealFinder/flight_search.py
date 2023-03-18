import requests
import os

flight_apikey = os.environ.get("FLIGHTAPIKEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.sfly_endpoint = "https://api.tequila.kiwi.com/v2/search?&dateFrom=01/12/2022&dateTo=01/05/2023"
        self.sfly_header = {
            'apikey': flight_apikey
        }
        self.sfly_params = {
            'fly_from': 'GIG',
            'fly_to': 'shorcut.'
        }

    def search_for_travel(self, iata_code):
        self.sfly_params['fly_to'] = iata_code
        self.sfly_response = requests.get(url=self.sfly_endpoint, params=self.sfly_params, headers=self.sfly_header)
        self.sfly_data = self.sfly_response.json()