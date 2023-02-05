#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://www.sportybet.com/ng/sport/basketball/sr:category:15/sr:tournament:132')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# get the repo list
repo = soup.find(class_="match-league-wrap")

# find all instances of that class (should return 25 as shown in the github main page)
repo_list = repo.find_all(class_="m-table-row m-content-row match-row")

print(len(repo_list))

file_name = "Odd.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))
f.writerow(['Home', 'Away'])

for repo in repo_list:
    Home = repo.find(class_="home-team").text 
    Away = repo.find(class_="away-team").text
    f.writerow([Home, Away])


    
  
