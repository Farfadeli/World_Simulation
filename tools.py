import pandas as pd
import matplotlib.pyplot as plt
from Human.human import Human
from world_simulation import World_simulation, MAKE_CHILD_CHANCE, SEND_TO_ADOPTION_CHANCE
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
        f"INSERT INTO simulation(name, fertility_rate, send_adoption_rate) VALUES('{world_simulation.get_world_simulation_name()}' , {MAKE_CHILD_CHANCE}, {SEND_TO_ADOPTION_CHANCE})")
    DB.commit()

    print(f"✅ La simulation a été créer")

    # Récupération de l'identifiant de la simulation
    cursor.execute('SELECT max(id) from simulation')
    data = cursor.fetchall()
    ID = data[0][0]

    # Stockage des humains
    sql_statement = "INSERT INTO human(uuid, simulation_id, name, health, sexuality, is_gay, in_couple, birth_date) VALUES "
    for human in world_simulation.get_population_list():
        sql_statement += f"('{human.get_human_id()}', {ID}, '{human.get_name()}', '{human.get_health()}', '{human.get_sexuality()}', {human.get_is_gay()}, {human.get_in_couple()}, STR_TO_DATE('{human.get_birth_date()}', '%d-%m-%Y')),"
    sql_statement = sql_statement[:-1]
    
    cursor.execute(sql_statement)
    DB.commit()
    
    print(f"✅ Les humains ont été ajouté à la simulation numéro {ID}")
    
    # Stockage des couples
    
    sql_statement = "INSERT INTO couple(uuid, first_human, second_human, simulation_id) VALUES"
    for couple in world_simulation.get_couple_list() :
        sql_statement += f"('{couple.get_uuid()}', '{couple.get_first_human().get_human_id()}' , '{couple.get_second_human().get_human_id()}', {ID}),"
    sql_statement = sql_statement[:-1]
    
    cursor.execute(sql_statement)
    DB.commit()
    
    print(f"✅ Les humains ont été ajouté à la simulation numéro {ID}")
        
    
    cursor.close()
