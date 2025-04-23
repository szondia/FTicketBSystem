try:
    from tabulate import tabulate
    tabulate_installed = True
except ImportError:
    tabulate_installed = False

from Legitarsasag import LegiTarsasag
from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat
from Jegyfoglalas import JegyFoglalas


def main():
    tarsasag = LegiTarsasag("GDE Airlines")

    # Előre betöltött járatok
    tarsasag.hozzaad_jarat(BelfoldiJarat("B100", "Budapest", 15000))
    tarsasag.hozzaad_jarat(BelfoldiJarat("B200", "Debrecen", 12000))
    tarsasag.hozzaad_jarat(NemzetkoziJarat("N300", "London", 30000))
    tarsasag.hozzaad_jarat(NemzetkoziJarat("N400", "New York", 50000))

    foglalas_mgr = JegyFoglalas()

    # Előre betöltött foglalások (6 példa)
    foglalas_mgr.foglal("B100", tarsasag.find_jarat("B100"), "Alice")
    foglalas_mgr.foglal("B100", tarsasag.find_jarat("B100"), "Bob")
    foglalas_mgr.foglal("B200", tarsasag.find_jarat("B200"), "Carol")
    foglalas_mgr.foglal("B200", tarsasag.find_jarat("B200"), "Dave")
    foglalas_mgr.foglal("N300", tarsasag.find_jarat("N300"), "Eve")
    foglalas_mgr.foglal("N300", tarsasag.find_jarat("N300"), "Frank")

    while True:
        print("\n--- GDE Airlines Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        choice = input("Válasszon menüpontot (1-4): ").strip()

        if choice == '1':
            # Foglalás: először listázzuk a járatokat
            print("\nElérhető járatok:")
            for j in tarsasag.get_elerheto_jaratok():
                print(f" - {j.jaratszam}: {j.celallomas}, Ár: {j.get_jegy_ara():.0f} Ft")
            jsz = input("Járatszám: ").strip()
            jarat = tarsasag.find_jarat(jsz)
            if not jarat:
                print("[HIBA] Érvénytelen járatszám.")
                continue
            nev = input("Utas neve: ").strip()
            ar = foglalas_mgr.foglal(jsz, jarat, nev)
            print(f"Foglalás sikeres! Jegy ára: {ar:.0f} Ft")

        elif choice == '2':
            # Lemondás: először listázzuk a járatokat
            print("\nElérhető járatok:")
            for j in tarsasag.get_elerheto_jaratok():
                print(f" - {j.jaratszam}: {j.celallomas}")
            jsz = input("Járatszám: ").strip()
            nev = input("Utas neve: ").strip()
            success = foglalas_mgr.lemond(jsz, nev)
            if success:
                print("Lemondás sikeres.")
            else:
                print("[HIBA] Nincs ilyen foglalás.")

        elif choice == '3':
            foglalasok = foglalas_mgr.listaz()
            if not foglalasok:
                print("Nincs aktív foglalás.")
            else:
                print("\nAktuális foglalások:")
                if tabulate_installed:
                    table = [[jsz, u] for jsz, u in foglalasok]
                    print(tabulate(table, headers=["Járatszám", "Utas"]))
                else:
                    for jsz, u in foglalasok:
                        print(f" - Járat {jsz}: {u}")

        elif choice == '4':
            print("Kilépés...")
            break

        else:
            print("[HIBA] Érvénytelen választás. Próbáld újra.")

if __name__ == '__main__':
    main()
