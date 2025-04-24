# FTicketBSystem - Flight Ticket Booking System

A program elinditásáhz futtassa a main.py fájlt!

Ez a projekt egy egyszerű repülőjegy foglalási rendszert valósít meg python nyelven, ahol járatokra lehet jegyet foglalni, lemondani a foglalást, és megtekinteni az aktuális foglalások listáját.
A projekt célja az absztrakt osztály alkalmazása. Az absztrakt osztályok olyan osztályok, amelyek nem példányosíthatók közvetlenül, és egy vagy több absztrakt metódust tartalmaznak, amelyeket a leszármazott osztályokban kell implementálni.
A projektben kizárólag csak egyszerű szerkezeteket használunk, hiszen a projekt célja nem a hatékonyság, hanem a python alapvető működését bemutató feladat létrehozása, illetve egy alapvető felhasználóbarát kezelőfelület létrehozása CLI alatt.

Az adatok átteknthetőbb megjelenitése miatt javasolt a tabulate osztály telepitése, de nem kötelező. Hiánya a program használatában nem okoz gondot.

!!!!FONTOS!!!!
Jegy rendelése csak jövőbeni dátumra vonatkozóan lehetséges! Dátumot a program a gép saját órájából nyeri, amennyiben az pontatlan, hibák léphetnek fel a használat során!
Utazás, azaz jegy lemondása csak az utazás isőpontja előtt legfeljebb 1 nappal megelőzően lehetséges!
