import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Accessing the webpage
url = "http://brokenepicgames.onlinewebshop.net/"

# Send a request to get the webpage content
response = requests.get(url)
html_body = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_body, "html.parser")

# Find all game containers on the website
games = soup.find_all('div', class_='css-2mlzob')
free_games = []

# Loop through each game to extract details
for game in games:
    # Extract the game title
    game_title = game.findChildren("div", class_="css-rgqwpc", recursive=True)
    game_title = game_title[0].text.strip()

    # Extract the game price and clean up the text
    game_price = game.find('span', {"class": 'eds_1ypbntd0 eds_1ypbntdc eds_1ypbntdk css-12s1vua'}).find_parent()
    game_price = game_price.text.strip().replace('$', '')

    # Extract the game URL
    game_url = (game.find('a', class_='css-g3jcms'))['href']

    # Extract the game image source
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

# Create the root element for the XML
root = ET.Element("Games")

# Add each game as a child to the root element
for game in free_games:
    game_element = ET.SubElement(root, "Game")

    # Create child elements for title, price, URL, and image
    title_element = ET.SubElement(game_element, "Title")
    title_element.text = game['title']

    price_element = ET.SubElement(game_element, "Price")
    price_element.text = game['price']

    url_element = ET.SubElement(game_element, "URL")
    url_element.text = game['url']

    image_element = ET.SubElement(game_element, "Image")
    image_element.text = game['image']

# Create an ElementTree object
tree = ET.ElementTree(root)

# Write the XML to a file
tree.write("games_data.xml", encoding="utf-8", xml_declaration=True)

print("XML file 'games_data.xml' has been generated successfully.")
