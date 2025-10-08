from Human.human import Human
from Human.human_tools import Human_tools
from Utils.calendar import Calendar
import random
import uuid

MENOPAUSE_AGE = 50


class Couple() :
    def __init__(self, human_1 : Human, human_2 : Human) :
        self.uuid = uuid.uuid4()
        
        self.human_1 = human_1
        self.human_2 = human_2
        self.is_gay = human_1.get_sexuality() == human_2.get_sexuality()
        self.is_menopause = (self.human_1.get_sexuality() == 'F' and self.human_1.get_age() > MENOPAUSE_AGE) or (self.human_2.get_sexuality() == 'F' and self.human_2.get_age() > MENOPAUSE_AGE)

    def make_child(self, birth_date : Calendar) :        
        last_name = self.human_1.get_name().split(" ")[-1]
        first_name = Human_tools().make_first_name()
        
        final_name= first_name + " " + last_name
        
        sex = random.choice(['H', 'F'])
        
        return Human(final_name, self.calculate_child_health(), sex, birth_date)
    

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

    
    def adopt_child(self, adoption_list : list[Human]) :
        if len(adoption_list) == 0 :
            return None
        else :
            child = adoption_list[0]
            del adoption_list[0]
            return child
    
    
    def get_is_gay(self) -> bool : return self.is_gay
    def get_is_menopause(self) -> bool : return self.is_menopause
    def get_first_human(self) -> Human : return self.human_1
    def get_second_human(self) -> Human : return self.human_2
    def get_uuid(self) -> str : return self.uuid