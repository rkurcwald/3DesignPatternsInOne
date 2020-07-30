#sklep ktory dziala od godziny do godziny dekorator
#observator do sprawdzania newslettera
#singleton do liczenia aktualnie obserwujacych osob [implementacja w observerze]

from observer import *
from decorator import Decorator

@Decorator.runOnlyBetween(7, 23)        #Dekorator
def decoredObserver():
    subject = ConcreteSubject()         #Tworzenie obiektu subject

    observer_a = ConcreteObserverA()    #Tworzenie obiektu observer_a
    subject.attach(observer_a)          #Dodanie observer_a do listy

    observer_b = ConcreteObserverB()    #Tworzenie obiektu observer_a
    subject.attach(observer_b)          #Dodanie observer_a do listy


    subject.changeState()               #Zmiana stanu danego obiektu
    subject.changeState()               #Zmiana stanu danego obiektu

    subject.detach(observer_a)          #Usuniecie observera z listy

    subject.changeState()               #Zmiana stanu danego obiektu

if __name__ == "__main__":              
    decoredObserver()                   