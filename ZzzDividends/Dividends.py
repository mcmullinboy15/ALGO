import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas.io.json import json_normalize

'''
Selenium:  Selenium is a web testing library. It is used to automate browser activities.
BeautifulSoup: Beautiful Soup is a Python package for parsing HTML and XML documents. It creates parse trees that is helpful to extract the data easily.
Pandas: Pandas is a library used for data manipulation and analysis. It is used to extract the data and store it in the desired format.
'''

'''<div class="market-calendar__body loaded">'''
# TODO Dividend Calendar API Call
link = 'https://www.nasdaq.com/market-activity/dividends'

# link = "https://www.thestreet.com/dividends/index.html#"
# urls = []

# r = requests.get(link)
# lines = r.iter_lines()
# print(r.text)
#
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)
# print(soup.find_all('div'))


# <tr class="yui-dt-first yui-dt-last"><th id="yui-dt0-th-Symbol" rowspan="1" colspan="1" class="yui-dt0-col-Symbol yui-dt-col-Symbol yui-dt-sortable yui-dt-first">

# from selenium import webdriver

# path = "/Users/amcmullin/Downloads/chromedriver"
# print(path)
# path = "/Users/amcmullin/chromedriver_s/73/chromedriver"
# print(path)
# driver = webdriver.Chrome(path)
# print(path)
#
# var = driver < - rsDriver(browser=c("chrome"), chromever="73.0.3683.68", extraCapabilities=eCaps)
#
# products = []  # List to store name of the product
# prices = []  # List to store price of the product
# ratings = []  # List to store rating of the product
# driver.get(
#     "<a href=\"https://www.flipkart.com/laptops/\">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops"
#     "-/pr?sid=6bo%2Cb5g&uniq")
#
# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
#     name = a.find('div', attrs={'class': '_3wU53n'})
# price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
# rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
# products.append(name.text)
# prices.append(price.text)
# ratings.append(rating.text)
#
# df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
# df.to_csv('products.csv', index=False, encoding='utf-8')

# '''Browser from Splinter'''
# from splinter import Browser
# import pandas as pd
#
#
#
# url="https://www.google.com"
#
#
# browser = Browser('chrome')
# browser.visit(url)
#
# search_bar_xpath = '//*[@id="lst-ib"]'
# search_bar = browser.find_by_xpath(search_bar_xpath)[0]
# search_bar.fill("Tony_stark is Iron_Man")
#
#
# search_button_xpath = '//*[@id="tsf"]/div[2]/div[3]/center/input[1]'
# search_button = browser.find_by_xpath(search_button_xpath)[0]
# search_button.click()
#
#
# search_results_xpath = '//h3[@class="r"]/a'
# search_results = browser.find_by_xpath(search_results_xpath)
#
#
# scraped_data = []
# for search_result in search_results:
#
#     title = search_result.text.encode('utf8')
#     link = search_result["href"]
#     scraped_data.append((title, link))
#
# df = pd.DataFrame(data=scraped_data, columns=["title", "link"])
# df.to_csv("links.csv")
