import timeit

class Song:
    def __init__(self, trackId, songId, artistName, song_titel):
        self.trackId = trackId
        self.songId = songId
        self.artistName = artistName
        self.song_titel = song_titel

    def __lt__(self, other):
        return self.trackId < other.trackId

def readfile(file_name):
    songList = []
    songDict = {}
    with open(file_name, encoding='utf-8') as data_set:
        for rawRow in data_set:
            row = rawRow.strip('\n').split('<SEP>')
            songObject = Song(row[0], row[1], row[2], row[3])
            songList.append(songObject)
            songDict[row[0]] = songObject
    return songList, songDict



'''
Tidskomplexitet O(n)aaaasdasdasds
asdasdas
'''
def linsok(list_, testArtist_): #geeksforgeeks.org/timeit-python-examples/
    found = False #https://stackoverflow.com/questions/43302810/linear-search-python
    position = 0
    n = len(list_)

    while position < n:
        if list_[position] == testArtist_:
            found = True
            break
        position = position + 1
    return found

'''
quicksort och dess hjälpfunktioner togs från föreläsning 7.
Tidskomplexitet på O(n log(n)) i bästa fallet och O(n^2) i värsta fallet
'''
def quicksort(data):
    last = len(data) - 1
    qsort(data, 0, last)

def qsort(data, low, high):
    pivotindex = (low+high)//2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]  
    
    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low-1, high, data[high]) 
    
    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]       
    
    if pivotmid-low > 1:
        qsort(data, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(data, pivotmid+1, high)

def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and pivot < data[h]:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h: 
            break
    data[v], data[h] = data[h], data[v]
    return v

'''
Tidskomplexitet O(log n)
'''
def binsok(song_list, artist):
    start = 0
    end = len(song_list) - 1
    
    while start <= end:
        middle_point = (start + end) // 2
        if artist < song_list[middle_point].artistName:
            end = middle_point - 1
        elif artist > song_list[middle_point].artistName:
            start = middle_point + 1
        else:
            return True


'''
Tidskomplexitet O(1)
'''
def dictsok(songDict, artist):
    resultat = songDict[artist]

def main():

    filename = "unique_tracks.txt"
    
    lista, dictionary = readfile(filename)
    n = len(lista)
    print("Antal element =", n)

    last = lista[n-1]
    testartist = last.trackId

    linearTime = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 1)
    print("Linjärsökningen tog", round(linearTime, 10) , "sekunder")

    sortTime = timeit.timeit(stmt = lambda: quicksort(lista), number = 1)
    print("Det tog", round(sortTime, 10), "att sortera listan med hjälp av quicksort")

    binTime = timeit.timeit(stmt = lambda: binsok(lista, testartist), number = 1)
    print("Binärsökningen tog", round(binTime, 10) , "sekunder")

    dictTime = timeit.timeit(stmt = lambda: dictsok(dictionary, testartist), number = 1)
    print("Uppslagning i dictionary tog", round(dictTime, 10) , "sekunder")

if __name__ == '__main__':
    main()