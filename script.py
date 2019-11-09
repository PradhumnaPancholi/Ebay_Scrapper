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

# extracting requried data from html
for product in products:

    product_name = product.h3.a.text

    product_price_container = product.ul.find('li', {'class':'lvprice prc'})
    product_price = product_price_container.span.text

    product_shipping_type_container = product.ul.find('li', {'class':'lvshipping'})
    product_shipping_type = product_shipping_type_container.span.span.text

    product_hotness_container = product.ul.find('li', {'class':'lvextras'})
    product_hotness = product_hotness_container.div.text

    product_seller_location = product.find('ul', {'class':'lvdetails'}).find('li', {'class':''}).text

    print(product_name, product_price, product_shipping_type, product_hotness, product_seller_location)


# write data onto a csv file
