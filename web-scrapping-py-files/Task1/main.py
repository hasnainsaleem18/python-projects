import requests
from bs4 import BeautifulSoup

url = "http://brokenepicgames.onlinewebshop.net/"

# Accessing webpage
response = requests.get(url)

# Checking if website is accessible or not.
print(response.status_code)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the game card div using class code
game = soup.find('div', class_="css-2mlzob")

# Extracting the title and price
title = game.find('div', class_="css-rgqwpc")
price = game.find('span', class_="css-12s1vua")

game_title = title.text.strip()
game_price = price.text.strip()

# Creating the formatted output
html_structure = f"""<div class="css-2mlzob">
    <div class="box">
        <span class="title"> {game_title} </span>
        <span class="price"> {game_price} </span>
    </div>
</div>"""

print(html_structure)

print("\n\nWithout formatted output\n\n")
# Without formatted output
print(game)

