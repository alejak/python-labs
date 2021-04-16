
class Node:                                 # node-klass som definierar noden som ett värde och två pekare, left - right.
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Bintree:                              # klassen som skapar vårt binära sökträd
    def __init__(self):                     # vanlig init metod som returnerar värde
        self.root = None

    def put(self, new_value):               # metod som tar in ett värde. Finns ingen root skapas ett en med detta värde som rot mha Node-klassen.
        if self.root == None:
            self.root = Node(new_value)
        else:                               # om det rot existerar, anropas hjälpmetoden putta som jämför värden för att applicera nya noden på rätt plats.
            putta(self.root, new_value)     # dvs, om värdet är lägre, gå vänster, högre gå höger. bättre beskrivning återfinns efter respektive metod

    def __contains__(self, value):          # metod som "svarar" när objekt placeras in i en if-sats   
        return finns(self.root, value)      # contains får sitt värde genererat, returnerat? från finns-funktionen, finns fungerar så att om värdet finns, return true. omvänt

    def write(self):                        # write kallar likt put på en hjälpmetod, skriv som gör så att värden skrivs i inorder. dvs storleksordning.
        skriv(self.root)
        print("\n")

def putta(root, value):                     #putta är vår hjälpfunktion till put-metoden
    if value < root.value:                  #om värdet är mindre än roten, undersöker vi noden till vänster om roten
        if root.left == None:               #om denna nod är tom skapar vi en ny nod med det inmatade värdet
            root.left = Node(value)
        else:
            putta(root.left, value)         #om denna nod finns kör vi funktionen igen för med noden till vänster om roten som ny rot
    else:
        if root.right == None:              #om värdet är större än roten, undersöker vi noden till höger om roten
            root.right = Node(value)        #om denna nod är tom skapar vi en ny nod med det inmatade värdet
        else:
            putta(root.right, value)        #om denna nod finns kör vi funktionen igen för med noden till höger om roten som ny rot

def finns(x, value):
    if x == None:
        return False
    elif value == x.value:
        return True
    elif value < x.value:
        return finns(x.left, value)
    else:
        return finns(x.right, value)

def skriv(x):
    if x != None:
        skriv(x.left)
        print(x.value)
        skriv(x.right)
