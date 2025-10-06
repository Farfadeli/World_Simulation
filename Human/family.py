from Human.couple import Couple
from Human.human import Human

class Family() : 
    def __init__(self, couple : Couple, children : list[Human]) :
        self.parent = couple
        self.children = children
    

    def add_children(self, child : Human) :
        self.children.append(child)
    
    def get_couple(self) -> Couple : return self.parent