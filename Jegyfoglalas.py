class JegyFoglalas:
    def __init__(self):
        # foglalasok: jaratszam -> list of utas_nevek
        self.foglalasok = {}

    def foglal(self, jaratszam, jarat, utas):
        """
        Hozzáad egy foglalást az adott járatra.
        Visszaadja a jegy árát.
        """
        self.foglalasok.setdefault(jaratszam, []).append(utas)
        return jarat.get_jegy_ara()

    def lemond(self, jaratszam, utas):
        """
        Lemond egy meglévő foglalást.
        Visszaad True ha sikerült, False ha nincs ilyen foglalás.
        """
        utasok = self.foglalasok.get(jaratszam, [])
        if utas in utasok:
            utasok.remove(utas)
            return True
        return False

    def listaz(self):
        """
        Visszaadja az összes foglalást [(jaratszam, utas), ...] formában.
        """
        eredmeny = []
        for jsz, utasok in self.foglalasok.items():
            for u in utasok:
                eredmeny.append((jsz, u))
        return eredmeny
