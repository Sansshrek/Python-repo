import random

def bin_search(arr, low, high, x):
    if len(arr) == 0:
        print("\nLa lista è vuota")
    else:
        if high >= low:
            mid = (low + high) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return bin_search(arr, low, mid-1, x)
            else:
                return bin_search(arr, mid+1, high, x)
        return -1
    
def bin_search1(arr):
    if len(arr) == 0:
        print("\nLa lista è vuota")
    else:
        arr.sort()
        print("\nArray in ordine di grandezza")
        print(arr)
        num = int(input("\nInserire valore da cercare: "))
        high = len(arr)-1
        low = cicli = 0
        check = False
        for i in range(len(arr)):
            mid = (low + high) // 2
            if arr[mid] == num:
                check = True
                cicli += 1
                break
            elif arr[mid] > num:
                high = mid-1
            else:
                low = mid+1
        
        if check:
            print(f"\nNumero cicli = {str(cicli)}\nIl valore {str(num)} è in posizione {mid}")
        else:
            print("\nIl valore non è stato trovato")

def search_array(arr):
    if len(arr) == 0:
        print("\nLa lista è vuota")
    else:
        arr.sort()
        print("\nArray in ordine di grandezza")
        print(arr)
        num_insert = int(input("\nInserire valore da cercare: "))
        check = False
        cicli = 0
        pos = []
        for i in range(len(arr)):
            pos.append(i)
        if num_insert == arr[len(arr)//2]:
            check = True
            cicli = 1
            pos[0] = pos[len(arr)//2]
        else:
            for i in range(len(arr)):
                div = len(arr)//2
                num = arr[div]
                if num == num_insert:
                    check = True
                    cicli = i+1
                    break
                elif len(arr) == 1:
                    break
                elif num_insert < num:
                    arr = arr[:div]
                    pos = pos[:div]
                elif num_insert > num:
                    arr = arr[div+1:]
                    pos = pos[div+1:]

        if check:
            print(f"\nNumero cicli = {str(cicli)}\nIl valore {str(num_insert)} è in posizione {str(pos[0])}")
        else:
            print("\nIl valore non è stato trovato")

def insert_array():
    choice = int(input("\nInserimento casuale(1) o manuale(2): "))
    length = int(input("\nInserire grandezza array: "))
    arr = []
    if choice == 1:
        for i in range(length):
            arr.append(random.randint(0, 50))
        return arr
    elif choice == 2:
        for i in range(length):
            var = int(input("Inserire valore posizione "+str(i)))
            arr.append(var)
        return arr
    else:
        print("\nScelta inesistente")

def print_array(arr):
    if len(arr) == 0:
        print("\nLa lista è vuota")
    else:
        for i in arr:
            print("[{}]".format(i),end=" ")

while True:
    print("""
    Inserire valore per scegliere opzione
    Opzione 1: Inserimento nell'array
    Opzione 2: Stampa dell'array
    Opzione 3: Ricerca valore nell'array
    Opzione 4: Ricerca valore nell'array 2
    Opzione 0: Esci dal programma
    """)
    choice = int(input("Inserire valore: "))
    if choice == 0:
        print("\n---Uscendo dal programma---")
        break
    elif choice == 1:
        arr = insert_array()
    elif choice == 2:
        print_array(arr)
    elif choice == 3:
        search_array(arr)
    elif choice == 4:
        arr.sort()
        print("\nArray in ordine di grandezza")
        print(arr)
        num = int(input("\nInserire valore da cercare: "))
        res = bin_search(arr, 0, len(arr)-1, num)
        if res != -1:
            print(f"\nIl valore {str(num)} è in posizione {str(res)}")
        else:
            print("\nIl valore non è stato trovato")
    elif choice == 5:
        bin_search1(arr)
    else:
        print("\nScelta inesistente")