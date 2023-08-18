symbol_value = {
    'A': 1, 'B': 5, 'Z': 10, 'L': 50, 'C': 100, 'D': 500, 'R': 1000,
    'AB' : 4, 'AZ' : 9, 'ZL' : 40, 'ZC' : 90, 'CD' : 400, 'CR' : 900
    }

s = ["AAA", "LBAAA", "RCRZCAB"]


def input_symbol(s):
    for text in s:
            print("input s:",text)
            convert_to_int(text)
    return

def convert_to_int(s):
    total = 0
    pre_value = 0
    explanation = []
    
    for symbol in s[::-1]:
        value = symbol_value[symbol]
        
        if value >= pre_value:
            total += value
            explanation.append(symbol)
            
        else:
            total -= value
            explanation[-1] = symbol + explanation[-1]
            
        pre_value = value
    explanation_str = ", ".join(explanation[::-1])
    print("output:",total)
    # print(explanation_str)
    explanation_list = explanation_str.split(", ")
    expanation_value(explanation_list)
    
    return total, explanation_str

def expanation_value(s):
    explanations_str = []

    for index in s:
        for index2 in symbol_value:
            value = symbol_value[index2]
            if index == index2:
                text = f"{index} = {value}"
                explanations_str.append(text)

    explanation_line = ", ".join(explanations_str)
    print(explanation_line)
    return explanation_line


input_symbol(s)