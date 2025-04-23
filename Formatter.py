try:
    from tabulate import tabulate
    _HAS_TABULATE = True
except ImportError:
    _HAS_TABULATE = False

class Formatter:
    """
    Formázó osztály a foglalások és járatok megjelenítéséhez.
    Ha telepítve van a tabulate, táblázatként jeleníti meg az adatokat.
    Egyébként egyszerű felsorolás + figyelmeztetés.
    """
    HAS_TABULATE = _HAS_TABULATE

    @staticmethod
    def format_foglalasok(foglalasok):
        # foglalasok: lista tuple (id, jaratszam, utas)
        if Formatter.HAS_TABULATE:
            rows = [[fid, jsz, u] for fid, jsz, u in foglalasok]
            return tabulate(rows, headers=["ID", "Járatszám", "Utas"])
        else:
            lines = [f"ID: {fid}, Járat: {jsz}, Utas: {u}" for fid, jsz, u in foglalasok]
            warning = (
                "Az adatok megjelenítése a tabulate osztály telepítésével áttekinthetőbb lenne. "
                "Kérjük telepítse!"
            )
            return "\n" + "\n".join(lines) + "\n" + warning

    @staticmethod
    def format_jaratok(jaratok):
        # jaratok: lista Jarat objektumok
        if Formatter.HAS_TABULATE:
            rows = [[j.jaratszam, j.celallomas, f"{j.get_jegy_ara():.0f} Ft"] for j in jaratok]
            return tabulate(rows, headers=["Járatszám", "Célállomás", "Ár"])
        else:
            lines = [f"{j.jaratszam}: {j.celallomas}, Ár: {j.get_jegy_ara():.0f} Ft" for j in jaratok]
            warning = (
                "Az adatok megjelenítése a tabulate osztály telepítésével áttekinthetőbb lenne. "
                "Kérjük telepítse!"
            )
            return "\n" + "\n".join(lines) + "\n" + warning
