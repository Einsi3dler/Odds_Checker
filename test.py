#!/usr/bin/env python3
from bs4 import BeautifulSoup

with open("bet9ja.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#sports_tables = soup.find('div', class_="accordion-inner")

sports_tables = soup.find('div', class_="accordion-inner")

for table in sports_tables:
    print (table.text)


for table in soup.find('div', class_="accordion-item accordion-item accordion-item--open"):
    for x in table:
        print (x.text)
        print ('@@@@@@@@@@')

