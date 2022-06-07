#!/usr/bin/env python3

user = input("What is your name? ")


print(f"Hello {user}, do you believe in mathemagic? ")

random_no = input("Enter a 4 digit random number:")

if random_no.isalpha():
    print(f"{random_no} is not a number") 

elif int(random_no) == 0000:
    print(f"{random_no} is not a valid number")
    print("Please enter a valid 4 digit number greater than zero")

elif int(random_no) <= 999 :
    print(f"{random_no} is not a 4 digit number")
    print("Please enter a valid 4 digit number that doesn't start with zero")

elif int(random_no) > 9999:
    print(f"Your number has {len(random_no)} digits")
    print(f"{random_no} is not a valid four-digit number")
    
elif random_no.isnumeric():
    print("That is a valid number")
else:
    print(f"{random_no} is not a number") 
     


