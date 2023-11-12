from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup
import urllib.request
import ssl

def insta_searching(word):
    url = "https://www.instagram.com/explore/tags/"+str(word)
    return url

def select_first(driver):
    first = driver.find_elements(By.CSS_SELECTOR,"div._aagw")[0]
    first.click()
    driver.implicitly_wait(10)
    
def move_next(driver):
    right =  driver.find_elements(By.CSS_SELECTOR,"div._aaqg._aaqh")[0]
    right.click()
    driver.implicitly_wait(10)
    
def get_contents(driver):
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    try:
        content = soup.select('div._a9zs')[0].text
    except:
        content = ''
        
    tags = re.findall(r'#[^\s#,\\]+',content)
    date = soup.select('time._aaqe')[0]['datetime'][:10]

    try:
        #like = soup.select('div._ap3a._aaco._aacu._aacx._aada._aade')[0].findAll('span')[-1].text()
        like = str(soup.select('span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs'))
        #like = like + " size = " + str(len(like))
        like = like[249:-8]
    except:
        like=0
        
    try:
        place = soup.select('div._aaqm')[0].text
    except:
        place='nope'
        
    data = [content,date,like,place,tags]
    return data
        


ssl._create_default_https_context = ssl._create_unverified_context
import time

from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://instagram.com")

driver.implicitly_wait(10)

id = input("ID:")
pwd = input("PWD:")
login_id=driver.find_element(By.CSS_SELECTOR,'input[name="username"]')
login_id.send_keys(str(id))
login_pwd=driver.find_element(By.CSS_SELECTOR,'input[name="password"]')
login_pwd.send_keys(str(pwd))

login_id.send_keys(Keys.ENTER)
driver.implicitly_wait(10)

time.sleep(8)
#word = "플리마켓"
word = input("태그 입력:")
word = str(word)
url = insta_searching(word)

driver.get(url)
driver.implicitly_wait(10)

select_first(driver)

results=[]
target=5
for i in range(target):
    try:
        data = get_contents(driver)
        results.append(data)
        print(results[-1][0]) #content
        print(results[-1][1]) #date
        print(results[-1][2]) #like
        print(results[-1][3]) #place
        print(results[-1][4]) #tags
        move_next(driver)
    except:
        time.sleep(2)
        move_next(driver)
    time.sleep(5)
        
        
