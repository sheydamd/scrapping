import requests
from bs4 import BeautifulSoup
web=requests.get("https://www.varzesh3.com")
soup=BeautifulSoup(web.content)
#print(soup.prettify())
dvs=soup.find_all("div",{"class":"widget news"})
links=dvs[1].find_all("a")+dvs[2].find_all("a")
with open("links.txt","wt") as f1:
    for link in links:
        if "https://video.varzesh3.com/" not in link["href"]:
            f1.write(link["href"]+"\n")