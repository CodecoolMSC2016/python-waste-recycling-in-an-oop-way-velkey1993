from garbage import Garbage


class PlasticGarbage(Garbage):

    def __init__(self, name, is_clean=False):
        self.name = name
        self.is_clean = is_clean

    def clean(self):
        pass
