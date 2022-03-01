from bs4 import BeautifulSoup
from good_links import good_links
from lxml import etree
import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


############################################################################
# Final script to scrape the relevant data from the filtered working links #
############################################################################


options = Options()

# headless browser for removing browser head pop
# options.add_argument("--headless")
# Required opetions for proper functioning of chromedriver
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")

# Increases speed for some sites
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")

# To bypass site restrictions for headless browsers
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
options.add_argument("user-agent={0}".format(user_agent))
br = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# creating an empty list to store the data
temp = []

# initializing a variable to keep the count of visited links
counter = 0

# scraping begins
for i in range(len(good_links)):
    counter += 1
    final = {}
    br.get(good_links[i])

    # scraping title
    product_title = br.find_element_by_xpath('//*[@id="productTitle"]').text

    # scraping image url
    image_url = br.find_element_by_xpath('//*[@id="imgBlkFront"]').get_attribute("src")

    # scraping product description
    try:
        product_description = br.find_element_by_xpath(
            '//*[@id="bookDescription_feature_div"]/div/div[1]/span'
        ).text
    except:
        product_description = br.find_element_by_xpath(
            '//*[@id="editorialReviews_feature_div"]'
        ).text

    # scraping price
    try:
        price = br.find_element_by_xpath('//*[@id="price"]').text
    except:
        try:
            price = br.find_element_by_xpath(
                '//*[@id="corePrice_feature_div"]/div/span/span[2]'
            ).text
        except:
            try:
                price = br.find_element_by_xpath('//*[@id="buyNew_noncbb"]/span').text
            except:
                try:
                    price = br.find_element_by_xpath(
                        '//*[@id="outOfStock"]/div/div[1]/span[1]'
                    ).text
                except:
                    try:
                        price = br.find_element_by_xpath(
                            '//*[@id="a-autoid-1-announce"]/span[2]'
                        ).text
                    except:
                        price = "Not available"
    time.sleep(3)

    # storing the data in a dictionary
    final["productLink"] = good_links[i]
    final["productTitle"] = product_title
    final["productPrice"] = price
    final["productImageURL"] = image_url
    final["productDescription"] = product_description

    # append the dictionary to the list
    temp.append(final)
    print(counter)
print("Scraping complete!")

# Storing the data in a json file
my_file = open("amazondata.json", "w")
my_file.write(json.dumps(temp))
my_file.close()
