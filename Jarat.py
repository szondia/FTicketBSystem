from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.elerheto = True  # A járat foglalható-e

    @abstractmethod
    def get_jegy_ara(self):
        """
        Visszaadja a jegy árát, típusonként módosítva.
        """
        pass