# Interact with web pages:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # This "Keys" class, had a bunch of constants that allow us do staff like press "ENTER".

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# link = "https://en.wikipedia.org/wiki/Main_Page"
#
# driver.get(link)
# articles_volume = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(articles_volume.text)

# # # Click on elements:
# # articles_volume.click()
#
# # Faster way to click on elements is to find elements using the "By.LINK_TEST" method:
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Type in (Sending Keyboard input in Selenium):
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Romania", Keys.ENTER) # Type in then hit Enter


# # Form Sign Up Bot Challenge:
# form_challenge_link = "https://secure-retreat-92358.herokuapp.com/"
#
# driver.get(form_challenge_link)
#
# first_name = driver.find_element(By.NAME, value="fName")
# first_name.send_keys("Andrei")
# last_name = driver.find_element(By.NAME, value="lName")
# last_name.send_keys("Cosofret")
# email = driver.find_element(By.NAME, value="email")
# email.send_keys("acosofretcwst@gmail.com", Keys.ENTER)



# driver.quit()