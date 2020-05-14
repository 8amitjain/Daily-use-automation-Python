import requests 
import sys 
import webbrowser
import bs4 as bs 

"""
requried modules:
    requests
    webbrowser
    bs4
    
    This script is used to open specfic number of web page's that are top results of google search for that phrase.
"""
# res = requests.get('https://www.google.com/search?q=cube')  # .join(sys.argv[1:]))
data = 'hey'
url = 'https://www.google.com/search?q=' + data
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; Zoom 3.6.0; Microsoft Outlook 16.0.10730; Microsoft Outlook 16.0.10730; ms-office; MSOffice 16)'}
res = requests.get(url, headers=headers)
res.raise_for_status()

# b = webbrowser.get('chrome')

soup = bs.BeautifulSoup(res.text, 'html.parser')
link_element = soup.select('.r a')
link_to_open = 10  # number of page to open
for i in range(link_to_open):
    #  webbrowser.open(link_element[i].get('href'))
    webbrowser.open(link_element[i].get('href'))
# print(link_element)
# print()
# print(link_to_open)

