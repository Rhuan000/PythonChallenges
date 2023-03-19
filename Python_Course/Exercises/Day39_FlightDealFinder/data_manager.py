import requests
import os

header = {
    'Authorization': os.environ.get("SHEETYTOKEN")
}

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_endpoint_get = "https://api.sheety.co/b13441ca49dfaa90ffa6828a0ed8d03d/cópiaDeFlightDeals/prices"
        self.sheet_endpoint_put = "https://api.sheety.co/b13441ca49dfaa90ffa6828a0ed8d03d/cópiaDeFlightDeals/prices"
        self.sheet_response = requests.get(url=self.sheet_endpoint_get, headers=header)
        self.sheet_data = self.sheet_response.json()
        self.new_dic ={key['iataCode']: key['lowestPrice'] for key in self.sheet_data['prices']}



    def update_sheet(self, iataCode, lowest_price):

            try:
                for city in self.sheet_data['prices']:
                    if city['iataCode'] == iataCode:
                        self.params = {
                            'price': {'lowestPrice': lowest_price}
                        }
                        city['lowestPrice'] = lowest_price
            except KeyError:
                for city in self.sheet_data['price']:
                    if city['iataCode'] == iataCode:
                        self.params = {
                            'price': {'lowestPrice': lowest_price}
                        }
                        city['lowestPrice'] = lowest_price

        ### remember ##
    # I needed to fix an error. When I tried to update the prices it was giving me an error. Because I didn't  pass the id to modify.
    def sendUpdate_sheet(self):

            self.sheet_data['price'] = self.sheet_data.pop('prices')


            for item in self.sheet_data['price']:
                self.params = {'price': {'lowestPrice': item['lowestPrice']}}
                self.sheet_response = requests.put(url=f"{self.sheet_endpoint_put}/{item['id']}", json=self.params, headers=header)
