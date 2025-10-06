from Human.human import Human
from Human.human_tools import Human_tools
import random

class Couple() :
    def __init__(self, human_1 : Human, human_2 : Human) :
        self.human_1 = human_1
        self.human_2 = human_2

    def make_child(self):
        last_name = self.human_1.get_name().split(" ")[-1]
        first_name = Human_tools().make_first_name()
        
        final_name= first_name + " " + last_name
        
        sex = random.choice(['H', 'F'])
        
        return Human(final_name, self.calculate_child_health(), sex)
    

    def calculate_child_health(self) -> str :
        child_health = ""
        first_health = self.human_1.get_health()
        second_health = self.human_2.get_health()

        for nucleotide in range(len(first_health)) :
            if first_health[nucleotide] == '0' and second_health[nucleotide] == '0' :
                if random.randint(1,100) == 99 : child_health += '1' # Mutation génétique non controllé par les gènes des parents
                else : child_health += '0'
            elif first_health[nucleotide] == '1' and second_health[nucleotide] == '1' :
                if random.randint(1,4) == 4 : child_health += '1'
                else : child_health += '0'
            else :
                if random.randint(1,8) == 8 : child_health += '1'
                else : child_health += '0'
        
        return child_health

    
    def adopt_child(self) :
        pass