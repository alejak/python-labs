import timeit
import sys
sys.setrecursionlimit(10000)
class Track:
    def __init__(self, id, latid, artist,titel):
        self.id = id
        self.latid = latid
        self.artist = artist
        self.titel = titel
    def __lt__(self, other):
            if self.artist < other.artist:
                return True
            else:
                return False
"""   
tracklist = []
trackdict = {}
with open("10tracks.txt", "r", encoding = "utf-8") as tracks:
    for row in tracks:
        track = row.strip()
        if track in tracklist:
            pass
        else:
            tracklist.append(track)
        if track in trackdict:
            pass
        else:
            track = list(track.split("<SEP>"))
            trackdict [track[2]] = track[0] , track[1] , track[3]

print(trackdict)
"""

def linsok(lista, testartist):
    for item in lista:
        if item.artist is testartist:
            break

def mergeSort(alist):      #denna sorteringsfunktion togs från http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def binärsök(lista, testartist):
    if len(lista) == 0:
        False
    else:
        mid = len(lista)//2
        if lista[mid].artist == testartist:
            return True
        else:
            if testartist < lista[mid].artist:
                return binärsök(lista[:mid], testartist)
            else:
                return binärsök(lista[mid+1:], testartist)


    
def main():
    #filename = "/info/tilda/unique_tracks.txt"
    #file_del2 = "/info/tilda/sang-artist-data.txt"

    tracklist = []
    trackdict = {}
    with open("unique_tracks.txt", "r", encoding = "utf-8") as tracks:
        for row in tracks:
            track = row.strip()
            track = list(track.split("<SEP>"))
            track = Track(track[0] , track[1] , track[2] ,  track[3])
            if track in tracklist:
                pass
            else:
                tracklist.append(track)
            if track in trackdict:
                pass
            else:
                trackdict[track.artist] = track.id , track.latid , track.titel
    
    antal_element = len(tracklist)
    print("Antal element =", antal_element)

    sista = tracklist[antal_element-1]
    testartist = sista.artist
    print (testartist)

    linjtid = timeit.timeit(stmt = lambda: linsok(tracklist, testartist), number = 10)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")
"""
    mergesorttid = timeit.timeit(stmt = lambda : mergeSort(tracklist), number = 10)
    print("Sorteringen med mergeSort tog", round(mergesorttid, 4), "sekunder")

    binärtid =timeit.timeit(stmt = lambda : binärsök(tracklist, testartist), number = 10)
    print("Binärsökningen tog", round(binärtid, 4), "sekunder")

    önskan = input("Vilken artist vill du slå upp?")
    slåupptid = timeit.timeit(stmt = lambda : trackdict[önskan] , number=10)
    print (trackdict[önskan])
    print ("Att slå upp denna artist  tog", round(slåupptid, 4), "sekunder")
    """
main()



        

    