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
