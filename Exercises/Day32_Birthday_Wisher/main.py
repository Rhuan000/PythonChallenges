import smtplib
import random
import datetime as dt

my_email = "@gmail.com"
my_password = "********"


#Selecting a random text to send.
with open('quotes.txt') as data:
    random_text = random.choice(data.readlines())

#Creating a connection with email to send.
connection = smtplib.SMTP('smtp.gmail.com', 587)

#checking if the time is the rihgt day and time to send.
time_now = dt.datetime.now()
day_week = time_now.weekday()

if day_week == 2:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f'subject: MOTIVATION TO START YOUR WEDNESDAY\n\n{random_text}')
    connection.close()