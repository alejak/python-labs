import timeit



class Track2:
    def __init__(self, artistid, artistnamn, sångtitel, låtlängd ,år):
        self.artistid = artistid
        self.år = år
        self.artistnamn = artistnamn
        self.sångtitel = sångtitel
        self.låtlängd = låtlängd
        self.år = år
    def __lt__(self,other):
        if self.låtlängd < other.låtlängd:
            return True
        else:
            return False

def specsök(lista, max):
    redan_hittad = []
    längsta = lista[0]
    for i in range (max+1):
        for track in lista:
            if längsta.låtlängd == track.låtlängd:
                if track not in redan_hittad:
                    längsta = track
                    redan_hittad.append(track)
                else:
                    pass
            elif längsta < track:
                if track not in redan_hittad:   
                    längsta = track
                    redan_hittad.append(track)
                else:
                    pass
            else:
                pass
        i += 1         
    print (längsta.sångtitel)

def main():
    #filename = "/info/tilda/unique_tracks.txt"
    #file_del2 = "/info/tilda/sang-artist-data.txt"

    max = int(input("Sorterade i fallande ordning efter längd, skriv det index som tillhör den låt du vill höra! (längsta låten har index 0)"))

    tracklist = []
    trackdict = {}
    with open("10data.txt", "r", encoding = "utf-8") as tracks:
        for row in tracks:
            track = row.strip()
            track = list(track.split("\t"))
            track = Track2(track[0] , track[1] , track[2] ,  track[3], track [4])
            if track in tracklist:
                pass
            else:
                tracklist.append(track)
    
    specsöktid = timeit.timeit(stmt = lambda : specsök(tracklist, max), number = 1000)
    print("Sökningen tog", round(specsöktid, 4), "sekunder med osorterad sökning")

main()