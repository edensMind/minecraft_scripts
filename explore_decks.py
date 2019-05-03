from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
import time


# Create a new instance of the FireFox driver
driver = webdriver.Chrome("C:\\_cuts\\Selenium\\chromedriver.exe")

# go to the site
base_url = "http://192.168.1.33:8333"
driver.get(base_url+"/explore_decks")

# wait for the page to load
WebDriverWait(driver,10).until(EC.title_contains("MTG Deck Planner | Explore Decks"))
print()


###################################################################################
#Checks to ensure each deck listed in the Explore Decks page actually has at least 60 cards
print("Test: Ensure each deck listed in the Explore Decks page actually has at least 60 cards...")


print("\tGettign all listed decks...")
#get deck link URLs
deck_elements = driver.find_elements_by_class_name("deck_link")
#get deck names
deck_name_elements = driver.find_elements_by_class_name("deck_name")

#store deck URLS and names
decks = []
for i in range(0,len(deck_elements)):
	decks.append([deck_elements[i].get_attribute('href'), deck_name_elements[i].text])


print("\tDecks found: "+str(len(decks)))

# foreach deck, check number of cards shown
for deck in decks:
	# deck[0] = deck url
	# deck[1] = deck name
	print("\tChecking deck: "+deck[1]+"...")

	# go to deck page
	driver.get(deck[0])
	# wait for the page to load
	WebDriverWait(driver,10).until(EC.title_contains("MTG Deck Planner | View Deck"))
	
	cards = driver.find_elements_by_class_name("deck_card")#deck_card

	ok = False
	if len(cards) > 59:
		ok = True

	assert ok
	print("\tOk number of cards! - "+str(len(cards)))
	print()





###################################################################################
#END TEST
driver.quit()
pause = input("Enter Any Key to Complete Test...")