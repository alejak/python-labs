from arrayQFile import ArrayQ

def main():
	order = [int(x) for x in input('Vilken ordning ligger korten i?').strip().split()] # listomfattning som gör om input till en lista av int, varav vi strippar " " och radbryten.
	card = ArrayQ()        # Ansätter en instans "card" av klassen ArrayQ.skapar lista utan element vars metoder kommer från klassen ArrayQ
	for i in order:
		card.enqueue(i) #går igenom listan order, ansätter alla värden i Card med mall från ArrayQ.
	result = []  # kan anses vara bordet.
	while not card.isEmpty():
		first_card = card.dequeue()  #plockar ur första kortet, 
		card.enqueue(first_card)      # placerar första kortet längst bak.
		next_card = card.dequeue()    # kort 2, plockas ut
		result.append(next_card)       # kort 2 läggs i resultatlistan dvs placereras ut på bordet.
	print (str(result).strip('[]'))  # printar result, från int --> str. strippar alla hakgrejjer, design.

if __name__ == '__main__':
	main()