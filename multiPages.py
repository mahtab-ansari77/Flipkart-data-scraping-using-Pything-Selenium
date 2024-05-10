import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://www.flipkart.com/")
time.sleep(2)

search_term = input("Enter your search term:- ")
search_bar = driver.find_element(By.XPATH, "//input[@class='Pke_EE']").send_keys(search_term)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)


name = []
price = []
review = []

for i in range(3):
    items = driver.find_elements(By.XPATH, "//div[@class='_75nlfW']")
    for item in items:
        name.append(item.find_element(By.XPATH, ".//div[@class='KzDlHZ']").text)
        price.append(item.find_element(By.XPATH, ".//div[@class='Nx9bqj _4b5DiR']").text)
        try:
            review.append(item.find_element(By.XPATH, ".//div[@class= 'XQDdHH']").text)
        except:
            review.append(None)

    print(f"Iteration {i}:")
    print(f"  Name: {len(name)}")
    print(f"  Price: {len(price)}")
    print(f"  Review: {len(review)}")

    next_page = driver.find_element(By. XPATH, "//span[normalize-space()='Next']").click()
    time.sleep(5)


df = pd.DataFrame({"Product Name": name, "Price":price, "Reviews":review})
print(df)
df.to_csv("scrapData.csv")


