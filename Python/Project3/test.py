def romanToInt(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for char in s[::-1]:  # Reverse the string to simplify subtraction
        current_value = roman_dict[char]
        
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        
        prev_value = current_value
    
    return result

# Example usage:
roman_numeral = "VVX"
result = romanToInt(roman_numeral)
print(result)  # This should print 1994
