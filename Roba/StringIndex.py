
string = str(input("Inserire la stringa: "))

print("|",end="")
for i in range(len(string)):
    print(str(i), end="|")
print()
print("|",end="")
for i in range(len(string)):
    if i<10:
        print(string[i], end="|")
    else:
        print(string[i], end=" |")