
def divide(string):
    char_list = [][]
    for character in string:
        if character in char_list:
            char_list[char_list.index(character)][+1]
        else:
            char_list.append(character, 0)
    print(char_list,sep="\n")

while True:
    string = input("\nInserire stringa: ")
    divide(string)