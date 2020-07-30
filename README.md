# POLSKA WERSJA
# Używanie 3 typów wzorców projektowych w aplikacji  
## Opis projektu:  
Projekt przedstawiony przeze mnie jest pythonową koncepcją sklepu (ew. witryny internetowej), który jest otwarty tylko w wyznaczonych godzinach, przez co użytkownicy mogą zrobić zamówienia i/lub zapisać się do newslettera tylko w wyznaczonych godzinach. Projekt jest w pełni skalowalny i należy go traktować, jako ogólny zarys nakładania się wzorców projektowych, które potrafią ze sobą współgrać.  
  
## Instrukcja użytkowania:
Wszystkie operacje dla zwykłego użytkownika mają miejsce w pliku main.py.  
1.	Instalujemy środowisko Python 3.8 i wyżej  
2.	(opcjonalnie) Instalujemy środowisko PyCharm, które ułatwi kompilowanie projektu  
3.	Importujemy wszystkie pliki podane w „Opis poszczególnych plików”  
4.	W metodzie decoredObserver() tworzymy obiekt klasy ConcreteSubject(), który będzie naszą rzeczą do subskrypcji (np. newsletter). [Tych obiektów może być kilka]  
5.	Poprzez klasę ConcreteObserverX(), gdzie X to A lub B, tworzymy obiekt obserwatora, który będzie subskrybował dany przedmiot (obiekt) z punktu 4.  
a.	ConcreteObserverA():  sprawdza czy zmienna _state obiektu subject, która jest liczbą pseudolosową, jest mniejsza od 3. Jeśli tak, to obserwator dostaje powiadomienie, jeśli nie, to nie dostaje powiadomienia z danego stanu  
b.	ConcreteObserverB(): sprawdza czy zmienna _state obiektu subject, która jest liczbą pseudolosową, jest równa 0 lub większa od 1. Jeśli tak, to obserwator dostaje powiadomienie, jeśli nie, to nie dostaje powiadomienia z danego stanu  
6.	Używając metody attach(Observer) dodajemy obserwatora do danego przedmiotu (obiektu)  
7.	Używając metody changeState() możemy zasymulować zmiany stanów w przedmiocie, przez co wywołujemy metodę update() w klasach ConcreteObserverX()  
8.	Używając metody detach(Observer) możemy usunąć obserwatora z danego przedmiotu  
  
## Opis poszczególnych plików:
__main.py__ – główny plik programu zawierający udekorowany metodą runOnlyBetween(_from,_to) metodę decoredObserver()  
__dekorator.py__ – plik programu zawierający implementację metody runOnlyBetween(_from,_to) oraz implementację metody timeAtShop(string)  
__singleton.py__ – plik programu zawierający implementacje wzorca projektowego singleton (&#95;&#95;init&#95;&#95; jest konstruktorem) oraz dwie metody (&#95;&#95;add&#95;&#95;, &#95;&#95;rem&#95;&#95;), które manipulują ilością obserwatorów subskrybujących dany przedmiot (obiekt)  
__observer.py__ – plik zawiera 2 klasy abstrakcyjne (Subject, Observer) oraz ich implementacje  
  
## Diagram klas:  
![alt diagram klas](https://i.imgur.com/a3KmJ0M.png)
  
  ---
  
  
# ENGLISH VERSION
# Concept of using 3 types of design patterns in Python application
## Project description:  
  
## User's manual:  
  
## Project's files description:  
__main.py__ - main file contains decored method decoredObserver() by runOnlyBetween(_from,_to)  
__dekorator.py__ - file contains implementation of these methods: runOnlyBetween(_from,_to), timeAtShop(string)  
__singleton.py__ - file contains implementation of:  
a) methods: &#95;&#95;add&#95;&#95;, &#95;&#95;rem&#95;&#95;' [Add or remove user from object subscribe list]  
b) singleton design pattern    
__observer.py__ - file contains declaration and implementation of abstract classes: Subject and Observer  
  
## UML Class Diagram:  
![alt class diagram](https://i.imgur.com/a3KmJ0M.png)
