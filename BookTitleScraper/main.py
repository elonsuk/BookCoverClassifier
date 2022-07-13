from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

urls = [f'https://thegreatestbooks.org/?page={i+1}' for i in range(4)]

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) ,options=options)

file = open('list.txt', 'w+')

for url in tqdm(urls):
    driver.get(url)
    boxes = [driver.find_element(By.XPATH, f'/html/body/div[2]/div/div[2]/div/div/div/div[2]/ol/li[{i+1}]') for i in range(50)]

    for i, box in enumerate(boxes):
        title = box.find_element(By.XPATH, f'/html/body/div[2]/div/div[2]/div/div/div/div[2]/ol/li[{i+1}]/div/div/div/h4/a[1]').text
        author = box.find_element(By.XPATH, f'/html/body/div[2]/div/div[2]/div/div/div/div[2]/ol/li[{i+1}]/div/div/div/h4/a[2]').text
        file.write(f'{title} by {author}\n')

file.close()
driver.close()