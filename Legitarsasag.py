class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []  # lista Jarat objektumokkal

    def hozzaad_jarat(self, jarat):
        """Hozzáad egy járatot a légitársasághoz."""
        self.jaratok.append(jarat)

    def get_elerheto_jaratok(self):
        """Visszaadja az összes járatot."""
        return self.jaratok

    def find_jarat(self, jaratszam):
        """Keres egy járatot a járatszám alapján."""
        for j in self.jaratok:
            if j.jaratszam == jaratszam:
                return j
        return None
