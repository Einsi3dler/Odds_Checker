#!/usr/bin/python3
import requests
urlx = "https://sports.bet9ja.com/popularCoupons/0/englandpremierleague/492"

r = requests.get(urlx)

with open("betty.html",'w') as f:

    f.write(r.content)

print(r.content)
