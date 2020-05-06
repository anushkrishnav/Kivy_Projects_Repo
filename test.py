import requests
from bs4 import BeautifulSoup


page = requests.get('https://github.com/trending')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# get the repo list
box = soup.find(class_="Box")

box_list=box.find_all(class_='Box-row')

print(len(box_list))