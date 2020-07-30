from datetime import datetime as dt

class Decorator:
    def runOnlyBetween(_from=7, _to=22):            #Deklaracja funkcji dekoratora
        def rDecorator(func):                       #Dekorator dekoruje funkcje pobraną jako func
            def wrapper():
                if _from <= dt.now().hour < _to:
                    Decorator.timeAtShop("\n")      #Wywołanie metody
                    func()                          #Wywołanie pozostałych czynności po dekorowaniu
                else:
                    Decorator.timeAtShop("\n")
                    print("[D] Shop is closed.\n[D] Open hours:\n[D] From:" + str(_from) + " To:" + str(_to))

            return wrapper

        return rDecorator

    def timeAtShop(string):
        print("[D] Today is: " + str(dt.now().date()))
        print("[D] Current time: " + str(dt.now().time()) + str(string))

#timeAtShop()