from Legitarsasag import LegiTarsasag
from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat
from Jegyfoglalas import JegyFoglalas
from Formatter import Formatter

def main():
    tarsasag = LegiTarsasag("GDE Airlines")
    # Előre betöltött járatok
    tarsasag.hozzaad_jarat(BelfoldiJarat("B100", "Budapest", 15000))
    tarsasag.hozzaad_jarat(BelfoldiJarat("B200", "Debrecen", 12000))
    tarsasag.hozzaad_jarat(NemzetkoziJarat("N300", "London", 30000))
    tarsasag.hozzaad_jarat(NemzetkoziJarat("N400", "Jalta", 50000))

    foglalas_mgr = JegyFoglalas()
    # Előre foglalások
    foglalas_mgr.foglal("B100", tarsasag.find_jarat("B100"), "Szent Borbála")
    foglalas_mgr.foglal("N400", tarsasag.find_jarat("N400"), "Иосиф Виссарионович Сталин")
    foglalas_mgr.foglal("N400", tarsasag.find_jarat("N400"), "Sir Winston Leonard Spencer-Churchill")
    foglalas_mgr.foglal("N400", tarsasag.find_jarat("N400"), "Franklin Delano Roosevelt")
    foglalas_mgr.foglal("N300", tarsasag.find_jarat("N300"), "Ikarosz")
    foglalas_mgr.foglal("B200", tarsasag.find_jarat("B200"), "Jesus Christ")

    while True:
        print("\n--- GDE Airlines Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        choice = input("Válasszon menüpontot (1-4): ").strip()

        if choice == '1':
            print("\nElérhető járatok:")
            print(Formatter.format_jaratok(tarsasag.get_elerheto_jaratok()))
            jsz = input("Járatszám: ").strip()
            jarat = tarsasag.find_jarat(jsz)
            if not jarat:
                print("[HIBA] Érvénytelen járatszám.")
                continue
            nev = input("Utas neve: ").strip()
            fid, ar = foglalas_mgr.foglal(jsz, jarat, nev)
            print(f"Foglalás sikeres! Azonosító: {fid}, Jegy ára: {ar:.0f} Ft")

        elif choice == '2':
            print("\nLemondási mód:")
            print(" 1. Foglalási azonosító alapján")
            print(" 2. Név alapján")
            mode = input("Válasszon (1-2): ").strip()
            if mode == '1':
                fid = input("Foglalási azonosító: ").strip()
                if foglalas_mgr.lemond_by_id(fid):
                    print("Lemondás sikeres.")
                else:
                    print("[HIBA] Nem található ilyen azonosító.")
            elif mode == '2':
                nev = input("Utas neve: ").strip()
                lista = foglalas_mgr.lemond_by_name(nev)
                if not lista:
                    print("[HIBA] Nincs ilyen névhez foglalás.")
                elif len(lista) == 1:
                    fid, _ = lista[0]
                    foglalas_mgr.lemond_by_id(fid)
                    print(f"Lemondás sikeres (ID: {fid}).")
                else:
                    print("Több foglalás található, válasszon:")
                    for fid, jsz in lista:
                        print(f" - {fid}, Járat: {jsz}")
                    fid = input("Foglalási azonosító: ").strip()
                    if foglalas_mgr.lemond_by_id(fid):
                        print("Lemondás sikeres.")
                    else:
                        print("[HIBA] Nem található ilyen azonosító.")
            else:
                print("[HIBA] Érvénytelen választás.")

        elif choice == '3':
            foglalasok = foglalas_mgr.listaz()
            if not foglalasok:
                print("Nincs aktív foglalás.")
            else:
                print("\nAktuális foglalások:")
                print(Formatter.format_foglalasok(foglalasok))

        elif choice == '4':
            print("Kilépés...")
            break

        else:
            print("[HIBA] Érvénytelen választás. Próbáld újra.")

if __name__ == '__main__':
    main()
