from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:

    def __init__(self, color):
        self.color = color
        self.paper_content = []
        self.plastic_content = []
        self.house_waste_content = []

    def throw_out_garbage(self, garbage):
        if isinstance(garbage, PlasticGarbage):
            if garbage.is_clean:
                self.plastic_content.append(self)
            elif not garbage.is_clean:
                raise DustbinContentError
        elif isinstance(garbage, PaperGarbage):
            if garbage.is_squeezed:
                self.paper_content.append(self)
            elif not garbage.is_squeezed:
                raise DustbinContentError
        elif isinstance(garbage, Garbage):
            self.house_waste_content.append(self)
        elif not isinstance(garbage, Garbage):
            raise DustbinContentError

    def empty_contents(self):
        self.plastic_content = []
        self.paper_content = []
        self.house_waste_content = []
