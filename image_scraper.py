from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from bs4 import BeautifulSoup
import os


# 1.利用Selenium套件操作網頁
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://pixabay.com/images/search/car/')

for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(5)

# 2.利用BeautifulSoup套件爬取網頁圖片的連結
soup = BeautifulSoup(driver.page_source, 'lxml')

images = soup.find_all('a', {'class': 'link--h3bPW'})

image_links = [image.find('img').get('src') for image in images]
# 3.下載圖片
for index, link in enumerate(image_links):

    if not os.path.exists('image'):
        os.mkdir('image')

    img = requests.get(link)

    with open(f'image\\{index+1}.jpg', 'wb') as file:
        file.write(img.content)
