import requests
from bs4 import BeautifulSoup

# Accessing the website
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
    # Extract the game title, price, url, image
    game_title = game.findChildren("div", class_="css-rgqwpc", recursive=True)
    game_title = game_title[0].text.strip()

    game_price = game.find('span', {"class": 'eds_1ypbntd0 eds_1ypbntdc eds_1ypbntdk css-12s1vua'}).find_parent()
    game_price = game_price.text.strip().replace('$', '')

    game_url = (game.find('a', class_='css-g3jcms'))['href']

    game_image = game.select_one('img.css-1ae5wog')['src']

    # Convert the price to a float to check the price range
    try:
        price_value = float(game_price)
    except ValueError:
        price_value = None  # Set to None if conversion fails

    # Check if the game price is between $5 and $30
    if 5 <= price_value <= 30:
        # Add the game details to the list if it meets the price criteria
        free_games.append(
            {
                'title': game_title,
                'price': game_price,
                'url': game_url,
                'image': game_image
            }
        )

    # Stop the loop once three games have been added
    if len(free_games) == 3:
        break

# Display the collected free games information
print("***Free Games***:")
for index, game in enumerate(free_games, start=1):
    print(f"{index}. Title: {game['title']}")
    print(f"- Price: ${game['price']}")
    print(f"- URL: {game['url']}")
    print(f"- Image: {game['image']}")
    print("\n")
