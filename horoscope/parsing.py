import requests
from bs4 import BeautifulSoup as bs

def parsing_description(url):
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    description = soup.find_all('div', class_ = 'e45a4c1552')
    description = soup.find_all('p')
    description = "\n\n".join([p.get_text() for p in description])
    return description