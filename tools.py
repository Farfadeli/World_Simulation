import pandas as pd
import matplotlib.pyplot as plt
from Human.human import Human
from world_simulation import World_simulation
import mysql.connector


DB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="world_simulation"
)


def transform_to_dataframe(population: list[Human]) -> pd.DataFrame:
    result = {"name": [], "health": [], "age": [], "sexuality": []}
    for human in population:
        result["name"].append(human.get_name())
        result["health"].append(human.get_health())
        result["age"].append(human.get_age())
        result["sexuality"].append(human.get_sexuality())

    return pd.DataFrame(result)


def make_line_charts(data_x: list, data_y: list) -> None:
    plt.plot(data_x, data_y)
    plt.show()


def make_sexuality_pie_chart(total_human: int, female_human: int) -> None:
    labels = ["Male", "Female"]
    sizes = [(total_human - female_human), female_human]
    print(female_human)
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')


def display_human_list(human_list: list[Human]) -> None:
    print("-" * 68)
    print(f"| {'name':<20} | {'health':<20} | {'age':<5} | {'sexuality':<10} |")
    print("-" * 68)
    for human in human_list:
        print(f"| {human.get_name():<20} | {human.get_health():<20} | {human.get_age():<5} | {human.get_sexuality():<10} |")
        print("-" * 68)


def save_simulation_to_database(world_simulation: World_simulation):
    cursor = DB.cursor()

    # Création de la simulation dans la table simulation
    cursor.execute(
        f"INSERT INTO simulation(name) VALUES('{world_simulation.get_world_simulation_name()}')")
    DB.commit()

    # sauvegarde des statistiques global de la population
    # Récupération del'identifiant de la simulation
    cursor.reset()
    cursor.execute("SELECT id FROM simulation")
    res = cursor.fetchall()

    ID = max(res)[0]

    # Envoyer les données dans la table population
    cursor.reset()
    cursor.execute(f"""INSERT INTO population(simulation_id, human_number, female_number, male_number) VALUES(
                   {ID}, 
                   {world_simulation.get_population_number()},
                   {world_simulation.get_female_population_number()},
                   {world_simulation.get_population_number() - world_simulation.get_female_population_number()})""")
    DB.commit()
    
    print(f"✅ La Population de la simulation numéro {ID} a été sauvegardé")
    
    # Sauvegarde de chaque humain de la simulation
    cursor.reset()
    for human in world_simulation.get_population_list() :
        cursor.execute(f"""INSERT INTO humans(simulation_id, human_name, human_health, human_birth_date) VALUES(
            {ID},
            '{human.get_name()}',
            '{human.get_health()}',
            {human.get_birth_date()})""")
        
        DB.commit()
        
    print(f"✅ Les humains de la simulation numéro {ID} ont été sauvegardé")
    
    
    # Sauvegarde des couples
    cursor.reset()
    
    for couple in world_simulation.get_couple_list() :
        first_human = couple.get_first_human()
        second_human = couple.get_second_human()
        
        first_human_id = 0
        second_human_id = 0
        
        cursor.execute(f"SELECT human_id FROM humans WHERE human_name = '{first_human.get_name()}' and human_health = '{first_human.get_health()}' and human_birth_date = {first_human.get_birth_date()}")
        data = cursor.fetchall()
        for d in data : first_human_id = d[0]
        
        cursor.reset()  
        
        cursor.execute(f"SELECT human_id FROM humans WHERE human_name = '{second_human.get_name()}' and human_health = '{second_human.get_health()}' and human_birth_date = {second_human.get_birth_date()}")
        data = cursor.fetchall()
        for d in data : second_human_id = d[0]
        
        cursor.reset()
        
        
        

    cursor.close()
