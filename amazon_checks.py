from selenium import webdriver # is this webdriver that is going to be driving our browser and automate tasks
from selenium.webdriver.common.by import By

# link = "https://www.amazon.co.uk/RDX-Standing-Pedestal-Freestanding-Kickboxing/dp/B08M4BNDTT/ref=sr_1_6?crid=HWRZ3NRNT7X2&dib=eyJ2IjoiMSJ9.mX4GP146Dmv-kqYZ_2E9HWTSAlPC3US2Qol_iZX7zqwrHYffRv57fDl5ydILHtgzHVR0SWhCt56DK-mvQgZMhlz88kpeWNBshXEnJvGFFGRM0hZgbJ5FoRlPDF2iXXxbUdhIzyoNyeOSlN1i_ZLi2hgWrO5pXmSq5vmOHkR_WZbIDZoS6EDVSHS3WVZBCVVpIWrcHNMT3UzXrfqK49UOZrJU3E7QZqjyAcqAf3NuDkqiXmJiI8y_XuPV_hV9Ab052Xzl4feOMyomYTxtlQIerrka9YANfwiiR6UJxB8AtPE.dgMgfJtmfFIBjMsiIKfHALdUX8YGZEvsMCTzhSSYOjg&dib_tag=se&keywords=standing%2Bboxing%2Bbag&qid=1717094824&sprefix=standing%2Bboxing%2Bbag%2Caps%2C73&sr=8-6&ufe=app_do%3Aamzn1.fos.d7e5a2de-8759-4da3-993c-d11b6e3d217f&th=1&psc=1"
# Initially, the browser will open but will close shortly after.
# To keep browser open we have to configure our webdriver:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Now we pass our configuration to our webdriver:

driver = webdriver.Chrome(options=chrome_options)

# And now, when we run, the browser will stay on.
# driver.get(link)

# Now let's find elements, using different methods:
## a) By.CLASS_NAME:
# price_pounds = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_pences = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"The price is {price_pounds.text}.{price_pences.text}")

## b) By.NAME:
# driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar) # it won't give you the HTML, but it will print out as a Selenium element
# # if we want to tap in various attributes (or text, or tags) we have to do that using a ".":
# print(search_bar.tag_name)

## c) By.ID:
# driver.get("https://www.python.org")
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# # d) By.CSS_SELECTOR:
# driver.get("https://www.python.org")
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# # e) By.XPATH:
# driver.get("https://www.python.org")
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# MULTIPLE ELEMENTS FIND: Pull out Dictionary of "Upcoming Events" on python.org website:
driver.get("https://www.python.org")
events_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range (len(events_dates)):
	events[n] = {
		"date": events_dates[n].text,
		"name": events_names[n].text
	}

print(events)



# To close the browser:
# driver.close() # .close() method closes a single active tab
# or:
driver.quit() # .quit() method will quit the entire browser

