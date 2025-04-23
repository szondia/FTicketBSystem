class JegyFoglalas:
    def __init__(self):
        # foglalasok: jaratszam -> list of utas_nevek
        self.foglalasok = {}

    def foglal(self, jaratszam, jarat, felhasznalo):
        """
        Foglal egy járatra; ha sikeres, visszaadja az árat és None hibaüzenetet.
        Ha már foglalt, visszaad None-t és hibaszöveget.
        """
        if not jarat.elerheto:
            return None, "Ez a járat már foglalt."
        self.foglalasok.setdefault(jaratszam, []).append(felhasznalo)
        jarat.elerheto = False
        return jarat.get_jegy_ara(), None

    def lemond(self, jaratszam, felhasznalo, jarat):
        """
        Lemond egy korábbi foglalást; siker esetén (True, None), egyébként (False, hibaüzenet).
        """
        utasok = self.foglalasok.get(jaratszam, [])
        if felhasznalo in utasok:
            utasok.remove(felhasznalo)
            jarat.elerheto = True
            return True, None
        return False, "Nincs ilyen foglalás."

    def listaz(self):
        """Visszaadja az összes aktuális foglalást listaként."""
        lines = []
        for jsz, utasok in self.foglalasok.items():
            for u in utasok:
                lines.append(f"Járat {jsz}: {u}")
        return lines