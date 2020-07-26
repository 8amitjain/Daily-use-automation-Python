import requests
from bs4 import BeautifulSoup
import math

Stock_name = 'ACC'
url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuoteFO.jsp?underlying=' + Stock_name \
      + '&instrument=FUTSTK&expiry=30JUL2020'

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E;\
 .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; Zoom 3.6.0; Microsoft Outlook 16.0.10730; \
 Microsoft Outlook 16.0.10730; ms-office; MSOffice 16)'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find(id='responseDiv').getText().strip().split(':')
print(data)
for x in data:
    x = ''.join(x)
    if "closePrice" in x:
        quant = x.split(',')

    if "lastPrice" in x:
        lp = x.split(",")

qty = quant[0][1:-1]
print(qty)
l_price = lp[0][1:-3]
print(l_price)
# l_price = math.ceil(l_price)  # rounding to high 5.2 -> 6
print(l_price)
