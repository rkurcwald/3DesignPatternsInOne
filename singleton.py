class Singleton:
    __instance = None
    val=0
    @staticmethod
    def getInstance():                          #Zwracanie instancji singletona i/lub jego tworzenie
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __add__(self):                          #Dodawanie wartości +1 do zmiennej publicznej val, która oznacza
        Singleton.val=Singleton.val+1           #ilość subskrybentów (observerów)
        print("[S] (Att): Observers count " + str(Singleton.val))
    def __rem__(self):                          #Odejmowanie wartości 1 od zmiennej publicznej val
        Singleton.val =Singleton.val-1
        print("[S] (Dett): Observers count " + str(Singleton.val))


    def __init__(self):                         #Konstruktor klasy Singleton, ktory tworzy instancję singletona, lub
        if Singleton.__instance != None:        #Wyrzuca Exception
            raise Exception("This class is singleton")
        else:
            Singleton.__instance = self
