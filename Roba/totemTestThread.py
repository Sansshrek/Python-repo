from bs4 import BeautifulSoup
import requests
import random
import string
import threading
# code buono: H18F04
# code merda: H17F07

lista_buoni = lista_visti = []

class threadTest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.max_cont = 2176782335
    def generateRandom():
        char = string.ascii_uppercase + string.digits
        return "".join(random.choice(char) for i in range(6))
    def run(self):
        cont = 0
        while cont < self.max_cont:
            while True:
                rCode = generateRandom()
                if rCode not in list_visti:
                    break
            print()
            print(self.name + " " + rCode)
            list_visti.append(rCode)
            cont += 1
            link = "https://www.tot-em.com/it/ascoltare/" + rCode

            soup = BeautifulSoup(requests.get(link).content, "html.parser")
            audio = soup.find("div", {"class": "svg-wrapper"})
            if audio != None:
                print("Trovato")
                list_buoni.append(rCode)
    
thread1 = threadTest("thread-1")
thread2 = threadTest("thread-2")
thread3 = threadTest("thread-3")
thread4 = threadTest("thread-4")
thread5 = threadTest("thread-5")

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()


print("\n\n\nLista link buoni")
for code in self.list_buoni:
    print(code)