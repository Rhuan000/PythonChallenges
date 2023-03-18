import requests
import datetime
import math
import smtplib
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
count = 0
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": "IYBETTRSLMSV007S"
}
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": "7a15b35ec4cb42cf97e648d835c4a1e2"
}
its_negative: bool
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
for key in stock_data['Time Series (Daily)']:
    count += 1
    if count > 3:
        break
    elif count == 1:
        today = key
    elif count == 2:
        yesterday = key
    elif count == 3:
        before_yesterday = key


yesterday_close = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])
before_yesterday_close = float(stock_data['Time Series (Daily)'][before_yesterday]['4. close'])

percentual = ((before_yesterday_close - yesterday_close)*100)/before_yesterday_close
show = str(percentual).split('.')
show = show[0] + '.' + show[1][0:2] + '%Y'



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if percentual < 0:
    its_negative = True
    percentual *= -1

if percentual < 5:
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_data = news_response.json()
    for number in range(0, 2):
        news_title = html.escape(news_data['articles'][number]['title']).encode()
        news_discription = html.escape(news_data['articles'][number]['description']).encode()
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user="simplestchau@gmail.com", password="bquohyyyzbdbyksb")
        connection.sendmail(from_addr="simplestchau@gmail.com", to_addrs="simplestchau@gmail.com", msg=f"subject: TSLA {show}\n {news_title} \n {news_discription}")
        connection.close()
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

#Optional: Format the SMS message like this: 
"""                                                                                             
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

