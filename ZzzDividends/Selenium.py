import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

path = "/Users/amcmullin/Downloads/chromedriver"
print(path)
path = "/Users/amcmullin/chromedriver_s/2.46/chromedriver"
print(path)
driver = webdriver.Chrome(executable_path=path)
print(path)

# path = "~/Applications/Firefox.app/Contents/MacOS/firefox"
# print(path)
# driver = webdriver.Firefox(path)
# print(path)

var = driver <- rsDriver(browser=c("chrome"), chromever="73.0.3683.68", extraCapabilities = eCaps)

products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product
driver.get(
    "<a href=\"https://www.flipkart.com/laptops/\">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops"
    "-/pr?sid=6bo%2Cb5g&uniq")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    name = a.find('div', attrs={'class': '_3wU53n'})
price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text)

df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
