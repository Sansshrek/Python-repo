#inserisco tre valori in input e ricevo in output le possibili combinazioni dei tre valori la cui somma non sia n

x = int(input("\nInserire primo valore: "))
y = int(input("\nInserire secondo valore: "))
z = int(input("\nInserire terzo valore: "))
n = int(input("\nInserire valore N: "))

print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n))