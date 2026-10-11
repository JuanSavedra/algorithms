def roman_to_integer(txt):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0

    for x in range(len(txt)):
        current = values[txt[x]]

        if x + 1 < len(txt) and current < values[txt[x + 1]]:
            total = total - current
        else:
            total = total + current

    return total

print(roman_to_integer("III"))      
print(roman_to_integer("LVIII"))    
print(roman_to_integer("MCMXCIV"))
