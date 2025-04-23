from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def get_jegy_ara(self):
        """
        Visszaadja a jegy árát járattípus szerint módosítva.
        """
        pass
