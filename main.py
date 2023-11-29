from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import pandas as pd
driver = wd.Chrome()
driver.maximize_window()
driver.get('https://www.century21.com/real-estate/new-city-ny/LCNYNEWCITY/')
driver.implicitly_wait(5)
click_on_grid = driver.find_element(By.XPATH, '//*[@id="gallery-view-button"]')
click_on_grid.click()
driver.implicitly_wait(5)
url_link = driver.find_elements(
    By.XPATH, '//*[@id="results-parent"]/div[1]/div[2]/div/div[2]/a')
title_list = []
titles = driver.find_elements(By.XPATH, '//*[@class="property-address-info"]')
url_links_list = []
price_list = []
for link, title in zip(url_link, titles):
    url_links_list.append(link.get_attribute('href'))
    price_list.append(link.text)
    title_list.append(title.text)
data = {
    "property_url": url_links_list,
    "property_title": title_list,
    "price": price_list
}
df = pd.DataFrame(data)
df.to_csv("anees_pretask.csv", index=False)
driver.quit()
