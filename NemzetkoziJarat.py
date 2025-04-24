from Jarat import Jarat

class NemzetkoziJarat(Jarat):
    def get_jegy_ara(self) -> float:
        return self.jegyar * 1.2
