import requests
from bs4 import BeautifulSoup

for i in range('no. of indexes'):
    url=""+str(i)
    response = requests.get(url)
    htmlContent = response.text
    soup = BeautifulSoup(htmlContent, 'lxml')
    td= soup.find_all('td')
