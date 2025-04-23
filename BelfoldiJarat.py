from Jarat import Jarat

class BelfoldiJarat(Jarat):
    def get_jegy_ara(self):
        # Belföldi járatok 10%-kal olcsóbbak
        return self.jegyar * 0.9
