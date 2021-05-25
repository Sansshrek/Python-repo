from bs4 import BeautifulSoup
import requests

# This program works only with sites that
link = str(input("Inserire link da controllare: " ))
soup = BeautifulSoup(requests.get(link).content, 'html.parser')
soupstr = str(soup)
print(soup.prettify())
check = False
pos = 0
for i in range(2, len(soupstr)):
    st = soupstr[i-2] + soupstr[i-1] + soupstr[i]
    if st == "404":
        print("Il sito non esiste")
        pos = i

print("posizione " + str(pos) + " = "+ soupstr[pos-2] + soupstr[pos-1] + soupstr[pos])
if '404' in soupstr:
    print("Il sito non esiste")
else:
    soup = BeautifulSoup(requests.get(link).content, 'html5lib')
    soupstr = str(soup)
    if '404' in soupstr:
        print("Il sito non esiste")
    else:
        print("Il sito esiste")
