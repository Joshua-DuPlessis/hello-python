#Basic Python Commands

#For Comments (# is used for comments)


# Print Statement
print("Hello, World!")  

#Python also has variables and data types
x = 5  # Integer
y = 3.14  # Float
name = "Alice"  # String    
is_student = True  # Boolean  
print(x, y, name, is_student) 

#For more dynamic data, we can use the input function to get user input
user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")  

#Once again, main data types include integers, floats, strings, and booleans. We can also use lists, tuples, and dictionaries to store collections of data.
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_dict = {"name": "Alice", "age": 30, "is_student": True}
print(my_list)
print(my_tuple)
print(my_dict)    

#We can pass 3 data types, no value or None, single value, or multiple values. We can also use the type() function to check the data type of a variable.
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(name))  # <class 'str'>
print(type(is_student))  # <class 'bool'>
print(type(my_list))  # <class 'list'>
print(type(my_tuple))  # <class 'tuple'>
print(type(my_dict))  # <class 'dict'>    

#Built-in functions like len() can be used to get the length of a list, tuple, or dictionary.
print(len(my_list))  # 5
print(len(my_tuple))  # 5
print(len(my_dict))  # 3    

#3rd party libraries like pandas can be used to work with data in a more efficient way. We can use pandas to read and manipulate data from CSV files, Excel files, and more.

#User-defined functions can be created using the def keyword. Functions can take parameters and return values.
def greet(name):
    return "Hello, " + name + "!"   
print(greet("Alice"))  # Hello, Alice!  

