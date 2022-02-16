from math import sqrt
import numpy as np
from statistics import mode

def insert_value():
    num_list = []
    lenght = int(input("\nInserire quantità numeri: "))
    for i in range(lenght):
        num_list.append(float(input(f"Inserire numero {str(i+1)}: ")))
    return num_list

def get_average(list):
    med = 0
    for i in range(len(list)):
        med += list[i]
    med /= len(list)
    return med

def get_mode(list, val):
    mode_list = np.zeros( (len(list), 2) )
    cont = pos = 0
    for i in range(len(list)):
        check = False
        for j in range(len(list)):
            if list[i] == mode_list[j][0]:
                pos = j
                check = True
                break
        if check:
            mode_list[pos][1] += 1
        else:
            mode_list[cont][0] = list[i]
            mode_list[cont][1] = 1
            cont += 1
    for i in range(cont):
        print(f"{str(i)}) [{str(mode_list[i][0])}] = {str( int(mode_list[i][1]) )} volte")
    if val == 1:
        print("\nIl numero con maggior frequenza è: " + str(mode(list)))
    else:
        return mode_list, cont

def get_median(list):
    list.sort()
    if len(list)%2 == 0:
        x1 = list[int( len(list)/2 )]
        x2 = list[int( (len(list)/2)-1 )]
        print("La mediana è " + str( get_average([x1, x2]) ))
    else:
        print("La mediana è " + str( list[ int(len(list)/2) ] ))
        
def get_weighted_average(list):
    som = som_div = 0
    choice = int(input("\nVuoi usare la lista predefinita(1) o inserire una nuova(2)?\n"))
    if choice == 1:
        mode, cont = get_mode(list, 0)
    elif choice == 2:
        cont = int(input("\nInserire quantità numeri: "))
        mode = np.zeros( (cont, 2) )
        for i in range(cont):
            mode[i][0] = float(input(f"\nInserire numero {str(i+1)}: "))
            mode[i][1] = int(input(f"Inserire peso numero {str(int(mode[i][0]))}: "))
        for i in range(cont):
            print(f"{str(i)}) [{str(mode[i][0])}] | peso: {str( int(mode[i][1]) )} ")
    if choice == 1 or choice == 2:
        for i in range(cont):
            som += mode[i][0] * mode[i][1]
            som_div += mode[i][1]
        print("\nLa media ponderata è " + str(som/som_div))
    else:
        print("\nScelta inesistente")

def get_standard_deviation(list):
    som = 0
    for i in range(len(list)):
        som += pow( (list[i] - get_average(list)) ,2)
    som = sqrt( (som/len(list)) )
    print("\nLo scarto quadratico medio è " + str(som))


numbers = insert_value()
while True:
    print('-------------------------------------------------')
    choice = int(input("""
    \tOpzione 1: Media
    \tOpzione 2: Mediana
    \tOpzione 3: Moda
    \tOpzione 4: Scarto quadratico medio
    \tOpzione 5: Media ponderata
    \tOpzione 6: Inserire nuovi valori
    \tOpzione 7: Stampa lista
    \tOpzione 0: Uscita dal programma.\n
    \tinserire valore opzione:  """))
    if choice == 1:
        print("\nLa media dei valori è :" + str( get_average(numbers) ))
    elif choice == 2:
        get_median(numbers)
    elif choice == 3:
        get_mode(numbers, 1)
    elif choice == 4: 
        get_standard_deviation(numbers)
    elif choice == 5:
        get_weighted_average(numbers)
    elif choice == 6:
        numbers = insert_value()
    elif choice == 7:
        print()
        for i in range(len(numbers)):
            print(f"{str(i+1)}) {str(numbers[i])}")
    elif choice == 0:
        break
    else:
        print("\nScelta inesistente")