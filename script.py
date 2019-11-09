from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xgraphics+card.TRS0&_nkw=graphics+card&_sacat=0'

# fetch data from URL 
uClient = uReq(my_url)
page_data = uClient.read()
uClient.close()

# html parsing
page_data_soup = soup(page_data, 'html.parser')
products = page_data_soup.find_all('li', {'class':'sresult lvresult clearfix li shic'}) 
print(len(products))