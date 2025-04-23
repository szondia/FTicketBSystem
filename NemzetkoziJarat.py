from Jarat import Jarat

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def get_jegy_ara(self):
        # Nemzetközi járatok 20%-kal drágábbak
        return self.jegyar * 1.2