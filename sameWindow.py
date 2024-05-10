import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://www.flipkart.com/")
time.sleep(2)

search_term = input("Enter your search term:- ")
search_bar = driver.find_element(By.XPATH, "//input[@class='Pke_EE']").send_keys()
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)

items = driver.find_elements(By.XPATH, "//div[@class='_75nlfW']")

name = []
price = []
review = []

for item in items:
    name.append(item.find_element(By.XPATH, ".//div[@class='KzDlHZ']").text)
    price.append(item.find_element(By.XPATH, ".//div[@class='Nx9bqj _4b5DiR']").text)
    try:
        review.append(item.find_element(By.XPATH, ".//div[@class= 'XQDdHH']").text)
    except:
        pass



print(name)
print(price)
print(review)
print(len(review))

