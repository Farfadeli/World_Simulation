import random

class Human_tools():
    def __init__(self) : 
        pass

    def make_name(self) -> str :
        first_name = [
            "Emma", "Lucas", "Léa", "Hugo", "Chloé", "Nathan", "Manon", "Gabriel", "Camille", "Louis",
            "Inès", "Arthur", "Sarah", "Tom", "Jade", "Noah", "Lina", "Ethan", "Zoé", "Paul"
        ]

        last_name = [
            "Dubois", "Lefevre", "Moreau", "Laurent", "Simon", "Michel", "Leroy", "Garcia", "Roux", "David",
            "Bertrand", "Morel", "Fournier", "Girard", "Bonnet", "Dupont", "Lambert", "Fontaine", "Rousseau", "Vincent"
        ]
        
        return first_name[random.randint(0, len(first_name)-1)] + " " + last_name[random.randint(0, len(last_name)-1)]
    
    def make_first_name(self) -> str :
        first_name = [
            "Emma", "Lucas", "Léa", "Hugo", "Chloé", "Nathan", "Manon", "Gabriel", "Camille", "Louis",
            "Inès", "Arthur", "Sarah", "Tom", "Jade", "Noah", "Lina", "Ethan", "Zoé", "Paul"
        ]
        
        return first_name[random.randint(0, len(first_name)-1)]