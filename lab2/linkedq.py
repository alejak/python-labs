from linkedQFile import LinkedQ

def main():
	order = [int(x) for x in input('Vilken ordning ligger korten i?').strip().split()] # listomfattning som gör om input till en lista av int, varav vi strippar " " och radbryten.
	card = LinkedQ() #Ansätter en instans "card" av klassen LinkedQ.skapar lista utan element vars metoder kommer från klassen ArrayQ
	for i in order: #går igenom listan "order", ansätter alla värden med mall från LinkedQ.
		card.enqueue(i)
	result = []
	while not card.isEmpty(): # Här tar vi bort en och lägger den längst bak i kön, tar nästa i kön och sätter den i result listan, fortsätter tills listan är tom
		first_card = card.dequeue() # plockar ur första kortet ur listan
		card.enqueue(first_card) #placerar kortet längst bak
		next_card = card.dequeue() # plockar ur nästa kort
		result.append(next_card) # placerar det kortet i resultatlistan, dvs på "bordet"
	print (str(result).strip('[]')) # printar resultat, från int > str, strippar alla hakar

if __name__ == '__main__':
	main()
