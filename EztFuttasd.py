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

    foglalas_manager = JegyFoglalas()

    while True:
        print("\n--- GDE Airlines Rendszer ---")
        print("Elérhető járatok:")
        for j in tarsasag.get_elerheto_jaratok():
            print(f" - {j.jaratszam}: {j.celallomas}, Ár: {j.get_jegy_ara():.0f} Ft")
        print("\n1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        choice = input("Válasszon menüpontot (1-4): ").strip()

        if choice == '1':
            jaratszam = input("Járatszám: ").strip()
            jarat = tarsasag.find_jarat(jaratszam)
            if not jarat:
                print("Érvénytelen járatszám.")
                continue
            if not jarat.elerheto:
                print("Ez a járat már nem elérhető.")
                continue
            utas = input("Utas neve: ").strip()
            ar, hiba = foglalas_manager.foglal(jaratszam, jarat, utas)
            if hiba:
                print(f"[HIBA] {hiba}")
            else:
                print(f"Foglalás sikeres! Jegy ára: {ar:.0f} Ft")

        elif choice == '2':
            jaratszam = input("Járatszám: ").strip()
            jarat = tarsasag.find_jarat(jaratszam)
            if not jarat:
                print("Érvénytelen járatszám.")
                continue
            utas = input("Utas neve: ").strip()
            siker, hiba = foglalas_manager.lemond(jaratszam, utas, jarat)
            if hiba:
                print(f"[HIBA] {hiba}")
            else:
                print("Lemondás sikeres.")

        elif choice == '3':
            lista = foglalas_manager.listaz()
            if not lista:
                print("Nincs aktív foglalás.")
            else:
                print("Aktuális foglalások:")
                for sor in lista:
                    print(f" - {sor}")

        elif choice == '4':
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás. Próbáld újra.")

if __name__ == '__main__':
    main()