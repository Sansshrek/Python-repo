import random
import time

def doors_check(switch):
    doors = ["c", "c", "c"]
    car_pos = random.randint(0, 2)
    doors[car_pos] = "m"
    usr_choice = random.randint(0, 2)
    #print(str(doors) + " " + str(usr_choice))
    if doors[usr_choice] == "m":
        if switch: # se voglio scambiare
            return False # perso poichè scambia con la capra
        else:
            return True #vinto poichè ho scelto macchina
    else:
        if switch:
            return True #vinto poichè ho scelto capra, l'altra capra sarà eliminata e rimane la macchina
        else:
            return False # perso poichè ho scelto la capra
    

n=50000
start_time = time.time()
tot = win = lose = 0
print("--NON SCAMBIANDO PORTA--\n")
for i in range(n):  # non scambio
    tot += 1 
    result = doors_check(False)
    if result:
        win += 1
    else:
        lose += 1
    print(f"Totale = {tot} | Vittorie = {win} | Perdite = {lose}",end="\x1b[1K\r")
print(f"Totale = {tot} | Vittorie = {win} | Perdite = {lose}")
percentage = (win*100)/tot
print(f"\nPercentuale vittorie = {percentage}%")
print("--- %s secondi Scambio porta ---" % (time.time() - start_time))
second_time = time.time()

tot = win = lose = 0
print("\n--SCAMBIANDO PORTA--")
for i in range(n):  # scambio
    tot += 1 
    result = doors_check(True)
    if result:
        win += 1
    else:
        lose += 1
    print(f"Totale = {tot} | Vittorie = {win} | Perdite = {lose}",end="\x1b[1K\r")
print(f"Totale = {tot} | Vittorie = {win} | Perdite = {lose}")
percentage = (win*100)/tot
print(f"\nPercentuale vittorie = {percentage}%")
print("--- %s secondi Scambio porta ---" % (time.time() - second_time))
print("\n--- %s secondi totali ---" % (time.time() - start_time))