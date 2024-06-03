from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

game_link = "https://orteil.dashnet.org/experiments/cookie/"

driver.get(game_link)

iteration = 0

def get_element_text_as_float(element):
    return float(element.text.split(" - ")[1].split("\n")[0].replace(",", ""))

def upgrade_if_possible():
    global money

    try:
        time_machine_cost = get_element_text_as_float(driver.find_element(By.ID, value="buyTime machine"))
        if money >= time_machine_cost:
            driver.find_element(By.ID, value="buyTime machine").click()
            return
    except Exception:
        pass

    try:
        portal_cost = get_element_text_as_float(driver.find_element(By.CSS_SELECTOR, value="#buyPortal b"))
        if money >= portal_cost:
            driver.find_element(By.ID, value="buyPortal").click()
            return
    except Exception:
        pass

    try:
        alchemy_lab_cost = get_element_text_as_float(driver.find_element(By.ID, value="buyAlchemy lab"))
        if money >= alchemy_lab_cost:
            driver.find_element(By.ID, value="buyAlchemy lab").click()
            return
    except Exception:
        pass

    try:
        shipment_cost = get_element_text_as_float(driver.find_element(By.CSS_SELECTOR, value="#buyShipment b"))
        if money >= shipment_cost:
            driver.find_element(By.ID, value="buyShipment").click()
            return
    except Exception:
        pass

    try:
        mine_cost = get_element_text_as_float(driver.find_element(By.CSS_SELECTOR, value="#buyMine b"))
        if mine_cost <= 3600:
            if money >= mine_cost:
                driver.find_element(By.ID, value="buyMine").click()
                return
    except Exception:
        pass

    try:
        factory_cost = get_element_text_as_float(driver.find_element(By.CSS_SELECTOR, value="#buyFactory b"))
        if factory_cost <= 1500:
            if money >= factory_cost:
                driver.find_element(By.ID, value="buyFactory").click()
                return
    except Exception:
        pass


    try:
        grandma_cost = get_element_text_as_float(driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b"))
        if grandma_cost <= 230:
            if money >= grandma_cost:
                driver.find_element(By.ID, value="buyGrandma").click()
                return
    except Exception:
        pass

    # try:
    #     cursor_cost = get_element_text_as_float(driver.find_element(By.CSS_SELECTOR, value="#buyCursor b"))
    #     if money >= cursor_cost:
    #         driver.find_element(By.ID, value="buyCursor").click()
    #         return
    # except Exception:
    #     pass

start_time = time.time()
end_time = start_time + 300
upgrade_time = start_time

while time.time() < end_time:
    cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
    cookie.click()
    iteration += 1
    if time.time() - upgrade_time >= 5:
        money = float(driver.find_element(By.ID, value="money").text.replace(",", ""))
        upgrade_if_possible()
        upgrade_time = time.time()
    # time.sleep(0.1)

if time.time() > end_time:
    cookies_per_second = driver.find_element(By.ID, value="cps")
    print(f"Final score (5min): {cookies_per_second.text}")
    driver.quit()