import random
import pandas as pd
import argparse
import tools
from Human.human import Human
from Human.couple import Couple
from Human.family import Family
from Human.human_tools import Human_tools
from Utils.calendar import Calendar

MAKE_CHILD_CHANCE = 8.63  # default percent 8.63
SEND_TO_ADOPTION_CHANCE = 0.18  # default percent 0.18


class World_simulation():
    def __init__(self, simulation_name : str, gap: int, limit: int):
        self.name = simulation_name
        self.calendar = Calendar()
        
        self.gap = gap
        self.limit = limit

        self.world_population: list[Human] = []
        self.adoption_list: list[Human] = []
        self.couple_list: list[Couple] = []
        self.family_list: list[Family] = []
        self.demography: int = 0

        self.years_list = []
        self.count_people_list = []

    def generate_default_population(self, number_humans: int):
        for _ in range(number_humans):
            self.world_population.append(
                Human(Human_tools().make_name(), '0000000000000000', random.choice(['H', 'F']), self.calendar))

        self.years_list.append(0)
        self.count_people_list.append(number_humans)

# ----------------------------------------------------------------------------------------------------------------------

    def launch(self):
        for _ in range(0, self.limit, self.gap):
            # principal loop of simulation, add one year of each humans
            self.human_loop()

            # Family loop of simulation
            self.family_loop()

            # calendar managing
            self.calendar.next_year()
            
            # Data to generate some charts
            self.years_list.append(self.years_list[-1]+1)
            self.count_people_list.append(self.get_population_number())

    def human_loop(self):
        for human in range(len(self.world_population)):
            self.world_population[human].past_year()
            self.world_population[human].catch_disease()

            if self.world_population[human].get_age() > 18:
                if human != len(self.world_population) - 1:
                    if self.world_population[human+1].get_age() > 18 and self.world_population[human].get_in_couple() == False and self.world_population[human+1].get_in_couple() == False:
                        can_be_in_couple = random.randint(1, 3) == 1
                        if can_be_in_couple:
                            new_couple = Couple(
                                self.world_population[human], self.world_population[human+1])
                            self.couple_list.append(new_couple)
                            self.family_list.append(Family(new_couple, []))
                            self.world_population
                            self.world_population[human].make_in_couple()
                            self.world_population[human+1].make_in_couple()

    def family_loop(self):
        for family in self.family_list:
            want_a_child = random.random()*100 <= MAKE_CHILD_CHANCE
            if want_a_child:

                if family.get_couple().get_is_gay() or family.get_couple().get_is_menopause():
                    child = family.get_couple().adopt_child(self.adoption_list)
                    if child == None:
                        continue
                    else:
                        family.add_children(child)
                else:
                    child = family.get_couple().make_child(self.calendar)

                    if random.random()*100 <= SEND_TO_ADOPTION_CHANCE:
                        self.adoption_list.append(child)
                    else:
                        family.add_children(child)
                    self.world_population.append(child)

# ----------------------------------------------------------------------------------------------------------------------

    def get_population_list(self) -> list[Human]: return self.world_population
    def get_population_number(self) -> int: return len(self.world_population)
    def get_adoption_list(self) -> list[Human]: return self.adoption_list
    def get_world_simulation_name(self) -> str : return self.name
    def get_couple_list(self) -> list[Couple] : return self.couple_list
    def get_female_population_number(self) -> int:
        count = 0
        for human in self.world_population:
            if human.get_sexuality() == 'F':
                count += 1
        return count

# ----------------------------------------------------------------------------------------------------------------------

    def save_simulation(self, excel_file_name: str) -> None:
        world_pop_df = tools.transform_to_dataframe(self.world_population)
        adoption_df = tools.transform_to_dataframe(self.adoption_list)

        with pd.ExcelWriter(excel_file_name) as writer:
            world_pop_df.to_excel(writer, sheet_name="Population", index=False)
            adoption_df.to_excel(writer, sheet_name="Adoption", index=False)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--name", type=str,
                        help="Set the world simulation name")
    parser.add_argument("-p", "--population", type=int,
                        help="Set default population in the world")
    parser.add_argument("-g", "--gap", type=int,
                        help="Set the gap (in year) between each iteration")
    parser.add_argument("-l", "--limit", type=int,
                        help="Set the limit (in year) of the simulation")

    args = parser.parse_args()

    if (args.population == None or args.gap == None or args.limit == None or args.name == None):
        exit(1)

    main_simulation = World_simulation(args.name, args.gap, args.limit)
    main_simulation.generate_default_population(args.population)

    main_simulation.launch()

    main_simulation.save_simulation(f"./Results/{args.name}.xlsx")
    tools.save_simulation_to_database(main_simulation)