import csv
from bs4 import BeautifulSoup

filename = "sporty.csv"
mydict = []

with open("sporty.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')


odds = soup.find_all('div', class_="m-market m-market")
for odd in odds:
    #home_odd = odd[0]
    #print (odd[0].text)
    print (odd.text)
    print ('@@@@@@@@@@@@@@@@@@@')


teams = soup.find_all('div', class_="m-event--main")
for team in teams:
    home = team.find('div', class_="m-team-name m-home-team").text
    away = team.find('div', class_="m-team-name m-away-team").text
    #print (f"{home} vs {away}")

    mydict.append({'away_name': away, 'home_name': home})
#print (mydict)


fields = ['home_name', 'away_name']

with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(mydict)
