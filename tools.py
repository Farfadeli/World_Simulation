import pandas as pd
from Human.human import Human

def transform_to_dataframe(population : list[Human]) -> pd.DataFrame :
    result = {"name" : [], "health" : [], "age" : [], "sexuality": []}
    for human in population:
        result["name"].append(human.get_name())
        result["health"].append(human.get_health())
        result["age"].append(human.get_age())
        result["sexuality"].append(human.get_sexuality())
    
    return pd.DataFrame(result)