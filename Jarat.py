from abc import ABC, abstractmethod
from datetime import date, time

class Jarat(ABC):
    def __init__(self, jaratszam: str, origin: str, destination: str, jegyar: float,
                 departure_date: date, departure_time: time):
        self.jaratszam = jaratszam
        self.origin = origin
        self.destination = destination
        self.jegyar = jegyar
        self.departure_date = departure_date
        self.departure_time = departure_time

    @abstractmethod
    def get_jegy_ara(self) -> float:
        pass
