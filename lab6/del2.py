import timeit

class Song:

    def __init__(self, artistid, artistname, songtitle, songtime, year):
        self.artistid = artistid
        self.artistname = artistname
        self.songtitle = songtitle
        self.songtime = float(songtime)
        self.year = int(year)


    def __lt__(self,other):
        return self.songtime < other.songtime

def readTracks(amount):
    songList = list()
    with open("sang-artist-data.txt", "r", encoding = "utf-8") as songs:
        #count = 0
        for song in range(amount):
            data = song.split("\t")
            newSong = Song(data[0], data[1], data[2], data[3], data[4])
            songList.append(newSong)
           
    return songList

def getsongtime(songlist_user, alreadyfound, rank,counter):

     if counter < rank:

        counter += 1
        
        if len(songlist_user) != 0:
            longestsong = songlist_user[0]
            for i in range(len(songlist_user)):
                if longestsong < songlist_user[i]:
                    longestsong = songlist_user[i]

            alreadyfound.append(longestsong)
            songlist_user.remove(longestsong)
            getsongtime(songlist_user, alreadyfound, rank, counter)

            return alreadyfound[rank-1]
"""
def quicksort(data):
    last = len(data) - 1
    qsort(data, 0, last)

    return data

def qsort(data, low, high):
    pivotindex = (low + high)//2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]

    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low - 1, high, data[high])

    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]

    if pivotmid - low > 1:
        qsort(data, low, pivotmid - 1)
    if high - pivotmid > 1:
        qsort(data, pivotmid + 1, high)

    return data

def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h:
            break
    data[v], data[h] = data[h], data[v]
    return v
"""
def main2(): #NOTE: Jämför tiderna för att sortera alla element i filen med att köra linjär
                    #sökningen för några element. Upp till vilket antal element är linjär
                    #snabbare? Tiden det tar för att söka i sorterad lista är typ 0.

    amount = int(input("Hur många låtar vill du läsa in från filen?"))
    songlist_user = readTracks(amount)
    print(len(songlist_user))
    
    rank = int(input('Ange den position för vilken plats låten har i listan "längsta låt till kortaste"?'))
    alreadyfound = []
    songsearched = getsongtime(songlist_user, alreadyfound, rank, counter = 0)
    print("Title:",songsearched.songtitle,"\nSongDuration:",songsearched.songtime)
    #for w in range(1,rank):
        #i = w*10
        #print(i)
    time_linear = timeit.timeit(stmt=lambda: getsongtime(songlist_user, alreadyfound, rank, counter=0), number=1)
    print("Linjärsökningen tog", round(time_linear/1, 10), "sekunder")
    """    
    time_sort = timeit.timeit(stmt=lambda: quicksort(songlist_user), number=1)
    print('Sorteringen tog', round(time_sort/5, 10), 'sekunder')
    """


main2()