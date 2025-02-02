"""
მომხმარებელს შეეკითხეთ მისი სახელი, გვარი, ასაკი, საცხოვრებელი, დაბადების წელი, სიმაღლე,
შემდეგ ეს ყველაფერი უნდა დაპრინტოთ ერთ გრძელ წინადადებაში მაგ: შენი
სახელი არის (სახელი), შენი გვარი არის(გვარი), თქვენი ასაკი არის(ასაკი) ... მინიშნება (უნდა გამოიყენოთ input() ფუნქცია)
"""

name = input("Enter your name: ") 
surname = input("Enter your surname: ")
age = input("Enter you age: ") 
address = input("Enter your address: ")
birth_year = input("Enter your birth year: ")
height = input("Enter your height: ")

print("Your name is", name + ", your surname is", surname + ", your age is", age + ", your address is", address + ", your birth year is", birth_year + ", your height is", height + ".")