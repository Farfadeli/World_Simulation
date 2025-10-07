import random

CHANCE_BE_GAY = 25

class Human() :
    def __init__(self, name : str, health : str, sexuality : chr, birth_date : int) :
        """
            name -> Name of the Human
            health -> 16 bit string which is the equivalent of DNA and define pathologies
            sexuality -> 'H' for Man and 'F' for Femal
        """
        self.name = name
        self.health = health
        self.age = 0
        self.sexuality = sexuality
        self.in_couple = False
        self.birth_date = birth_date
        self.is_gay = random.random()*100 <= CHANCE_BE_GAY
    
    def past_year(self) -> None : self.age += 1
    def catch_disease(self) -> None :
        new_disease = random.randint(1,50) == 33
        if new_disease :
            for e in range(len(self.health)-1) :
                if self.health[e] == '0' :
                    if e != len(self.health) :
                        self.health = self.health[:e] + '1' + self.health[e+1:]
                    else :
                        self.health = self.health[:e] + '1'
                    break
                
    def make_in_couple(self) -> None: self.in_couple = True
    def make_single(self) -> None : self.in_couple = False
        
    def get_health(self) -> str : return self.health
    def get_name(self) -> str : return self.name
    def get_sexuality(self) -> chr : return self.sexuality
    def get_age(self) -> int : return self.age
    def get_in_couple(self) -> bool : return self.in_couple
    def get_birth_date(self) -> int : return self.birth_date
    
    def set_birth_date(self, new_birth_date : int) -> None : self.birth_date = new_birth_date




    