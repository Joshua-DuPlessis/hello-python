#Operators can be grouped as follows:
#Arithmetic Operators #includes +, -, *, /, %, **, //
#Assignment Operators #includes =, +=, -=, *=, /=, %=, **=, //=
#Comparison Operators #includes ==, !=, >, <, >=, <=
#Logical Operators #includes and, or, not
#Identity Operators #includes is, is not
#Membership Operators #includes in, not in
#Bitwise Operators Includes &, |, ^, ~, <<, >>

#Arithmetic Operators #includes +, -, *, /, %, **, //
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7

#Assignment Operators #includes =, +=, -=, *=, /=, %=, **=, //=
x = 5
x += 2  # Equivalent to x = x + 2
print(x)  # Output: 7

#Comparison Operators #includes ==, !=, >, <, >=, <=
print(a == b)  # Output: False
print(a != b)  # Output: True


#Logical Operators #includes and, or, not
print(a > 5 and b < 5)  # Output: True
print(a > 5 or b > 5)  # Output: True

#Identity Operators #includes is, is not
c = a
print(a is c)  # Output: True
print(a is not b)  # Output: True


#Membership Operators #includes in, not in
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 not in my_list)  # Output: True


#Bitwise Operators Includes &, |, ^, ~, <<, >>
x = 5  # In binary: 0101
y = 3  # In binary: 0011
print(x & y)  # Output: 1 (In binary: 0001)
print(x | y)  # Output: 7 (In binary: 0111)
print(x ^ y)  # Output: 6 (In binary: 0110)
print(~x)  # Output: -6 (In binary: 1010)

#Chained comparison operators
a = 10
b = 20
c = 30

print(a < b < c)  # Output: True    

#Dynamic user inputs can be checked with chained comparison operators

John = int(input("Enter John's age: "))
Mary = int(input("Enter Mary's age: "))
Alice = int(input("Enter Alice's age: "))
#convert to if statement to determine "True" age arrangement
if John < Mary < Alice: print(John < Mary < Alice)
else: print(Alice < Mary < John)
elif: print(Mary < Alice < John)
