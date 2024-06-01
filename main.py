from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

game_link = "https://orteil.dashnet.org/experiments/cookie/"

driver.get(game_link)

# Upgrades Costs & Buttons:
time_machine_cost = float(((driver.find_element(By.ID, value="buyTime machine")).text.split(" - "))[1].split("\n")[0].replace(",",""))
time_machine_button = driver.find_element(By.ID, value="buyTime machine")

portal_cost = float(((driver.find_element(By.CSS_SELECTOR, value="#buyPortal b")).text.split(" - "))[1].split("\n")[0].replace(",",""))
portal_button = driver.find_element(By.ID, value="buyPortal")

alchemy_lab_cost = float(((driver.find_element(By.ID, value="buyAlchemy lab")).text.split(" - "))[1].split("\n")[0].replace(",",""))
alchemy_lab_button = driver.find_element(By.ID, value="buyAlchemy lab")

shipment_cost = float(driver.find_element(By.CSS_SELECTOR, value="#buyShipment b").text.split(" - ")[1].replace(",",""))
shipment_button = driver.find_element(By.ID, value="buyShipment")

mine_cost = float(driver.find_element(By.CSS_SELECTOR, value="#buyMine b").text.split(" - ")[1].replace(",",""))
mine_button = driver.find_element(By.ID, value="buyMine")

factory_cost = float(driver.find_element(By.CSS_SELECTOR, value="#buyFactory b").text.split(" - ")[1].replace(",",""))
factory_button = driver.find_element(By.ID, value="buyFactory")

grandma_cost = float(driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b").text.split(" - ")[1].replace(",",""))
grandma_button = driver.find_element(By.ID, value="buyGrandma")

cursor_cost = float(driver.find_element(By.CSS_SELECTOR, value="#buyCursor b").text.split(" - ")[1].replace(",",""))
cursor_button = driver.find_element(By.ID, value="buyCursor")

# Cookie (button) to click:
cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

# Upgrade function:
def upgrade_if_possible():
	if money >= time_machine_cost:
		time_machine_button.click()
	elif money >= portal_cost:
		portal_button.click()
	elif money >= alchemy_lab_cost:
		alchemy_lab_button.click()
	elif money >= shipment_cost:
		shipment_button.click()
	elif money >= mine_cost:
		mine_button.click()
	elif money >= factory_cost:
		factory_button.click()
	elif money >= grandma_cost:
		grandma_button.click()
	elif money >= cursor_cost:
		cursor_button.click()

end_time = time.time() + 300

while time.time() < end_time:
	cookie.click()
	money = float(driver.find_element(By.ID, value="money").text)
	if money > grandma_cost:
		grandma_button.click()
	time.sleep(0.1)




# if time.time() > time_to_finish:
# 	cookies_per_second = driver.find_element(By.ID, value="cps")
# 	print(cookies_per_second.text)
# 	driver.quit()






