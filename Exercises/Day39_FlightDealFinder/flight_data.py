class FlightData:
    '''This class is responsible for structuring the flight data.'''
    def __init__(self):
        self.departure_city_name: str
        self.departure_iataCode: str
        self.arrival_city_name: str
        self.arrival_iataCode: str
        self.outbound_date: str
        self.inbound_date: str

    def capturing_details_of_fly(self, data_to_get):
        self.price = data_to_get['price']
        self.departure_city_name = data_to_get['cityFrom']
        self.departure_iataCode = data_to_get['flyFrom']
        self.arrival_city_name = data_to_get['cityTo']
        self.arrival_iataCode = data_to_get['flyTo']
        self.outbound_date = data_to_get['utc_arrival'].split('T')[0]
        self.inbound_date = data_to_get['utc_departure'].split('T')[0]
