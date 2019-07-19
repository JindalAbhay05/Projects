#basic coments are down the page
import requests
from bs4 import *
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
data = requests.get("https://www.accuweather.com/en/in/bathinda/190068/weather-forecast/190068", headers=headers)
# print(data) # prints : response:200

soup = BeautifulSoup(data.text, "html.parser")
soup.prettify()
#print(soup.find('div', {'class':'info'}))
data2 = soup.find('div', {'class': 'info'})
data3 = soup.find('span', {'class': 'large-temp'})
print(data3.contents[0])
# or
print(data3.string)








#   Only prettify function as it corrects the various errors in our html
'''from bs4 import BeautifulSoup

soup = BeautifulSoup("<html><p>dsfjdsfj<strng>Hello<a>Hello</p></html>","html.parser")
#print(soup.prettify())#errors are gone
#  after this all errors has been fixed in the soup and if you print
print(soup) # all the ierrors are removed (all the tags have been added)

soup.head # it will  reatern all the head head contents

soup.body.a #it will return the first a tag in the body

#if we want all the a tags of the body
array = soup.find_all('a')
# and then print each 'a'

array[0]
array[1]
array[2]
#will return all the 'a' tags
'''



