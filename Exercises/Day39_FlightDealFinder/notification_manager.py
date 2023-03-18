from flight_data import FlightData
import smtplib
import os

my_email = os.environ.get("MYEMAIL")
my_password = os.environ.get("MYPASSWORD")
email_to_send = os.environ.get("EMAILTOSEND")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
       self.message: str

    def making_message(self, fligh_data: FlightData):
        self.massage = f"Low price alert ${fligh_data.price} to fly from {fligh_data.departure_city_name}-{fligh_data.departure_iataCode} to {fligh_data.arrival_city_name}-{fligh_data.arrival_iataCode}, from {fligh_data.inbound_date} to {fligh_data.outbound_date}"

    def send_message(self, data):
        self.making_message(data)
        self.connection = smtplib.SMTP('smtp.gmail.com', 587)
        self.connection.starttls()
        self.connection.login(user=my_email, password=my_password)
        #try:
        self.connection.sendmail(from_addr=my_email, to_addrs=email_to_send, msg=f"subject: We found a discount\n\n{self.massage}")
        #except TypeError:
            #self.connection.sendmail(from_addr=my_email, to_addrs=email_to_send, msg=f"subject: We didnt find a discount.\n\n sorry but we didn't find.")
        self.connection.close()