from bs4 import BeautifulSoup
import pandas as pd
import requests
import time


################################################################
# Script to filter out only the working links from the dataset #
################################################################


def script(HEADERS):
    # reading the dataset
    df = pd.read_csv("data.csv")

    # storing the asin in a list
    asin = list(set(df["Asin"]))

    # finding the only correct and working links and not considering the broken links
    good_linkde = []
    good_linkfr = []
    good_linkit = []
    good_linkes = []

    # ['de' 'fr' 'it' 'es']  As there are 4 different countries in our dataset, we will be using combinations of the asin with the 4 countries in our links
    for i in asin:

        # finding all link of products for Germany
        link1 = "https://www.amazon.de/dp/" + i
        url1 = requests.get(link1, headers=HEADERS)
        time.sleep(0.5)

        # finding all link of products for France
        link2 = "https://www.amazon.fr/dp/" + i
        url2 = requests.get(link2, headers=HEADERS)
        time.sleep(0.5)

        # finding all link of products for Italy
        link3 = "https://www.amazon.it/dp/" + i
        url3 = requests.get(link3, headers=HEADERS)
        time.sleep(0.5)

        # finding all link of products for Spain
        link4 = "https://www.amazon.es/dp/" + i
        url4 = requests.get(link4, headers=HEADERS)

        # checking if the all the links are working or not
        if (
            url1.status_code == 200
            and url2.status_code == 200
            and url3.status_code == 200
            and url4.status_code == 200
        ):
            good_linkde.append(link1)
            good_linkfr.append(link2)
            good_linkit.append(link3)
            good_linkes.append(link4)

    #  storing all the working links in a list
    good_links = good_linkde + good_linkfr + good_linkit + good_linkes

    # storing all the working links in a text file for the record
    saving = open("good_links.txt", "w")
    saving.write(str(good_links))
    saving.close()
    return "Done"


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
}

print(script(HEADERS))
