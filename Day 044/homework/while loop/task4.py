# Write a while loop that repeatedly asks the user to enter a 
# password until the correct password "password123" is entered.

password = "password123"
guess = input("Enter a password: ")

while guess != password:
    guess = input("Wrong password, try again: ")
print("Password is correct")