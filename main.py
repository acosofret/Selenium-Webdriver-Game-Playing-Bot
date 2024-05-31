from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

time_for_upgrade = time.time() + 5
time_to_finish = time.time() + 300

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

game_link = "https://orteil.dashnet.org/experiments/cookie/"

driver.get(game_link)
money = driver.find_element(By.CSS_SELECTOR, value="#money")

# Upgrades Costs:
time_machine_cost = float(((driver.find_element(By.ID, value="buyTime machine")).text.split(" - "))[1].split("\n")[0].replace(",",""))
alchemy_lab_cost = float(((driver.find_element(By.ID, value="buyAlchemy lab")).text.split(" - "))[1].split("\n")[0].replace(",",""))
shipment_cost = float(driver.find_element(By.CSS_SELECTOR, value="#buyShipment b").text.split(" - ")[1].replace(",",""))
mine_cost = float(driver.find_element(By.CSS_SELECTOR, value="#buyMine b").text.split(" - ")[1].replace(",",""))
factory_cost = float(driver.find_element(By.CSS_SELECTOR, value="#buyFactory b").text.split(" - ")[1].replace(",",""))
grandma_cost = float(driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b").text.split(" - ")[1].replace(",",""))
cursor_cost = float(driver.find_element(By.CSS_SELECTOR, value="#buyCursor b").text.split(" - ")[1].replace(",",""))

# Cookie (button) to click:
cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

while time.time() < time_to_finish:
	game_on = True
	cookie.click()

if time.time() > time_to_finish:
	#print cookies per sec
	driver.quit()





