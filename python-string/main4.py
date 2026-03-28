#Searching data can be done in python using the built-in functions like find() and index() to search for a specific substring within a string. For example, we can use the find() method to search for the substring 'World' in the string 'Hello, World!' and get its starting index.  
my_string = "Hello, World!" 
index = my_string.find("World")
print(index)  # Output: 7

#We can also use the index() method to search for the substring 'World' in the string 'Hello, World!' and get its starting index. The difference between find() and index() is that find() returns -1 if the substring is not found, while index() raises a ValueError.
try:
    index = my_string.index("World")
    print(index)  # Output: 7
except ValueError:
    print("Substring not found")  

#Endswith() and startswith() methods can also be used to check if a string ends with or starts with a specific substring. For example, we can use the endswith() method to check if the string 'Hello, World!' ends with the substring 'World!' and use the startswith() method to check if it starts with the substring 'Hello'.
print(my_string.endswith("World!"))  # Output: True
print(my_string.startswith("Hello"))  # Output: True  

#For more complex endswith() and startswith() checks in larger strings, without using regex, we can use the built-in functions like rfind() and rindex() to search for the last occurrence of a specific substring within a string. For example, we can use the rfind() method to search for the last occurrence of the substring 'o' in the string 'Hello, World!' and get its starting index.   
index = my_string.rfind("o")
print(index)  # Output: 8
try:
    index = my_string.rindex("o")
    print(index)  # Output: 8
except ValueError:
    print("Substring not found")  

    