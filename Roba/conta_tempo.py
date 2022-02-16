time_list = []

class time_info:
    year = month = day = hour = minute = second = total_sec = 0
    def print_values(self):
        print("Year = "+str(self.year))
        print("month = "+str(self.month))
        print("day = "+str(self.day))
        print("hour = "+str(self.hour))
        print("minute = "+str(self.minute))
        print("second = "+str(self.second))
        print("total_sec = "+str(self.total_sec))

def check_time(time):
    time_split = time.split(":")
    if len(time_split) > 5 or len(time_split) <= 0:
        print("\nInserire tempo corretto")
        return False
    else:
        return True
        
def add_time():
    print("\nPer il formato dell'ora separare ogni unita di misura del tempo da ':'\n\nPer esempio: 1 giorno, 3 ore, 26 min e 7 sec -> 1:3:26:7 (o anche 01:03:26:7)\n")
    scelta = input("\nScegliere se inserire tempo singolo (default) o multipli(1): ")
    num_time = 1
    if scelta == "1":
        num_time = int(input("\nInserire numero tempi: "))
    for i in range(num_time):
        time = input(f"\nInserire tempo {str(len(time_list)+1)} (o 0 per uscire):\n")
        if time != "0":
            check = check_time(time)
            if check:
                time_list.append(time)

def print_list():
    print()
    if(len(time_list)==0):
        print("La lista è vuota")
    else:
        for i in range(len(time_list)):
            print(f"{str(i+1)}) {time_list[i]}")

def divide_time(time_div):
    time_fin = [0]*6
    time_split = time_div.split(":")
    j = 5
    for i in range(len(time_split)):
        time_fin[j] = time_split[(len(time_split)-1)-i]
        j-=1
    return time_fin

def calculate_seconds():
    time_set = time_info()
    total_second = 0
    for time in time_list:
        time_fin = divide_time(time)
        time_set.second = int(time_fin[5])
        time_set.minute = int(time_fin[4]) * 60
        time_set.hour = int(time_fin[3]) * 3600
        time_set.day = int(time_fin[2]) * 86400
        time_set.month = int(time_fin[1]) * 2628002.88
        time_set.year = int(time_fin[0]) * 31536000
        time_set.total_sec = time_set.year + time_set.month + time_set.day + time_set.hour + time_set.minute + time_set.second
        print()
        time_set.print_values()
        total_second += time_set.total_sec
    print("\n\nTotal Seconds: "+str(total_second))

def calculate_time():
    time_final = time_set = time_info()
    for time in time_list:
        time_fin = divide_time(time)
        time_final.second += int(time_fin[5])
        while time_final.second >= 60:
            time_final.minute += 1
            time_final.second -= 60
        time_final.minute += int(time_fin[4])
        while time_final.minute >= 60:
            time_final.hour += 1
            time_final.minute -= 60
        time_final.hour += int(time_fin[3])
        while time_final.hour >= 24:
            time_final.day += 1
            time_final.hour -= 24
        time_final.day += int(time_fin[2])
        while time_final.day >= 30:
            time_final.month += 1
            time_final.day -= 30
        time_final.month += int(time_fin[1])
        while time_final.month >= 12:
            time_final.year += 1
            time_final.month -= 12
        time_final.year += int(time_fin[0])
    print("\n\nTotal time:")
    time_final.print_values()

def main():
    print("Questo programma funziona dal conteggio di anni fino a secondi")
    scelta = 1
    while scelta != 0:
        print("""
        \nInserire valore per scegliere opzione
        Opzione 1: Aggiungere tempo alla lista
        Opzione 2: Stampa lista tempi
        Opzione 3: Calcola lista tempi in secondi
        Opzione 4: Calcola lista tempi in stampa semplice (YY/MM/DD/hh/mm/ss)
        Opzione 5: Resetta lista
        Opzione 6: Elimina ultimo tempo
        Opzione 0: Esci dal programma
        """)
        scelta = input()
        if scelta == "0":
            print("\n---Uscendo dal programma---")
            break
        elif scelta == "1":
            add_time()
        elif scelta == "2":
            print_list()
        elif scelta == "3":
            calculate_seconds()
        elif scelta == "4":
            calculate_time()
        elif scelta == "5":
            time_list.clear()
        elif scelta == "6":
            time_list.pop()
        else:
            print("\nScelta inesistente")

main()