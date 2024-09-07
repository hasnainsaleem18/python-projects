import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = "OOSXCEZCTCY02LI0"
news_api_key = "b78bceffcbc046b99506ec8ecab99e27"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

diff_percentage = (difference / float(day_before_yesterday_closing_price)) * 100
print(diff_percentage)

news_params = {
    "apiKey": news_api_key,
    "qInTitle": COMPANY_NAME,  
}

if diff_percentage > 4:
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"]

three_articles = articles[:3]
print(three_articles)

formatted_articles = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]


