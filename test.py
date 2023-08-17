#software test
#Thikamporn damban

def convert_to_int(s):
    symbol = {
        'A' : 1,
        'B' : 5,
        'Z' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'R' : 1000
    }
    value = 0
    pre_value = 0
    
    for i in s[::-1]:
        values = symbol[i]
        
        if values < pre_value:
            value -= values
            
        else:
            value += values
            
        pre_value = values
        
    return value


print(convert_to_int("AAA"))
print(convert_to_int("LBAAA"))
print(convert_to_int("RCRZCAB"))
 