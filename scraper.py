#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://github.com/topics')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# get the repo list
repo = soup.find(class_="col-lg-9 position-relative pr-lg-5 mb-6 mr-lg-5")

# find all instances of that class (should return 25 as shown in the github main page)
repo_list = repo.find_all(class_="py-4 border-bottom d-flex flex-justify-between")

print(len(repo_list))

file_name = "github_trending_today.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))
f.writerow(['Topic', 'Link'])

for repo in repo_list:
    topic = repo.find('p').text
    link = repo.find('a').href
    f.writerow([topic, link])


    
  
