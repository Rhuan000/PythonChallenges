import requests, time, smtplib, datetime

def checking_iss_ll():
    if latitude <= MY_LAT + 5  and latitude >= MY_LAT -5 and longitude <= MY_LNG + 5  and longitude >= MY_LNG -5:
        return True


MY_LAT = -22.385660
MY_LNG = -41.777790
my_email = "simplestchau@gmail.com"
my_password = "bquohyyyzbdbyksb"

while True:
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = iss_response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])


    now = datetime.datetime.now()
    time_now = now.time()

    #request with parameters:
    parameters = {
        "lat": -22.385660,
        "lng": -41.777790,
        "formatted": 0
    }

    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sunset = sun_response.json()['results']['sunset'].split('T')
    sunrise = sun_response.json()['results']['sunrise'].split('T')

    #catching the hour and minute separately
    sunset_hour = int(sunset[1].split(':')[0]) -3
    sunrise_hour = int(sunrise[1].split(':')[0]) -3
    hour_now = int(str(time_now).split(':')[0])


    if hour_now >= sunset_hour and hour_now <= sunrise_hour:
        if checking_iss_ll():
            connection = smtplib.SMTP('smtp.gmail.com', 587)
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="subject: LOOK UP\n\n The program was a success")
            connection.close()
            print('email send')

    time.sleep(1)