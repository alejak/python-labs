from array import array

class ArrayQ:

    def __init__(self):
        self.__list = array('i') #Skapar en tom lista som vill ha siffror

    def enqueue(self, arg): #Metod för att addera in värden i din lista
        self.__list.append(arg) #Placerar in argumeent längst bak i din lista, dvs i = (len(list)-1)

    def dequeue(self): #Motsats till ovanstående metod, plockar ut argument först i listan. i = valbart, detta fall 0
         pop_elem= self.__list.pop(0) #pop, tar utt ett värde vars index jag väljer.
         return pop_elem

    def isEmpty(self): #ffinns ett element i listan --> returnerar vi false. Dvs vi fortsätter köra if satsen
         if self.__list:
             return False
         else:
             return True
            
# kommer upp fungerar, ta bort efter första visning
q = ArrayQ()       # skapar en instans av klassen, ansätter objektet q till detta
q.enqueue(1)       # appendar värdet 1, dvs elementet vars värde = 1, längst bak i listan
q.enqueue(2)       # ovanstående, value =2
x = q.dequeue()    # Plockar ut index 0 från listan, ansätter x = detta.
y = q.dequeue()    # ovanstående, y = först i listan
if (x == 1 and y == 2):
     print("Fungerar")
else:
     print("Något är fel. 1 och 2 förväntades men vi fick", x, y)
