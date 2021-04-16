from bintreeFile import Bintree

svenska = Bintree()
ordbok = []
gamla = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for row in svenskfil:
        ordet = row.strip()
        ordbok.append(ordet)               # i vårt fall skapar detta ett trebokstavsord per row då alla ord i textfilen består av 3 bokstäver. 

def makechildren(word):
    for i in range(len(word)):
        for char in "abcdefghijklmnopqrstuvwxyzåäö":
            if word[i] == char:
                pass
            else:
                new_word = word[:i] + char + word[i+1:]
                if new_word in ordbok:
                    if new_word not in gamla:
                        svenska.put(new_word)
                        gamla.put(new_word)
                        print(new_word)
                    else:
                        pass
                else:
                    pass

startord=input("Vad är startordet?")
slutord=input("Vad är slutordet?")
makechildren(startord)