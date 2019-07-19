import requests
import re
from bs4 import *
#https://www.google.com/search?client=firefox-b-d&q=google+stock
try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;     rv:67.0) Gecko/20100101 Firefox/67.0'}
    one = "https://www.google.com/search?client=firefox-b-d&q="
    stock = input("Enter the stock you  want to find")
    other = "+stock"
    url = one+stock+other
    #print(url)
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, "html.parser")
    soup.prettify()
    data2 = soup.find('div', {'class': 'gsrt'})
    #IsqQVc NprOob
    for tag in soup.find_all('span', re.compile("^IsqQVc NprOob")):
        pass

    #print(data2.prettify())
    for tag1 in soup.find_all('span', re.compile("^knFDje")):
        pass

    print(tag.contents[0])

    for tag2 in soup.find_all('span', re.compile("i-ytLA")):
        print(tag1.contents[0] +" "+ tag2.string)
except:
    print("There is no company named as" + stock)
