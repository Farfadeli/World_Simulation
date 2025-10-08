from Human.human import Human

def display_main_word(text : str) :
    result = ""
    if len(text) % 2 == 0 :
        result += ''.join(['-' for _ in range(150)]) + '\n|'
        calculate_space = int((148 - len(text)) / 2)
        result += ''.join([' ' for _ in range(calculate_space)])
        result += text
        result += ''.join([' ' for _ in range(calculate_space)]) + '|\n'
        result += ''.join(['-' for _ in range(150)])
    else :
        result += ''.join(['-' for _ in range(151)]) + '\n|'
        calculate_space = int((149 - len(text)) / 2)
        result += ''.join([' ' for _ in range(calculate_space)])
        result += text
        result += ''.join([' ' for _ in range(calculate_space)]) + '|\n'
        result += ''.join(['-' for _ in range(151)])
    print(result)



def display_human_list(human_list: list[Human]) -> bool:
    print("-" * 68)
    print(f"| {'name':<20} | {'health':<20} | {'age':<5} | {'sexuality':<10} |")
    print("-" * 68)
    for human in human_list:
        print(f"| {human.get_name():<20} | {human.get_health():<20} | {human.get_age():<5} | {human.get_sexuality():<10} |")
        print("-" * 68)
