from datetime import date, timedelta

class JegyFoglalas:
    def __init__(self):
        self.bookings = {}
        self.next_id = 1

    def book(self, airline, flight, travel_date, passenger):
        today = date.today()
        if travel_date < today:
            return None, None, "Kérjük, hogy jövőbeli dátumot adjon meg, időutazás még fejlesztés alatt, sajnos jelenleg nem elérhető!"
        fid = f"BKG{self.next_id:03d}"
        self.next_id += 1
        self.bookings[fid] = {
            'airline': airline,
            'flight_number': flight.jaratszam,
            'origin': flight.origin,
            'destination': flight.destination,
            'passenger': passenger,
            'travel_date': travel_date,
            'departure_time': flight.departure_time
        }
        return fid, flight.get_jegy_ara(), None

    def cancel(self, fid):
        info = self.bookings.get(fid)
        if not info:
            return False, "Nem található ilyen azonosító."
        if info['travel_date'] - date.today() <= timedelta(days=1):
            return False, "Lemondási határidő lejárt, két választása maradt. Utazik, vagy iszik egyet az egészségünkre."
        del self.bookings[fid]
        return True, None

    def list_bookings(self):
        return self.bookings
