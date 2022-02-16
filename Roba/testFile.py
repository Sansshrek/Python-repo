lista = []

with open('python\Python-repo\Roba\data.txt', 'r') as file:
    data = file.read().split('\n')
    print(data)
    char = data[0].split(" ")
    ch1 = char[0]
    ch2 = char[1]
    ch3 = char[2]
    ch4 = char[3]
    ch5 = char[4]
    ch6 = char[5]      
    print(f"{ch1} {ch2} {ch3} {ch4} {ch5} {ch6}")
    cont = data[1]
    print(cont)
    for i in range(2, len(data)):
        lista.append(data[i])
        
print(lista)
lines = []
with open('python\Python-repo\Roba\data.txt', 'r') as filer:
    data = filer.read().split('\n')
    data[1] = "57"
    data.append("gianlu")
    with open('python\Python-repo\Roba\data.txt', 'w') as filew:
        for line in data:
            filew.write(line)
            filew.write("\n")