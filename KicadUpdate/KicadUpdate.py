import wget
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
#get program file path
dirname = os.path.dirname(__file__)
#make path with appended relative path
filename = os.path.join(dirname, 'chromedriver_win32\\chromedriver.exe')
#get Chrome Browser Web driver options
options = webdriver.ChromeOptions()
#make it headless
options.add_argument('headless')
#make the headless window this size
options.add_argument('window-size=1200x600')
#create our browser
browser = webdriver.Chrome(chrome_options=options,executable_path=filename)
#go to this webpage. This has the download links for the daily builds
browser.get('https://kicad-downloads.s3.cern.ch/index.html?prefix=windows/nightly/')
#wait for javascript on page to populate
time.sleep(5)
#take html and put into Beautiful Soup
soup = BeautifulSoup(browser.page_source, 'html.parser')
#close our browser becasue we are done using it
browser.close()
# drill down through the html to the links
links = soup.find_all("div", {"id": "listing"}, 'pre')

last_url = ''

for a in soup.find_all('a', href=True):
    #if its a 64bit exe
    if '64.exe' in a['href']:
        #will give us the last 64bit exe link in the list
        last_url = a['href']
#download the file at this link
wget.download(last_url, dirname) 
