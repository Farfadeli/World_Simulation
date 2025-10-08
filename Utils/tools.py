import pandas as pd
import matplotlib.pyplot as plt
from Human.human import Human
from world_simulation import World_simulation, MAKE_CHILD_CHANCE, SEND_TO_ADOPTION_CHANCE
import mysql.connector
from Utils.display import display_main_word


DB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)


def transform_to_dataframe(population: list[Human]) -> pd.DataFrame:
    result = {"name": [], "health": [], "age": [], "sexuality": []}
    for human in population:
        result["name"].append(human.get_name())
        result["health"].append(human.get_health())
        result["age"].append(human.get_age())
        result["sexuality"].append(human.get_sexuality())

    return pd.DataFrame(result)
def save_simulation(excel_file_name: str, main_world : World_simulation) -> None:
        world_pop_df = transform_to_dataframe(main_world.get_population_list())
        adoption_df = transform_to_dataframe(main_world.get_adoption_list())

        with pd.ExcelWriter(excel_file_name) as writer:
            world_pop_df.to_excel(writer, sheet_name="Population", index=False)
            adoption_df.to_excel(writer, sheet_name="Adoption", index=False)


def check_database_exist(cursor) -> None:
    cursor.execute("SHOW DATABASES LIKE %s" , ('world_simulation',))
    result = cursor.fetchone()
    
    if result : 
        return True
    else :
        print(f"⏳ Création de la base de données...")
        cursor.execute(f"CREATE DATABASE world_simulation DEFAULT CHARACTER SET 'utf8mb4'")
        print("🎉 Base de donnée 'world_simulation' créer avec succès")
        
        print('-----------------------------------------------------------------------------------------------------')
    return False       

def save_simulation_to_database(world_simulation: World_simulation):
    display_main_word("DATABASE")
    cursor = DB.cursor()
    
    database_aleready_exist = check_database_exist(cursor)
    
    cursor.execute("use world_simulation")

    if database_aleready_exist == False :
        sql_file = "./data/Database_init.sql"
        
        print("⏳ Création des tables dans la base de donnée 'world_simulation'")
        
        with open(sql_file, 'r', encoding='utf-8') as file :
            sql_script = file.read()
        
        for states in sql_script.split(";") :
            stmt = states.strip()
            if stmt : 
                cursor.execute(stmt)
        DB.commit()
        
        print("🎉 Les tables ont été créer avec succès")
        print('-----------------------------------------------------------------------------------------------------')
        
    
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
    if sql_statement[-1] != 'S' :
        sql_statement = sql_statement[:-1]
        cursor.execute(sql_statement)
        DB.commit()
    
        print(f"✅ Les couples ont été ajouté à la simulation numéro {ID}")
    else :
        print(f"✅ Il n'existe pas de couple dans la simulation numéro {ID}")
        
    
    cursor.close()
    DB.close()


