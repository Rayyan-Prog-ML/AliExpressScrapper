from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver=webdriver.Chrome()
query="laptop"
count=1
try:
    for page in range(1,5):
        if page==1:
            driver.get(f"https://aliexpress.com/w/wholesale-{query}.html?spm=a2g0o.best.search.0")
        else:
            driver.get(f"https://www.aliexpress.com/w/wholesale-laptop.html?page={page}&g=y&SearchText=laptop")
        elements=driver.find_elements(By.CLASS_NAME, "multi--container--1UZxxHY")
        print(f"The no of books are in page {page} are {len(elements)}")
        for product in elements:
            data=product.get_attribute("outerHTML")
            with open(f"Aliexpress/product{count}.html","w",encoding="utf-8") as f:
                f.write(data)
                count+=1
except Exception as e:
    print(e)

time.sleep(3)
driver.close()
