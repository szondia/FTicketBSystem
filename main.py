from datetime import date, time, timedelta
from Legitarsasag import LegiTarsasag
from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat
from Jegyfoglalas import JegyFoglalas
from Formatter import Formatter

def main():
    codes = [
        ('GDE', 'GDE Airlines'),
        ('WZZ', 'Wizz Air'),
        ('LH', 'Lufthansa'),
        ('BA', 'British Airways'),
        ('AF', 'Air France'),
        ('KL', 'KLM'),
        ('TK', 'Turkish Airlines'),
        ('EK', 'Emirates'),
        ('QR', 'Qatar Airways'),
        ('FR', 'Ryanair')
    ]
    airlines = {code: LegiTarsasag(code, name) for code, name in codes}

    belfoldi_cities = ['Debrecen', 'Szeged', 'Pécs', 'Győr']
    international_cities = ['London', 'Paris', 'New York', 'Jalta', 'Sydney', 'Dubai', 'Tokyo']
    today = date.today()

    # Dinamikus járatok generálása
    for i, (code, _) in enumerate(codes):
        dep_date = today + timedelta(days=i+1)
        dep_time = time(hour=8 + i % 12, minute=(i * 5) % 60)
        jaratszam = f"{code}{100+i}"
        if code in ['GDE', 'WZZ']:
            destination = belfoldi_cities[i % len(belfoldi_cities)]
            price = 8000 + i * 2000
            jarat = BelfoldiJarat(jaratszam, 'Budaörs', destination, price, dep_date, dep_time)
        else:
            destination = international_cities[i % len(international_cities)]
            price = 30000 + i * 5000
            jarat = NemzetkoziJarat(jaratszam, 'Budapest', destination, price, dep_date, dep_time)
        airlines[code].add_flight(jarat)

    presets = [
        ('GDE', 'GDE100', 'Szent Borbála', 1),
        ('BA', 'BA103', 'Иосиф Виссарионович Сталин', 7),
        ('BA', 'BA103', 'Sir Winston Leonard Spencer-Churchill', 7),
        ('BA', 'BA103', 'Franklin Delano Roosevelt', 7),
        ('AF', 'AF104', 'Ikarosz', 3),
        ('GDE', 'GDE100', 'Jesus Christ', 2)
    ]
    fog_mgr = JegyFoglalas()
    for code, flight_num, utas, offset in presets:
        al = airlines.get(code)
        flight = al.find_flight(flight_num) if al else None
        td_preset = today + timedelta(days=offset)
        if flight:
            fog_mgr.book(al.name, flight, td_preset, utas)

    while True:
        print("\n--- Foglalási Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        ch = input("Válasszon (1-4): ").strip()

        if ch == '1':
            try:
                y = int(input("Év (YYYY): "))
                m = int(input("Hó (MM): "))
                d = int(input("Nap (DD): "))
                td = date(y, m, d)
            except ValueError:
                print("[HIBA] Érvénytelen dátum.")
                continue
            if td < today:
                print("[HIBA] A megadott dátum a múltban van és az időutazás szolgáltatásunk jelenleg fejlesztés alatt van. Kérem adjon meg jövőbeni időpontot.")
                continue

            # Összes járat szűrése: origin != destination
            all_flights = []
            for al in airlines.values():
                for f in al.available_flights(td):
                    if f.origin != f.destination:
                        all_flights.append((al.name, f))
            if not all_flights:
                print("[HIBA] Nincsenek elérhető járatok erre a dátumra.")
                continue

            # limit max 6
            print("\nElérhető járatok:")
            display = all_flights[:6]
            # Csoportosítva légitársaságonként
            grouped = {}
            for name, f in display:
                grouped.setdefault(name, []).append(f)
            for name, fls in grouped.items():
                print(f"\n{name}:")
                print(Formatter.format_jaratok(fls))

            fn = input("Járatszám: ").strip()
            sel = next(((n, f) for n, f in all_flights if f.jaratszam == fn), None)
            if not sel:
                print("[HIBA] Nincs ilyen járat.")
                continue

            utas = input("Utas neve: ").strip()
            bid, price, err = fog_mgr.book(sel[0], sel[1], td, utas)
            if err:
                print(f"[HIBA] {err}")
            else:
                print(f"Foglalás sikeres! {sel[0]} {fn}, ID: {bid}, Ár: {price:.0f} Ft")

        elif ch == '2':
            bid = input("Foglalási ID: ").strip()
            ok, err = fog_mgr.cancel(bid)
            if err:
                print(f"[HIBA] {err}")
            else:
                print("Lemondás sikeres.")

        elif ch == '3':
            bookings = fog_mgr.list_bookings()
            if not bookings:
                print("Nincsenek foglalások.")
            else:
                print(Formatter.format_foglalasok(bookings))


        elif ch == '4':

            print("Kilépés...")

            break

        else:

            print("[HIBA] Érvénytelen választás.")


if __name__ == '__main__':
    main()
