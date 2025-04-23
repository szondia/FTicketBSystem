try:
    from tabulate import tabulate
    _HAS_TABULATE = True
except ImportError:
    _HAS_TABULATE = False

class Formatter:
    """
    Formázó osztály a foglalások és járatok megjelenítéséhez.
    Ha telepítve van a tabulate, táblázatként jeleníti meg az adatokat.
    Egyébként egyszerű felsorolást használ.
    """
    @staticmethod
    def format_foglalasok(foglalasok):
        # foglalasok: lista tuple (id, jaratszam, utas)
        if _HAS_TABULATE:
            rows = [[fid, jsz, u] for fid, jsz, u in foglalasok]
            return tabulate(rows, headers=["ID", "Járatszám", "Utas"])
        else:
            return "\n" + "\n".join(f" - ID: {fid}, Járat: {jsz}, Utas: {u}" for fid, jsz, u in foglalasok)

    @staticmethod
    def format_jaratok(jaratok):
        # jaratok: lista Jarat objektumok
        return "\n".join(f" - {j.jaratszam}: {j.celallomas}, Ár: {j.get_jegy_ara():.0f} Ft" for j in jaratok)
