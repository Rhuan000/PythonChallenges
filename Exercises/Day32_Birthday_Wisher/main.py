import smtplib
import random
import datetime as dt

my_email = "simplestchau@gmail.com"
my_password = "bquohyyyzbdbyksb"

'''connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs='simplestchau@yahoo.com', msg='hello')
connection.close()

time_now = dt.datetime.now()
year = time_now.year
month = time_now.month
day_of_week = time_now.weekday()
print(day_of_week)

date_of_birthday = dt.datetime(year=1995, month=12, day=15)
print(date_of_birthday)'''

#Selecting a random text to send.
with open('quotes.txt') as data:
    random_text = random.choice(data.readlines())

#Creating a connection with email to send.
connection = smtplib.SMTP('smtp.gmail.com', 587)

#checking if the time is the rihgt time to send.
time_now = dt.datetime.now()
day_week = time_now.weekday()

if day_week == 2:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f'subject: MOTIVATION TO START YOUR WEDNESDAY\n\n{random_text}')
    connection.close()