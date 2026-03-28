#Numbers and Rounding in Python
#Built-in functions and Imported Functions can be used
import random
import math

#Measure distance
distance = 3.14159
print(distance)  # Output: 3.14159

#Absolute value
negative_number = -5
absolute_value = abs(negative_number)
print(absolute_value)  # Output: 5

#Rounding a number to a specific number of decimal places using the round() function. For example, we can round the distance variable to 2 decimal places.
rounded_distance = round(distance, 2)
print(rounded_distance)  # Output: 3.14 

#Math Ceiling and Floor, and Bankers rounding methods

#Ceiling rounds to the highest number
#Floor Methods rounds to the lowest number
#Bankers is rounding half to even (2.4 is 2.5 and thus is rounded to 3)

price = 34.66453452523
print(round(price))  # Output: 35
print(round(price, 2))  # Output: 34.67
print(math.ceil(price))  # Output: 35
print(math.floor(price))  # Output: 34
print(math.trunc(price)) # Output: 34


#Advanced math - revisit

#Randow numbers

print (random.random())

#Random numbers in a range
print(random.randint(1, 10))  

#Random numbers in a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

