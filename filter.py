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
driver.get(base_url+"/search")

# wait for the page to load
WebDriverWait(driver,10).until(EC.title_contains("MTG Deck Planner | Card Search"))
print()


###################################################################################
###################################################################################
print("Test 1: Finding a card just by the name...")
print("\tSearching for Mental Misstep - will return only one card...")

time.sleep(1)

#find the search name element
search = driver.find_element_by_id("in_page_search")
search.clear()
search.send_keys("Mental Misstep")


# click the submit form button
submit_button = driver.find_element_by_id("filter_button")
submit_button.click()

# wait for reload page
WebDriverWait(driver,10).until(EC.title_contains("MTG Deck Planner | Card Search"))

print("\tChecking search results...")

# get the returned card element
cards = driver.find_elements_by_class_name("card_show")

print("\tChecking search results...")

# assert to see if one card is returned
assert len(cards) == 1
print("\tOnly one card properly returned!")


# assert to see if the corrent card is returned
name = driver.find_element_by_css_selector("div.card_show > p:nth-child(1)")
assert name.text == 'Mental Misstep'
print("\tMental Misstep properly returned!")
print()


###################################################################################
###################################################################################
print("Test 2: Finding a card using CMC, Power, & Toughness...")
print("\tSearching for CMC = 13, Power = 13, & Toughness = 13")
print("\tWill return only one card: Emrakul, the Promised End...")

#clear the search name element
search = driver.find_element_by_id("in_page_search")
search.clear()

cmcValue = driver.find_element_by_name("cmcValue")
cmcValue.clear()
cmcValue.send_keys("13")

powerValue = driver.find_element_by_name("powerValue")
powerValue.clear()
powerValue.send_keys("13")

toughnessValue = driver.find_element_by_name("toughnessValue")
toughnessValue.clear()
toughnessValue.send_keys("13")
    
time.sleep(1)

# click the submit form button
submit_button = driver.find_element_by_id("filter_button")
submit_button.click()

# wait for reload page
WebDriverWait(driver,10).until(EC.title_contains("MTG Deck Planner | Card Search"))

print("\tChecking search results...")

# assert to see if one card is returned
assert len(cards) == 1
print("\tOnly one card properly returned!")


# assert to see if the corrent card is returned
name = driver.find_element_by_css_selector("div.card_show > p:nth-child(1)")
assert name.text == 'Emrakul, the Promised End'
print("\tEmrakul, the Promised End properly returned!")
print()


###################################################################################
###################################################################################
print("Test 3: Finding cards using Colors...")

###################################################################################
def checkColor(color, card):
	print("\tSearching for "+color+" cards...")
	print("\tFirst Card should be '"+card+"'...")

	#clear the search name element
	search = driver.find_element_by_id("in_page_search")
	search.clear()

	#check color box
	colo = driver.find_element_by_name("check_"+color)
	colo.click()

	# click the submit form button
	submit_button = driver.find_element_by_id("filter_button")
	submit_button.click()

	# wait for reload page
	WebDriverWait(driver,10).until(EC.title_contains("MTG Deck Planner | Card Search"))

	print("\tChecking search results...")

	# assert to see if the corrent card is returned
	name = driver.find_element_by_css_selector("div.card_show > p:nth-child(1)")
	assert name.text == card
	print("\t"+card+" properly returned!")
	print()


#white Ancestor's Chosen
checkColor("white", "Ancestor's Chosen")
#blue Academy Researchers
checkColor("blue", "Academy Researchers")
#black Afflict
checkColor("black", "Afflict")
#red Anaba Bodyguard
checkColor("red", "Anaba Bodyguard")
#green Abundance
checkColor("green", "Abundance")


###################################################################################
#END TEST
driver.quit()
pause = input("Enter Any Key to Complete Test...")