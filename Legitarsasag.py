from datetime import date

class LegiTarsasag:
    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name
        self.flights = []

    def add_flight(self, jarat):
        self.flights.append(jarat)

    def available_flights(self, travel_date: date):
        # flights are daily recurring
        if travel_date < date.today():
            return []
        return self.flights

    def find_flight(self, flight_number: str):
        return next((f for f in self.flights if f.jaratszam == flight_number), None)
