import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service_obj = Service("D:/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://www.flipkart.com/")
time.sleep(2)

search_term = input("Enter your search Term:- ")
search = driver.find_element(By.NAME, "q").send_keys(search_term)
driver.find_element(By.XPATH, "//button[@type = 'submit']").click()

items = driver.find_elements(By.XPATH, "//div[@class='_75nlfW']")

for item in items:
    item.click()
    driver.switch_to.window(driver.window_handles[1])
    name = driver.find_element(By.XPATH, "//span[@class='VU-ZEz']").text
    price = driver.find_element(By.XPATH, "//div[@class='Nx9bqj CxhGGd']").text

    try:
        mrp = driver.find_element(By.XPATH, "//div[@class='yRaY8j A6+E6v']").text
        discount = driver.find_element(By.XPATH, "//div[@class='UkUFwK WW8yVX']").text
        reviews = driver.find_element(By.XPATH, "(//span[@class='Y1HWO0'])[1]").text
    except:
        pass

    print(f"name is {name}")
    print(price)

    try:
        print(mrp)
        print(discount)
        print(reviews)
    except:
        pass
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

time.sleep(3)
