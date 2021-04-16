from bs4 import BeautifulSoup
import requests
# This program only works on this site: tv.animelove.it

while True:
    choice = int(input("Vuoi inserire il tuo risultato in un file? (1 per si) (2 per no)"))
    if choice == 1 or choice == 2:
        break
episode_num = int(input("Inserire numero episodi: "))
link = str(input("Inserire link primo episodio"))
link = link[:29] + "-video/streaming" + link[29:]
link = link[:46] + link[51:]
link = link[0:(len(link)-2)]
list = []
index = 1
print("Link base: "+ link)
file = open("link.txt", "w")
file.write("")
file.close()
for i in range(episode_num):
    linkUse = link + str(index)
    index += 1
    if (choice == 1):
        file = open("link.txt", "a")
        file.write(linkUse + "\n")
        file.close()
    list.append(linkUse)
print(*list,sep="\n")
