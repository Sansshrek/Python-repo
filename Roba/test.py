import math

def separateFirstDegree(equ):
    split_equ = equ.split(',')
    a = b = 0
    if len(split_equ) == 2:
        n1 = split_equ[0]
        n2 = split_equ[1]
        pos = n1.find('x')
        if pos == 0 or n1[pos-1] == '+':  # +1 is implied
            a = 1
        elif n1[pos-1] == '-':  # -1 is implied
            a = -1
        else:
            a = int(n1[:pos])
        b = int(n2)
    elif len(split_equ) == 1:
        n1 = split_equ[0]
        pos = n1.find('x')
        if pos == 0 or n1[pos-1] == '+':  # +1 is implied
            a = 1
        elif n1[pos-1] == '-':  # -1 is implied
            a = -1
        else:
            a = int(n1[:pos])
    return a,b

def separateSecondDegree(equ):
    split_equ = equ.split(',')
    a = b = c = 0
    if len(split_equ) == 3:
        n1 = split_equ[0]  # x^2  a
        n2 = split_equ[1]  # x    b
        n3 = split_equ[2]  #      c
        pos = n1.find('x^2')
        if pos == 0 or n1[pos-1] == '+':  # +1 is implied
            a = 1
        elif n1[pos-1] == '-': # -1 is implied
            a = -1
        else:
            a = int(n1[:pos])
        pos = n2.find('x')
        if n2[pos-1] == '+':
            b = 1
        elif n2[pos-1] == '-':
            b = -1
        else:
            b = int(n2[:pos])
        c = int(n3)
    elif len(split_equ) == 2:
        n1 = split_equ[0]  # x^2  a
        pos = n1.find('x^2')
        if pos == 0 or n1[pos-1] == '+':  # +1 is implied
            a = 1
        elif n1[pos-1] == '-': # -1 is implied
            a = -1
        else:
            a = int(n1[:pos])
        if 'x' in split_equ[1]:
            n2 = split_equ[1]  # x  b
            pos = n2.find('x')
            if n2[pos-1] == '+':
                b = 1
            elif n2[pos-1] == '-':
                b = -1
            else:
                b = int(n2[:pos])
        else:
            c = int(split_equ[1])
    elif len(split_equ) == 1:
        a = int(split_equ[0])
    return a,b,c

#---

def firstDegree(equ):
    a,b = separateFirstDegree(equ)
    x = (-b)/a
    n = [x]
    return n

def secondDegree(equ):
    a,b,c = separateSecondDegree(equ)
    if checkDelta(a,b,c):
        x1,x2 = Equation(a,b,c)
        n = [x1,x2]
        return n
    else:
        print("\nCalcolo impossibile")
        return False

def checkDegree(equ):  # check equation degree
    if 'x^2' in equ:
        n = 2
    elif 'x' in equ:
        n = 1
    else:
        n = 0
    return n

def checkDelta(a,b,c):  # check if delta is less than 0
    check = False
    delta = (b*b)-(4*a*c)
    if delta>=0:
        check = True
    return check

def Equation(a,b,c):
    delta = (b*b)-(4*a*c)
    delta = math.sqrt(delta)
    n1 = (-b + delta)/(2*a)
    n2 = (-b - delta)/(2*a)
    return n1,n2

def solveEquation(equ):
    if checkDegree(equ)==1:
        return firstDegree(equ)
    elif checkDegree(equ)==2:
        return secondDegree(equ)

#---

def Dominio(x2):
    print("\nCalcolo dominio:")
    sol = solveEquation(x2)
    check = True
    if sol == False: # Impossibile
        check = False
    else:
        dominio = sol
        print("Valori del domino:")
        for i in range(len(dominio)):
            print("\nx diverso da: "+str(dominio[i]))
    return check

def Num(x1):
    print("\nCalcolo numeratore:")
    sol = solveEquation(x1)
    check = True
    if sol == False: # Impossibile
        print("Calcolo Impossibile")
    else:
        num = sol
        print("Valori del numeratore:")
        for i in range(len(num)):
            print("\n"+str(num[i]))

def Den(x2):
    print("\nCalcolo denominatore:")
    sol = solveEquation(x2)
    check = True
    if sol == False: # Impossibile
        print("Calcolo Impossibile")
    else:
        den = sol
        print("Valori del denominatore:")
        for i in range(len(den)):
            print("\n"+str(den[i]))

def rationalFunction(x1, x2):
    # inserire funzioni controllo impossibile
    if Dominio(x2) == True:  # se il dominio non è impossibile
        Num(x1)
        Den(x2)

#---

print("Questo programma non funziona con la radice quadrata e equazioni maggiori di 2° grado")
while True:
    print("\n\t0: uscita dal programma\n\t1: calcolo equazione\n\t2: calcolo equazione razionale fratta.")
    choice = int(input("Inserire valore per scegliere opzione: "))
    if choice == 0:
        break
    if choice == 1:
        print("\nNon usare spazi e usa la virgola per separare i valori\nEsempio di equazione: -x^2,+3x,-2")
        equ = input("Inserire equazione: ")
        sol = solveEquation(equ)
        if sol != False:
            if len(sol) == 1: # 1° grado
                print("Il valore dell'equazione è:\nx = "+str(sol[0]))
            else:             # 2° grado
                print("I valori dell'equazione sono:\nx1 = {} \nx2 = {}".format(sol[0],sol[1]))
    if choice == 2:
        print("\nNon usare spazi e usa la virgola per separare i valori\nEsempio di equazione: -x^2,+3x,-2")
        x1 = input("Inserire numeratore: ")
        x2 = input("Inserire il denominatore: ")
        rationalFunction(x1, x2)