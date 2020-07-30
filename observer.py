from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
from singleton import *

class Subject(ABC):
    """
    Interfejs Subject z parametrem ABC (dziedziczenie do utworzenia klasy abstrakcyjnej), tworzy klasy abstrakcyjne
    do zarządzania subskrybującymi
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Metoda abstrakcyjna do dodawania subskrybujących
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Metoda abstrakcyjna do dodawania subskrybujących
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Powiadomienie wszystkich obserwujących
        """
        pass


class ConcreteSubject(Subject):
    """
    Klasa Subject zawiera w sobie znaczące stany, a subskrybujacy (obserwatorzy) zostana powiadomieni kiedy stany
    ulegną zmianie
    """

    _state: int = None
    """
    Stan wszystkich obserwatorów w formie zmiennej prywatnej
    """

    _observers: List[Observer] = []
    """
    Prywatna lista obserwatorów, którą można rozbudować na podziały grup itp
    """

    def attach(self, observer: Observer) -> None:       #Implementacja metody abstrakcyjnej attach z klasy Subject
        if Singleton.getInstance()==None:
            Singleton()
        else:
            pass
        Singleton.__add__(self)
        self._observers.append(observer)
        print("[O] Subject: Attached an observer.")

    def detach(self, observer: Observer) -> None:       #Implementacja metody abstrakcyjnej detach z klasy Subject
        Singleton.__rem__(self)
        self._observers.remove(observer)
        print("[O] Subject: Dettached an observer.")


    """
    Zarządzanie subskrybujacymi
    """

    def notify(self) -> None:
        """
        Wywołuje powiadomienie dla każdego subskrybującego
        """

        print("[O] Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def changeState(self) -> None:                  #Funkcja zmieniająca stan, która symuluje działąnie observerów
        print("\n[O] Subject: I'm gonna change my state and to achive it I'm gonna use pseudo-random function.")
        self._state = randrange(0, 10)

        print(f"[O] Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    Interfejs Observer
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Metoda abstrakcyjna update odpowiadajaca za uaktualnienie newslettera
        """
        pass


"""
Ponizej znajduja się dwie klasy obserwatoró, któe reagują na zmiany dokonane przez observery (+implementacja
interfejsu update
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


