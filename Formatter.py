try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False

class Formatter:
    @staticmethod
    def format_jaratok(jaratok):
        # limit up to 6 flights
        display = jaratok[:6]
        if HAS_TABULATE:
            rows = [[j.jaratszam, j.origin, j.destination,
                     f"{j.get_jegy_ara():.0f} Ft", j.departure_time.strftime('%H:%M')]
                    for j in display]
            return tabulate(rows, headers=["Járatszám","Honnan","Hova","Ár","Idő"])
        else:
            lines = [f"{j.jaratszam}: {j.origin} -> {j.destination} | Ár: {j.get_jegy_ara():.0f} Ft | Idő: {j.departure_time.strftime('%H:%M')}"
                     for j in display]
            return "\n".join(lines) + "\n!!!! Az adatok táblázatosan áttekinthetőbbek a 'tabulate' modullal, kérjük telepitse (pip install tabulate). !!!!"

    @staticmethod
    def format_foglalasok(foglalasok):
        if HAS_TABULATE:
            rows = [[fid, info['airline'], info['flight_number'],
                     info['origin'], info['destination'],
                     info['passenger'], info['travel_date'].isoformat(), info['departure_time'].strftime('%H:%M')]
                    for fid, info in foglalasok.items()]
            return tabulate(rows, headers=["ID","Légitársaság","Járat","Honnan","Hova","Utas","Dátum","Idő"])
        else:
            lines = [
                f"{fid}: {info['airline']} {info['flight_number']} {info['origin']}->{info['destination']} | Utas: {info['passenger']} | {info['travel_date']} {info['departure_time'].strftime('%H:%M')}"
                for fid, info in foglalasok.items()
            ]
            return "\n".join(lines) + "\n!!!! Az adatok táblázatosan áttekinthetőbbek a 'tabulate' modullal, kérjük telepitse (pip install tabulate). !!!!"
