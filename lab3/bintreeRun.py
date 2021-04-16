from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for row in svenskfil:
        ordet = row.strip()                # i vårt fall skapar detta ett trebokstavsord per row då alla ord i textfilen består av 3 bokstäver. 
        if ordet in svenska:
            print(ordet, end = " ")         #om ordet redan finns printas det
        else:
            svenska.put(ordet)             # om ordet inte redan finns adderas det till trädet
print("\n")

engelska = Bintree()
with open("engelska.txt", "r", encoding = "utf-8") as engelskfil:
    for row in engelskfil:
        row_strip = row.strip()
        row_word = row_strip.split()
        for word in row_word:
            if word in engelska:            #om ordet redan finns, gör inget
                pass
            else:
                engelska.put(word)          #om ordet inte finns i det engelska trädet läggs det till
                if word in svenska:         #om det även finns i det vsvenska trädet printas det
                    print(word, end = " ")
print("\n")
