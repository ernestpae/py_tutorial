# Function to calculate a to the power of b
# Takes two arguments, a and b, and returns a raised to the power of b
def exponent(a, b):
    return a ** b

# For example
print(exponent(10, 4))  # Output: 10000


# Function to convert a temperature from Fahrenheit to Celsius
# Takes a temperature in Fahrenheit and returns the temperature in Celsius
def convert_to_celsius(temp):
    temp_celsius = 5 / 9 * (temp - 32)
    return temp_celsius

'''For example'''
print(convert_to_celsius(98))  # Converts 98°F to Celsius


# Function to remove all characters 'c' and 'C' from a string
# Takes a string as input and returns a new string with all 'c' and 'C' characters removed
def no_c(my_string):
    result = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            result += i
    return result

'''Example Usage'''
print(no_c('Concentration'))  # Output: onentration


# Function to return a tuple with the length of a string and its first character
# Takes a sentence as input and returns (length of sentence, first character)
# If the sentence is empty, the first character is None
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])

# Example usage
print(multiple_returns("Hello"))  # Output: (5, 'H')
print(multiple_returns(""))       # Output: (0, None)




       