import requests
from bs4 import BeautifulSoup

# Accessing website
url = "http://brokenepicgames.onlinewebshop.net/"

# Send a request to get the website content
response = requests.get(url)
html_body = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_body, "html.parser")

# Find all games on the website
games = soup.find_all('div', class_='css-2mlzob')
free_games = []

# Loop through each game to extract details
for game in games:
    free_game_title = game.find('div', {"class": "css-rgqwpc"})
    free_game_price = game.find('span', {"class": 'eds_1ypbntd0 eds_1ypbntdc eds_1ypbntdk css-12s1vua'})
    free_game_url = (game.find('a', class_ ='css-g3jcms'))['href']
    free_game_image = game.select_one('img.css-1ae5wog')['src']

    # If all required information is present and the game is free, add it to the list
    if free_game_price and free_game_title and free_game_url and free_game_image:
        if free_game_price.text.strip().lower() == "free":
            free_games.append(
                {
                    'title': free_game_title.text.strip(),
                    'price': free_game_price.text.strip(),
                    'url': free_game_url,
                    'image': free_game_image
                }
            )

    # Stop the loop once two free games have been found
    if len(free_games) == 2:
        break

# Display the collected free games information
print("***Free Games***:")
for index, game in enumerate(free_games, start=1):
    print(f"{index}. Title: {game['title']}")
    print(f"- Price: ${game['price']}")
    print(f"- URL: {game['url']}")
    print(f"- Image: {game['image']}")
    print("\n")
