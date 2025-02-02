# მომხმარებელს შემოატანინეთ ორი რიცხვი შემდეგ კი შეადარეთ ისინი ერთმანეთს.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number"))

if num1 < num2:
    print(str(num1) + " is less than " + str(num2))
elif num1 > num2:
    print(str(num1) + " is greater than " + str(num2))
else:
    print(str(num1) + " is equal to " + str(num2))