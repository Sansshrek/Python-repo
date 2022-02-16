import string
from enigma.machine import EnigmaMachine

alphabet = list(string.ascii_lowercase)

def shift_r(num_s, lis=alphabet): #shift to the right a list by the number inserted
    chiper = lis[num_s:] + lis[:num_s]
    return chiper

def check_text(text, alph=alphabet): #check if the text has different character than the alphabets given
    check = False
    for let in text:
        if let not in alph:
            check = True
    return check

def get_chipertext(text, chiper, alph=alphabet): #return the chipertext by the chiper inserted
    text_list = [char for char in text]
    chipertext = []
    for i in range(len(text_list)):
        chip_index = alph.index(text_list[i])
        chipertext.append(chiper[chip_index])
    return chipertext

while True:
    print("""\nInserire valore per scegliere opzione
          Opzione 1: Cifrario shiftato
          Opzione 2: Cifrario numerico
          Opzione 3: Cifrario a Trasposizione
          Opzione 4: Macchina Enigma
          Opzione 5: Cifrario di Cesare
          Opzione 6: Cifrario di Atbash
          Opzione 7: Scacchiera di Polibio
          Opzione 8: Disco cifrante di Alberti
          Opzione 9: Cifrario di Vigenerè
          Opzione 0: Esci dal programma
          """)
    choice = input("\nInserire opzione: ")
    if choice == "0":
        break
    elif choice == "1": #Cifrario Alfabetico
        print("\nUn semplice cifrario che utilizza l'alfabeto spostato verso destra di un certo numero di lettere")
        shift_num = input("\nInserire numero di shift per cifrario: ")
        if shift_num.isnumeric():
            chiper = shift_r(int(shift_num))
            print("\nCifrario semplice:", end="")
            for let in alphabet:
                print(f" {let}", end="")
            print("\nCifrario shiftato:", end="")
            for let in chiper:
                print(f" {let}", end="")
            while True:
                text = input("\nInserire testo da cifrare (0 per uscire): ")
                chk_txt = check_text(text)
                if text == "0" or chk_txt:
                    break
                else:
                    chipertext = "".join(get_chipertext(text, chiper))
                    print(f"\nTesto normale: {text}")
                    print(f"Testo cifrato: {chipertext}")
                
    elif choice == "2": #Cifrario Numerico
        print("\nUn semplice cifrario che utilizza la posizione delle lettere nell'alfabeto")
        print("\nCifrario semplice:", end="")
        for i in range(len(alphabet)):
            if i < 10:
                print(f" {alphabet[i]}", end="")
            else:
                print(f"  {alphabet[i]}", end="")
        print("\nCifrario shiftato:", end="")
        for let in alphabet:
            index = alphabet.index(let)
            print(f" {index+1}", end="")
        while True:
            text = input("\nInserire testo da cifrare (0 per uscire): ")
            chk_txt = check_text(text)
            if text == "0" or chk_txt:
                break
            else:
                chiper = [str(i) for i in range(1,26)]
                chipertext = get_chipertext(text, chiper)
                print(f"\nTesto normale: {text}")
                print("Testo cifrato: "+"".join(chipertext))
                print("Testo cifrato separato: ",end="")
                for char in chipertext:
                    print(f"{char} ",end="")
                    
    elif choice == "3": #Cifrario a colonne
        print("\nUn cifrario che utilizza una chiave con al di sotto il messaggio chiario diviso in colonne per ogni carattere della chiave. Alla fine si riordina la chiave, con i rispettivi messaggi tagliati, in ordine alfabetico. Nel caso ci siano spazi vuoti restanti si inserisce il simbolo '*'")
        while True:
            text = input("\nInserire testo da cifrare (0 per uscire): ")
            if testo == "0":
                break
            else:
                key = input("\nInserire chiave: ")
                #inserimento valori nella tabella
                all_list = []
                for let in key:
                    col = {}
                    col["key"] = let
                    col["list"] = []
                    all_list.append(col)
                iter = 0
                key_iter = len(key)
                while key_iter < len(text):
                    key_iter *= 2
                char_left = key_iter-len(text)
                text += ("*"*char_left)
                for i in range(len(text)):
                    if i == len(key):
                        iter = 0
                    all_list[iter]["list"].append(text[i])
                    iter += 1
                    
                print("\nTabella non ordinata:")
                for obj in all_list:
                    print(f"{obj['key']} ", end="")
                print()
                print("--"*len(key))
                    
                row_iter = 0
                for i in range(len(all_list[0]['list'])):
                    for j in range(len(key)):
                        print(f"{all_list[j]['list'][row_iter]} ", end="")
                    print()
                    row_iter += 1
                    
                #ordinamento tabella
                all_list.sort(key=lambda x: x['key'])
                
                print("\nTabella ordinata:")
                for obj in all_list:
                    print(f"{obj['key']} ", end="")
                print()
                print("--"*len(key))
                    
                row_iter = 0
                for i in range(len(all_list[0]['list'])):
                    for j in range(len(key)):
                        print(f"{all_list[j]['list'][row_iter]} ", end="")
                    print()
                    row_iter += 1
                
                #create chipertext
                chipertext = ""
                for obj in all_list:
                    for char in obj['list']:
                        chipertext += char
                    chipertext += " "
                print(f"\nTesto Cifrato: {chipertext}")
    
    elif choice == "4": #Macchina Enigma
        machine = EnigmaMachine.from_key_sheet(
            rotors='II IV V',
            reflector='B',
            ring_settings=[1, 20, 11],
            plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')
        print(type(machine))
        print("""
              Rotori: II IV V
              Reflettore: B
              Impostazione anello: 1, 20, 11
              Collegamenti pannello di controllo: AV BS CG DL FU HZ IN KM OW RX""")
        display_1 = input("\nInserire primo display (3 lettere maiuscole) (es. WXC): ")
        machine.set_display(display_1)
        display_2 = input("\nInserire secondo display (3 lettere maiuscole) (es. KCH): ")
        msg_key = machine.process_text(display_2)
        print("\nSecondo display cifrato impostato: "+msg_key)
        machine.set_display(msg_key)
        while True:
            text = input("\nInserire testo da cifrare (0 per uscire): ")
            if text == "0":
                break
            else:
                chipertext = machine.process_text(text)
                print(f"\nTesto normale: {text}")
                print(f"Testo cifrato: {chipertext}")
            
    elif choice == "5": #Cifrario di Cesare
        print("\nIl cifrario di Cesare è un semplice cifrario che utilizza l'alfabeto spostato verso destra di 3 lettere")
        chiper = shift_r(int(3))
        print("\nCifrario semplice:", end="")
        for let in alphabet:
            print(f" {let}", end="")
        print("\nCifrario shiftato:", end="")
        for let in chiper:
            print(f" {let}", end="")
        while True:
            text = input("\nInserire testo da cifrare (0 per uscire): ")
            chk_txt = check_text(text)
            if text == "0" or chk_txt:
                break
            else:
                chipertext = "".join(get_chipertext(text, chiper))
                print(f"\nTesto normale: {text}")
                print(f"Testo cifrato: {chipertext}")
                
    elif choice == "6": #Cifrario di Atbash
        print("\nIl cifrario di Atbash è un cifrario che utilizza l'alfabeto invertito")
        chiper = alphabet[::-1]
        print("\nCifrario semplice:", end="")
        for let in alphabet:
            print(f" {let}", end="")
        print("\nCifrario shiftato:", end="")
        for let in chiper:
            print(f" {let}", end="")
        while True:
            text = input("\nInserire testo da cifrare (0 per uscire): ")
            chk_txt = check_text(text)
            if text == "0" or chk_txt:
                break
            else:
                chipertext = "".join(get_chipertext(text, chiper))
                print(f"\nTesto normale: {text}")
                print(f"Testo cifrato: {chipertext}")
    
    elif choice == "7": #Scacchiera di Polibio
        print("\nLa scacchiera di Polibio utilizza una sottospecie di scacchiera in cui si utilizzano le posizioni della colonna e della riga per indicare una lettera")
        print("Utilizzando l'alfabeto inglese bisogna per forza fondere 'k' e 'q' insieme")
        print("""
              #  1  2  3  4  5  
              1  a  b  c  d  e  
              2  f  g  h  i  j  
              3  kq l  m  n  o  
              4  p  r  s  t  u  
              5  v  w  x  y  z  """)
        chessboard = [["a", "b", "c", "d", "e"],
                      ["f", "g", "h", "i", "j"],
                      ["kq","l", "m", "n", "o"],
                      ["p", "r", "s", "t", "u"],
                      ["v", "w", "x", "y", "z"]]
        while True:
            text = input("\nInserire testo da cifrare (0 per uscire): ")
            chk_txt = check_text(text)
            if text == "0" or chk_txt:
                break
            else:
                text_list = [char for char in text]
                chipertext = []
                for let in text:
                    if let == "q" or let == "k":
                        chipertext.append("31")
                    else:
                        for i in range(5):
                            for j in range(5):
                                if chessboard[i][j] == let:
                                    chipertext.append(f"{i+1}{j+1}")
    
                print(f"\nTesto normale: {text}")
                print("Testo cifrato: "+"".join(chipertext))
                print("Testo cifrato separato: ",end="")
                for char in chipertext:
                    print(f"{char} ",end="")
    
    elif choice == "8": #Disco cifrante di Alberti
        print("\nIl disco cifrante di Alberti é un sistema che utilizza un disco fisso e un disco rotante per cifrare i messaggi")
        print("All'inizio del messaggio crittografato inseriamo in maiuscolo la lettera utilizzata come chiave del disco mobile")
        fix_disk = ["a", "b", "c", "d", "e", "f", "g", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "x", "z", "1", "2", "3", "4"]
        mob_disk = ["g", "k", "l", "n", "p", "r", "t", "v", "z", "&", "x", "y", "s", "o", "m", "q", "i", "h", "f", "d", "b", "a", "c", "e"]
        print("\n            Disco fisso: ", end="")
        for let in fix_disk:
            print(f" {let}", end="")
        print("\n      Disco mobile base: ", end="")
        for let in mob_disk:
            print(f" {let}", end="")
        key = input("\nInserire chiave del disco mobile: ")
        if key not in mob_disk:
            print("\nInserire una chiave valida")
        else:
            while mob_disk[0] != key:
                mob_disk = shift_r(1, mob_disk)
            print("\nDisco mobile modificato: ", end="")
            for let in mob_disk:
                print(f" {let}", end="")
            
            while True:
                text = input("\nInserire testo da cifrare (0 per uscire): ")
                chk_txt = check_text(text, fix_disk)
                if text == "0" or chk_txt:
                    print("\nInserire un testo con caratteri del disco fisso")
                    break
                else:
                    chipertext = "".join(get_chipertext(text, mob_disk, fix_disk))
                    print(f"\nTesto normale: {text}")
                    print(f"Testo cifrato: {chipertext}")
                    
    elif choice == "9": #Tabella di Vigenere
        print("\nIl cifrario di Vigenere è un cifrario che utilizza 26 alfabeti ordinati spostati di 1 a destra. Per cifare si andra a prendere, per ogni lettera del chiaro, l'incrocio tra la colonna della lettera chiara e la riga della lettera chiave detta 'verme'")
        table = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
                 ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A'],
                 ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B'],
                 ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C'],
                 ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D'],
                 ['F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E'],
                 ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F'],
                 ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
                 ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                 ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
                 ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                 ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
                 ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
                 ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'],
                 ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
                 ['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'],
                 ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
                 ['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'S'],
                 ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'],
                 ['T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'],
                 ['U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
                 ['V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
                 ['W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V'],
                 ['X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'],
                 ['Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
                 ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']]
        print("\nTabella di Vigenere:")
        for lis in table:
            for char in lis:
                print(f"{char} ", end="")
            print()
        while True:
            text = input("\nInserire testo da cifrare (0 per uscire): ")
            chk_txt = check_text(text)
            if text == "0" or chk_txt:
                print("\nInserire un testo con caratteri del disco fisso")
                break
            else:
                worm = input("Inserire verme(chiave): ")
                chk_txt = check_text(worm, list(string.ascii_uppercase))
                chipertext = ""
                if check_text(worm, [" "]):
                    worm += worm
                    worm = worm[:len(text)]
                for index in range(len(text)):
                    col = alphabet.index(text[index])
                    row = alphabet.index(worm[index])
                    chipertext += table[col][row]
                
                print(f"\nTesto normale: {text}")
                print(f"Testo chiave: {worm}")
                print(f"Testo cifrato: {chipertext}")
        
    else:
        print("\nScelta inesistente")
        
