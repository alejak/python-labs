class Node: # Node-klass
    def __init__(self, data, next_node = None):
        self.data = data              #ansätter ett värde till self.data = data
        self.next_node = next_node    # ovanstående, ansätts inte ett värde till next_node = ansätts värde None. t.ex. new = Node, se nedan

class LinkedQ: #Länkad köklass
    def __init__(self):
        self.__first = None # köplats = 1, dvs index 0
        self.__last = None # köplats = längstbak

    def enqueue(self, arg): # Hur vi placerar in värden i listan
        new = Node(arg) # Ett nytt nodobjekt med "arg" som värde.
        if self.__first == None: # Ifall kön är tom. då self.first -> new dvs nya noden. eftersom den är tom så är first och last samma.
            self.__first = new
            self.__last = new
        else:
            self.__last.next_node = new # likt append. ansätts längstbak med en pekare från den sista i kön
            self.__last = new # Sist i kön blir den nya noden

    def dequeue(self): # FIFO. först in först ut.
        arg = self.__first.data # skapar ett argument med den första i kön
        self.__first = self.__first.next_node # plockat ut första --> andra blir först
        return arg

    def isEmpty(self): # Kollar om listan innehåller element. är tom?
        if self.__first == None:
            return True
        else:
            return False
    
    def peek(self):
        if self.__first is not None:   
            return self.__first.data
        else:
            return None
