from garbage import Garbage


class PaperGarbage(Garbage):

    def __init__(self, name, is_squeezed=False):
        self.name = name
        self.is_squeezed = is_squeezed

    def squeeze(self):
        if self.is_squeezed != True:
            self.is_squeezed = True
        return self.is_squeezed
