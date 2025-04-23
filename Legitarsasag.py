class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def hozzaad_jarat(self, jarat):
        """Hozzáad egy járatot a légitársasághoz."""
        self.jaratok.append(jarat)

    def get_elerheto_jaratok(self):
        """Visszaadja az elérhető (még foglalható) járatok listáját."""
        return [j for j in self.jaratok if j.elerheto]

    def find_jarat(self, jaratszam):
        """Keres egy járatot a járatszám alapján."""
        return next((j for j in self.jaratok if j.jaratszam == jaratszam), None)