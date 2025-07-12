import requests
from bs4 import BeautifulSoup
f1=open("links.txt","rt",encoding="utf-8")
ms=f1.read()
links=ms.strip().split("\n")
for link in links:
    web=requests.get(link)
    soup=BeautifulSoup(web.content)
    dvs=soup.find_all("div",{"class":"news-main-image"})
    img=dvs[0].find_all("img")[0]["src"]
    n=img.strip().split("/")[-1].strip().split("?")[0]
    f2=open("imagess/"+n,"wb")
    web=requests.get(img)
    f2.write(web.content)
    f2.close()
    