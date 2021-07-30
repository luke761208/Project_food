# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.options import Options
#
#
# import pandas as pd
#
# filepath = 'C:/Users/Tibame_T14/Desktop/fda_cleaning.csv'
# df = pd.read_csv(filepath)
# fooddata = df.iloc[:,0]
# FDA_EN=[]
# for food in fooddata:
#     options = Options()
#     options.add_argument("--disable-notifications")
#     driver = webdriver.Chrome('./chromedriver', chrome_options=options)
#     driver.get("https://translate.google.com.tw/?hl=zh-TW&tab=TT&sl=zh-TW&tl=en")
#     element = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea').send_keys(food)
#     time.sleep(1)
#     data = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span')
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     en = soup.select('span[jsaction="click:qtZ4nf,GFf3ac,tMZCfe; contextmenu:Nqw7Te,QP7LD; mouseout:Nqw7Te; mouseover:qtZ4nf,c2aHje"]')[0].text
#     driver.close()
#     FDA_EN.append(en)
#
# print(FDA_EN)

from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import pandas as pd
# 用pandas 讀取 csv
filepath = 'C:/Users/Tibame_T14/Desktop/fda_cleaning.csv'
df = pd.read_csv(filepath)
# 定位欄位並顯示前五個
fooddata = df.iloc[0:5,0]
FDA_EN=[]
for food in fooddata:
    # 無頭模式
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # Selenium get()方法
    # 建立webdriver物件
    driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
    # 有了Selenium webdriver的物件後，就可以透過第10行的get()方法，前往要爬取的網頁網址。
    driver.get("https://translate.google.com.tw/?hl=zh-TW&tab=TT&sl=zh-TW&tl=en")
    # Selenium send_keys()方法
    element = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea').send_keys(food)
    time.sleep(1)
    #
    # data = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    en = soup.select('span[jsaction="click:qtZ4nf,GFf3ac,tMZCfe; contextmenu:Nqw7Te,QP7LD; mouseout:Nqw7Te; mouseover:qtZ4nf,c2aHje"]')[0].text
    driver.quit()
    FDA_EN.append(en)
with open("./fda_list_en", 'w', encoding='utf-8') as f:
    for each in
    f.write(FDA_EN)
print(FDA_EN)
