import requests
from bs4 import BeautifulSoup

url = "https://appbrewery.github.io/Zillow-Clone/"


def scrapes_for_info():
    addresses = []
    prices = []
    links = []

    try:
        response = requests.get(url)
        response.raise_for_status()

        contents = response.text
        soup = BeautifulSoup(contents,"lxml")

        #printed the prettified html to txt file for examination
        # with open("html_output.txt", "w", encoding="utf-8") as file:
        #     file.write(soup.prettify())

        property_cards = soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
        price_elements = soup.select(".PropertyCardWrapper span")

        #turned the for loops into list comprehensions
        links = [i["href"] for i in property_cards[:5]]
        addresses = [i.find("address", {"data-test": "property-card-addr"}).get_text(strip=True) for i in property_cards[:5]]
        prices = [price.get_text().replace("/mo", "").split("+")[0] for price in price_elements[:5] if "$" in price.text]

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve content. Error: {e}")

    return addresses, prices, links

    # For testing purposes i used the following code

    # formatted_links = "\n".join(links)
    # formatted_addresses = "\n".join(addresses)
    # formatted_prices = "\n".join(prices)
    # print(formatted_links)
    # print(formatted_addresses)
    # print(formatted_prices)


