import pandas
import smtplib
import random
import datetime as dt

now = dt.datetime.now()
month = now.month
day = now.day
my_email = "@gmail.com"
my_password = ""

# 1. Update the birthdays.csv
data = pandas.read_csv('birthdays.csv')

for column, row in data.iterrows():
    # 2. Check if today matches a birthday in the birthdays.csv
    if row.month == month and row.day == day:
        random_letter = str((random.randint(1, 3)))

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f'letter_templates/letter_{random_letter}.txt', 'r') as letter:
            letter = letter.read()
            letter = letter.replace('[NAME]', str(row['name']))
            letter = letter.replace('Angela', 'Rhuan')

        # 4. Send the letter generated in step 3 to that person's email address.
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=str(row.email), msg=f'subject: Congragulations\n\n{letter}')
        connection.close()




