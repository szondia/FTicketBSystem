class JegyFoglalas:
    def __init__(self):
        # foglalasok: id -> (jaratszam, utas)
        self.foglalasok = {}
        self.next_id = 1

    def foglal(self, jaratszam, jarat, utas):
        """
        Létrehoz egy új foglalást, visszaadja (foglalas_id, ar).
        """
        fid = f"BKG{self.next_id:03d}"
        self.next_id += 1
        self.foglalasok[fid] = (jaratszam, utas)
        return fid, jarat.get_jegy_ara()

    def lemond_by_id(self, fid):
        """
        Lemond foglalást azonosító alapján.
        """
        if fid in self.foglalasok:
            del self.foglalasok[fid]
            return True
        return False

    def lemond_by_name(self, nev):
        """
        Visszaadja a nevhez tartozó foglalások listáját: [(id, jaratszam)].
        """
        return [(fid, jsz) for fid, (jsz, u) in self.foglalasok.items() if u == nev]

    def listaz(self):
        """
        Visszaadja az összes foglalást: [(id, jaratszam, utas)].
        """
        return [(fid, jsz, u) for fid, (jsz, u) in self.foglalasok.items()]
