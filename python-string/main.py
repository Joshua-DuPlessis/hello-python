#One of the main data types in Python is the string. A string is a sequence of characters enclosed in either single quotes (' ') or double quotes (" "). Strings can be used to store and manipulate text data.
#Triple quotes (''' ''' or """ """) can be used for multi-line strings or to include both single and double quotes without escaping them.   
#Strings can be concatenated using the + operator and repeated using the * operator.
#Strings also have many built-in methods that allow you to manipulate and format them in various ways. For example, you can use the .upper() method to convert a string to uppercase, the .lower() method to convert it to lowercase, and the .strip() method to remove leading and trailing whitespace. You can also use the .format() method or f-strings (formatted string literals) to insert variables into strings.    
#Here are some examples of string manipulation in Python:       

#String types
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
triple_quote_string = '''Hello, World!'''
print(single_quote_string)
print(double_quote_string)
print(triple_quote_string)  

#Str () is a built-in function that converts other data types to strings. This can be useful when you want to concatenate a string with a non-string variable.
number = 42
string_number = str(number)
print(string_number)  # Output: '42'  

#Another example of string manipulation is using the .format() method to insert variables into a string. This can be done by using curly braces {} as placeholders for the variables and then calling the .format() method on the string with the variables as arguments.
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: 'My name is Alice and I am 30 years old.'    