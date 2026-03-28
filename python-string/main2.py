#Transformation can be done using the built-in functions or methods. The most common transformations are: 
#1. str() - converts a value to a string
#2. int() - converts a value to an integer
#3. float() - converts a value to a float
#4. bool() - converts a value to a boolean
#5. list() - converts a value to a list
#6. tuple() - converts a value to a tuple
#7. dict() - converts a value to a dictionary
#8. set() - converts a value to a set
#9. frozenset() - converts a value to a frozenset
#10. complex() - converts a value to a complex number
#11. ord() - converts a character to its Unicode code point
#12. chr() - converts a Unicode code point to a character
#13. hex() - converts an integer to a hexadecimal string
#14. oct() - converts an integer to an octal string
#15. bin() - converts an integer to a binary string


#f{} can be used to format strings in a more concise and readable way. It allows you to embed expressions inside string literals, using curly braces {} as placeholders for the expressions. The expressions are evaluated at runtime and their values are inserted into the string in place of the placeholders. For example:
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: 'My name is Alice and I am 30 years old.'

#We can also have fun with transforming 'ha' into 'hahahaha' using the * operator to repeat the string a certain number of times.
ha_string = "ha"
repeated_ha_string = ha_string * 4  
print(repeated_ha_string)  # Output: 'hahahaha'

#We can also use the .replace() method to replace a specific substring within a string with another substring. For example, we can replace 'ha' with 'ho' in the string 'hahahaha' to get 'hohohoho'.
original_string = "hahahaha"
replaced_string = original_string.replace("ha", "ho")
print(replaced_string)  # Output: 'hohohoho'    

#Another transformation function is the .split() method, which can be used to split a string into a list of substrings based on a specified delimiter. For example, we can split the string 'Hello, World!' into a list of words using the space character as the delimiter.
my_string = "Hello, World!"
split_string = my_string.split(" ")
print(split_string)  # Output: ['Hello,', 'World!']   

#Another transformation function is the .join() method, which can be used to join a list of strings into a single string using a specified delimiter. For example, we can join the list of words ['Hello,', 'World!'] into a single string using a space character as the delimiter.     
my_list = ['Hello,', 'World!']
joined_string = " ".join(my_list)
print(joined_string)  # Output: 'Hello, World!'   

#Transformation can also be done using the built-in functions like int(), float(), and bool() to convert strings to their respective data types. For example, we can convert the string '42' to an integer using the int() function, and the string '3.14' to a float using the float() function.
number_string = "42"
number = int(number_string)
print(number)  # Output: 42
float_string = "3.14"
float_number = float(float_string)
print(float_number)  # Output: 3.14
boolean_string = "True"
boolean_value = bool(boolean_string)
print(boolean_value)  # Output: True      

