class Pokemon:

	def __init__(self, name, hp, atk, deff, mass): #init operator, ansätter self.attribut = attribut
		self.name = name
		self.hp = hp
		self.atk = atk
		self.deff = deff
		self.mass = mass

	def __str__(self):  # str operator som returnerar information om vald pokemon i form av en sträng.
		pokeInfo = "Name: " + self.name + "\n" + "HP: " + str(self.hp) + "\n" + "Atk: " + str(self.atk) + "\n" + "Deff: " + str(self.deff) + "\n" + "mass: " + str(self.mass) + "\n"
		return pokeInfo

	def atkTrainer(self): # metod för att öka atk på vald pokemon
		self.atk = int(self.atk) + 5

	def deffTrainer(self): # /ovanstående fast deff.
		self.deff = int(self.deff) + 5

	def __lt__(self, other): # 
				if self.mass < other.mass:
					return True
				else:
					return False
class Gym:
	def __init__(self,gymList, gymName = "Brock GYM"):
		self.gymList = gymList
		self.gymName = gymName
	
	def __str__(self):
		return self.gymList

	def memberSearch(self, pokemonObject): #indata = pokemonObject. utdata blir då den pokemon vi söker efter eller felhantering längre ner
		found = True
		for pokemon in self.gymList:
			if pokemon.name == pokemonObject:
				found = True
				return found, pokemon
			else:
				found = False
		if not found:
			return found,None

	def changeGym(self):
		
		
		def ReadFile():#funktion som läser in pokemon filen, encodar med utf-8. och skapar en lista.
			fileName = "pokemon.csv"
			pokemonlist = [] #skapar en tom lista "pokemonlist"
			with open(fileName, encoding = "utf-8") as pokemonfile:
				firstLine = pokemonfile.readline()
				for row in pokemonfile:   #för varje rad i pokemonfilen
					category = row.strip().split(",") #skapar en lista "category" där elementen är attributen inom kommatecknen.
					pokemonName = category[2]
					pokemonHp = category[3]
					pokemonAtk = category[4]
					pokemonDeff = category[5]
					pokemonMass = category[16] #name till mass plockar ut de med valda index.
					pokemonObject = Pokemon(pokemonName, pokemonHp, pokemonAtk, pokemonDeff, pokemonMass) # skapar ett objekt med de angivna värdena som attribut.
					pokemonlist.append(pokemonObject) #Lägger in varje pokemon längst bak i den tomma listan vi skapade högst upp
			return pokemonlist

def menu(): #första interface, first user experience
	pokemonlist = ReadFile()
	gym = Gym(pokemonlist)
	while True:
		found = True   #ser till att vi inte skickas till "if" slingan under "else" ifall vi tar val 3 i submenu
		search = input("Search for a new pokemon in the gym: ").strip()
		found,pokemon = gym.memberSearch(search)
		if found:   #om pokemon från gymsearch funnen så printas denna ut map pokemonobjektets mallar.
			print()
			print(pokemon)
			Submenu(pokemon)
		else:
			print("Pokemon not found, try again.")

def Submenu(pokemon): #interface 2. vad vi ska göra med vår pokemon
	while True:	
		print("1. Increase Atk\n2. Increase Deff\n3. Check into SPA\n4. Choose a new pokemon\n5. End program")

		try:
			choice = int(input("What do you want to do: "))
			if choice == 1:
				pokemon.atkTrainer()
				print("\nNew Atk Lvl: " + str(pokemon.atk)+ "\n")
			elif choice == 2:
				pokemon.deffTrainer()
				print("\nNew Deff Lvl: " + str(pokemon.deff) + "\n")
			elif choice == 3:
				pokemon.spa()
			elif choice == 4:
				print() # Ligger som en break i while slinga, hoppas därmed ut om inget under sker. i detta fall exit. skickas till menu.
				break
			elif choice == 5:
				exit()
		except ValueError:
			print("\nChoose a number between 1-4.\n")
def hardCoded():
	a = [Pokemon("Charmander", 39, 52, 43, "8.5 kG")]
	return a
if __name__ == '__main__':
	#menu(hardCoded())
	menu()