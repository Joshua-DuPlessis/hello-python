name  = str(input("Enter you name:").upper())
if name != "JOSHUA" and name != "JOSH":
    print("Hello, " + name + "! You are not Joshua, but you are welcome here.")
else:
    print(f"Welcome back, {name}!")

age = int(input("Enter your age:"))
if age < 18:
    print("You are a minor. You may not have access to certain content.")
else:
    print(f"Hi, {name}! You are {age} years old. You have access to all content.")

phone = input("Enter your phone number:")
phone = phone.replace("", "-")
print("")


