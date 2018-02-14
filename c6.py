import requests
from bs4 import BeautifulSoup
r=requests.get("http://cs.unh.edu/~anarayan/Scraping/Navigation.html")
c=r.content
soup=BeautifulSoup(c,"html.parser")

def count():
    data =[]


cost =[]
for child in soup.find("table",{"id":"giftList"}).children:
    baby = child.find("td")
    count = 0
    for baby in child:
        count +=1
        if count == 3:
            cost.append(baby.get_text().replace("\n","").replace("\r","").replace("$","").replace(",",""))

cost.pop(0)

cost = [float(i) for i in cost]

print("The total cost for all gifts would be :" + str(sum(i for i in cost)))
