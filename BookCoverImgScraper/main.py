import wget
import time
import os
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

init_url = 'https://www.ebay.com/b/Books-Movies-Music/bn_7000259849'
SAVE_PATH = r'C:\Users\offco\Documents\Dev_Projects\BookCoverClassifier\Datasets\Cover_images'

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) ,options=options)

search_list_file = open('search.txt', 'r')
search_list = search_list_file.readlines()

for search in tqdm(search_list):
    driver.get(init_url)
    FOLDER_NAME = search.split(' by ')[0]
    if ':' in FOLDER_NAME:
        FOLDER_NAME = FOLDER_NAME.replace(':', '-')
    IMG_SAVE_PATH = rf'{SAVE_PATH}\{FOLDER_NAME}'

    if os.path.isdir(IMG_SAVE_PATH):
        continue
    else:
        search_bar = driver.find_element(By.XPATH, '//*[@id="gh-ac"]')
        search_keyword = f'{search} book'
        search_bar.send_keys(search_keyword)
        search_button = driver.find_element(By.XPATH, '//*[@id="gh-btn"]')
        search_button.click()
        time.sleep(0.5)

        items = driver.find_elements(By.CLASS_NAME, 's-item__image-img')
        thumb_urls = [item.get_attribute('src') for item in items]
        img_urls = [f"https://i.ebayimg.com/images/g/{thumb.split('/')[6]}/s-l500.jpg" for thumb in thumb_urls[1:]]

        try: os.mkdir(IMG_SAVE_PATH)
        except FileExistsError: pass

        for i, url in enumerate(img_urls):
            image = wget.download(url, rf'{IMG_SAVE_PATH}\image_{i}.png')

driver.close()