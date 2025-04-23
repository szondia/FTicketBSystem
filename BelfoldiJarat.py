from Jarat import Jarat

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def get_jegy_ara(self):
        # Belföldi járatok 10%-kal olcsóbbak
        return self.jegyar * 0.9