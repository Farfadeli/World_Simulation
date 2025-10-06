import pandas as pd
import matplotlib.pyplot as plt
from Human.human import Human
from world_simulation import World_simulation

def transform_to_dataframe(population : list[Human]) -> pd.DataFrame :
    result = {"name" : [], "health" : [], "age" : [], "sexuality": []}
    for human in population:
        result["name"].append(human.get_name())
        result["health"].append(human.get_health())
        result["age"].append(human.get_age())
        result["sexuality"].append(human.get_sexuality())
    
    return pd.DataFrame(result)

def make_line_charts(data_x : list, data_y : list) -> None : 
    plt.plot(data_x, data_y)
    plt.show()


def make_sexuality_pie_chart(total_human : int, female_human : int) -> None :
    labels = ["Male", "Female"]
    sizes = [(total_human - female_human) , female_human]
    print(female_human)
    fig, ax = plt.subplots()
    ax.pie(sizes,labels=labels, autopct='%1.1f%%')

def display_human_list(human_list : list[Human]) -> None :
    print("-" * 68)
    print(f"| {'name':<20} | {'health':<20} | {'age':<5} | {'sexuality':<10} |")
    print("-" * 68)
    for human in human_list:
        print(f"| {human.get_name():<20} | {human.get_health():<20} | {human.get_age():<5} | {human.get_sexuality():<10} |")
        print("-" * 68)