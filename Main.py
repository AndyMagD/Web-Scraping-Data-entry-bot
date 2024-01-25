from scrape_info import scrapes_for_info
from form_bot import fill_form

# Calling the scrapes_for_info() function and storing the returned values
addresses, prices, links = scrapes_for_info()

# Calling the fill_form() function with the obtained values
fill_form(addresses, prices, links)

