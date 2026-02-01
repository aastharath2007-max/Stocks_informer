import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_forstocks='SY27Q41RARCYFY8D' #stock
API_KEY_fornews= "cbd2239b2d7f4f1ea4d2d2230b77e8e7"    #news
stock_params={'function':'TIME_SERIES_DAILY', 'apikey':API_KEY_forstocks,'symbol':STOCK}
news_params={'apiKey':API_KEY_fornews,'q':'stocks','qInTitle':COMPANY_NAME}



## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.


stock_behaviour = requests.get(url=STOCK_ENDPOINT,params=stock_params)
stock = stock_behaviour.json()

st_yesterday = float(stock['Time Series (Daily)']['2026-01-30']['4. close'])
st_day_before_yesterday= float(stock['Time Series (Daily)']['2026-01-29']['4. close'])
print(stock)

growth=st_yesterday-st_day_before_yesterday
print(abs(growth))
up_down=None


percentage_growth=growth/st_yesterday*100
if percentage_growth>0:
    up_down='⬆️'
else:
    up_down='⬇️'

#HINT 2: Work out the value of 5% of yesterday's closing stock price.
cl_st_price=5/100*st_yesterday
print(cl_st_price)

if cl_st_price>5:
    print('Get news')
## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator

response=requests.get(url=NEWS_ENDPOINT,params=news_params)
news=response.json()
print(news)
three_articles=news['articles'][:2]
print(three_articles)

#[new item for item in list]
formatted_articles=[f'{STOCK}: {up_down}{percentage_growth}% \nHeadline:{article['title']} \nBrief:{article['description']}'for article in three_articles]
print(formatted_articles)
## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.




client=Client(account_sid,auth_token)
for article in formatted_articles:
    message=client.messages.create(body=f'{article}',from_='+18126377684',to='+919434792435')
    print(message.status)
#Optional: Format the SMS message like this:
"""
TSLA: ⬆️2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: ⬇️5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

