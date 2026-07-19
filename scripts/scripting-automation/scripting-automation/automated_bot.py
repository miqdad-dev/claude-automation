import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def automated_bot(url, search_term):
    driver = webdriver.Chrome()
    driver.get(url)

    search_box = driver.find_element_by_name('q')
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    results = driver.find_element_by_class_name('g')
    print(results.text)

    driver.quit()

if __name__ == "__main__":
    automated_bot("http://www.google.com", "Python")