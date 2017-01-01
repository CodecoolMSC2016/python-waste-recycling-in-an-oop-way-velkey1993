from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:

    def __init__(self, color, paper_content, plastic_content, house_waste_content):
        self.color = color
        self.paper_content = paper_content
        self.plastic_content = plastic_content
        self.house_waste_content = house_waste_content

    def throw_out_garbage(self, garbage):
        if garbage is PlasticGarbage and garbage.is_clean:
            pass
        elif garbage.is_clean == False:
            pass
        if garbage is PaperGarbage and garbage.is_squeezed:
            pass
        elif garbage.is_squeezed == False:
            pass
        if garbage is Garbage and garbage is not PlasticGarbageand garbage is not PaperGarbage:
            pass
        if garbage not in Garbage:
            raise DustbinContentError
