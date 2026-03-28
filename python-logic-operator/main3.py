#Membership and Identity operators

is_logged_in = True
is_guest = False
is_banned = True
print(is_logged_in is not is_guest is not is_banned)

#Membership and Identity operators
is_logged_in = True
is_guest = False
is_banned = True
print(is_logged_in and is_guest or is_banned)  

#Search for a character
print("f" in "hello")

#Search for a number
print(1 not in [1,2,3])


#Identity operators help connect variables, ID and values from application layer to code layer
x = ['a' + 'b', 'c']
y = ['a' + 'b', 'c']
print(x is y) 
print (x==y)


#Make sure email exists, and is not empty

email = None

print(email is not None and email != "")