def utskrift(lista):
    if len(lista) > 0:
        utskrift(lista[1:])
        print(lista[0])

from linkedQFile import LinkedQ
from bintreeFile import Bintree
import sys

class SolutionFound(Exception):
    pass

class Parentnode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
    def writechain(self, child):
        if child is not None:
            self.writechain(child.parent)
            print(child.word)

gamla = Bintree()

ordbok = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for row in svenskfil:
        ordet = row.strip()
        if ordet in ordbok:
            pass
        else:
            ordbok.put(ordet)               # i vårt fall skapar detta ett trebokstavsord per row då alla ord i textfilen består av 3 bokstäver. 

def makechildren(nod,slutord, q):
    for i in range(len(nod.word)):
        for char in "abcdefghijklmnopqrstuvwxyzåäö":
            if nod.word[i] == char:
                pass
            else:
                new_word = nod.word[:i] + char + nod.word[i+1:]
                if new_word in ordbok:
                    if new_word not in gamla:
                        if new_word == slutord:
                            barn = Parentnode(new_word, nod)
                            print("Det finns en väg nämnligen")
                            barn.writechain(barn)
                            raise SolutionFound
                        else:
                            barn = Parentnode(new_word, nod)
                            q.enqueue(barn)
                            gamla.put(new_word)
                    else:
                        break
                else:
                    pass


def main():
    try:
        startord=input("Vad är startordet?")
        slutord=input("Vad är slutordet?")
        q = LinkedQ()
        rot = Parentnode(startord)
        q.enqueue(rot)
        while not q.isEmpty():
            nod = q.dequeue()
            makechildren(nod, slutord, q)
    except SolutionFound:
        print()
    else:
        print("Det finns ingen väg till", slutord)

main()

