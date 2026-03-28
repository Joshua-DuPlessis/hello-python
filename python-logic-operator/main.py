#Logic and Operators

#Instead of just using straighty line flow, control flow allows python to perform multiple tasks at once.   

#Conditional Statements
#The if statement allows you to execute code only if a certain condition is true. If the condition is false, the code inside the else block is executed.  

x = 5
if x > 0:
  print("x is positive")
else:
  print("x is not positive")    

#The elif statement allows you to execute code only if a certain condition is false. If the condition is true, the code inside the elif block is executed.  

x = 5   
if x > 0:
  print("x is positive")
elif x < 0:
  print("x is negative")
else:
  print("x is zero")  


#Loops and Iteration
#Loops allow you to repeat a block of code multiple times. In Python, you can use the for loop and the while loop.  

for i in range(1, 6):
  print(i)

i = 1
while i <= 5:
  print(i)
  i += 1    

#Types for(for), while(while), break(break), continue(continue) 
  

#Break and Continue
#The break statement allows you to exit a loop early. The continue statement allows you to skip the current iteration of a loop and continue to the next iteration.   

for i in range(1, 6):
  if i == 3:
    break
  print(i)

for i in range(1, 6):
  if i == 3:
    continue
  print(i)


#Boolean expressions and building conditions

#Value can be true or false, and you can combine them using logical operators.  
#None is also different to false, or empty  
#Key functions may include bool(), any(), all()

#Comparison may be done through the operators: ==, !=, >, <, >=, <=   


email = str(input("Enter your email:"))
phone = str(input("Enter your phone number:"))
username = str(input("Enter your username:")) 

print(all([email, phone, username])) #vs all

#isinstance()
print(isinstance(email, str)  )