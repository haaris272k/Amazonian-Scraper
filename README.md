# Amazonian-scraper
An advance web scraper developed to scrape the data from amazon.

# Approach

  1> I have followed the approach of dividing the task into subtasks, because that makes our work easier especially while dealing with data.

  2> As most of the links were'nt working so, first i developed a script to extract the only working links (out of 1000). 
 
  3> I used pandas library to handle the data and requests module to handle the requests to the url.

  4> I checked the response (status code) of every link to differentiate between working and broken, then stored all working links in a list.

  5> The above mentioned script (working_links.py) helped me in getting the links (180 links out of 1000) which were working properly and helped me 
       to proceed further without any hassle.

  6> I stored all the links both in a text file (good_links.txt) and as a list in python file (good_links.py) so as to maintain a record and use in
       my main program respectively.

  7> After getting appropriate links i started working with my main script (final.py) to scrape the relevant data.

  8> I used selenium tool and related Classes to automate the web browser (used Chrome) and to help in scraping of the data. 

  9> The Selenium related classes helped in proper functioning of the web browser by increasing the speed and allowing almost error free functioning.

  10> Scraped the Product title, Product image url, Product price and Product description using beautiful soup, requests and lxml libraries respectively.

  11> Used exception handling to deal with various possible scenarious as there was a lot of data to be scraped and from different links.

  12> At last, after scrapng from each link is done I stored all the scraped data in a list of dictionaries then dumped it to json data format.
