import requests
from bs4 import BeautifulSoup
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://beomi.github.io/beomi.github.io_old/')

html = req.text
soup = BeautifulSoup(html,'html.parser')
my_titles = soup.select('h3 > a')

data = {}

for title in my_titles:
    print(title.text)
    data[title.text] = title.get('href')
with open(os.path.join(base_dir,'result.json'),'w') as json_file:
    json.dump(data,json_file)
    

