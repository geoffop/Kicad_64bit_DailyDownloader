import wget
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'chromedriver_win32\\chromedriver.exe')

options = webdriver.ChromeOptions()

options.add_argument('headless')

options.add_argument('window-size=1200x600')

browser = webdriver.Chrome(chrome_options=options,executable_path=filename)

browser.get('https://kicad-downloads.s3.cern.ch/index.html?prefix=windows/nightly/')

time.sleep(5)

soup = BeautifulSoup(browser.page_source, 'html.parser')

browser.close()

links = soup.find_all("div", {"id": "listing"}, 'pre')

last_url = ''

for a in soup.find_all('a', href=True):

    if '64.exe' in a['href']:

        last_url = a['href']

wget.download(last_url, dirname) 
