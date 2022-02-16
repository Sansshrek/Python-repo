from bs4 import BeautifulSoup
import requests
import random
import string
import time
# code buono: H18F04
# code merda: H17F07


def generateRandom():
    char = string.ascii_uppercase + string.digits
    return "".join(random.choice(char) for i in range(6))

def prova():
    with open('python\Python-repo\Roba\data.txt', 'r') as file:
        data = file.read().split('\n')
        print(data)
        char = data[0].split(" ")
        ch1_start = int(char[0])
        ch2_start = int(char[1])
        ch3_start = int(char[2])
        ch4_start = int(char[3])
        ch5_start = int(char[4])
        ch6_start = int(char[5])    
        print(f"{ch1_start} {ch2_start} {ch3_start} {ch4_start} {ch5_start} {ch6_start}")
        cont = int(data[1])
        for i in range(2, len(data)):
            list_buoni.append(data[i])

list_buoni = []
cont = 0

while cont < 2176782335:
    char = string.ascii_uppercase + string.digits
    for ch1 in range(0, 36):
        for ch2 in range(0, 36):
            for ch3 in range(0, 36):
                for ch4 in range(0, 36):
                    for ch5 in range(0, 36):
                        for ch6 in range(0, 36):
                            start_time = time.time()
                            rCode = char[ch1] + char[ch2] + char[ch3] + char[ch4] + char[ch5] + char[ch6]
                            print()
                            print(f"{ch1} {ch2} {ch3} {ch4} {ch5} {ch6}")
                            cont += 1
                            print("Cont: "+str(cont))
                            link = "https://www.tot-em.com/it/ascoltare/" + rCode

                            soup = BeautifulSoup(requests.get(link).content, "html.parser")
                            audio = soup.find("div", {"class": "svg-wrapper"})
                            if audio != None:
                                print(rCode)
                                print("Trovato")
                                list_buoni.append(rCode)
                            else:
                                print(rCode + " - Non trovato")
                            average = time.time() - start_time
                            print("Average: "+str(average))
                            finish_time = 36*36*36*36*36*average
                            print("Tempo finale: "+str(finish_time))
                            missing_time = finish_time - time.time()
                            print("Tempo mancante: "+str(missing_time))
                            # lines = []
                            # with open('python\Python-repo\Roba\data.txt', 'r') as filer:
                            #     data = filer.read().split('\n')
                            #     data[0] = f"{ch1} {ch2} {ch3} {ch4} {ch5} {ch6}"
                            #     data[1] = str(cont)
                            #     if audio != None:
                            #         print(rCode)
                            #         print("Trovato")
                            #         list_buoni.append(rCode)
                            #         data.append(rCode)
                            #     else:
                            #         print(rCode + " - Non trovato")
                            #     with open('python\Python-repo\Roba\data.txt', 'w') as filew:
                            #         print()
                            #         for line in data:
                            #             print(line)
                            #             filew.write(line)
                            #             filew.write("\n")

                    print("\n\nLista link buoni")
                    for code in list_buoni:
                        print(code)

print("\n\n\nLista link buoni")
for code in list_buoni:
    print(code)
        
    