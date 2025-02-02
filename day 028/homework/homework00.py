"""
დაწერე პროგრამა რომელიც მიიღებს ორ რიცხვს მომხმარებლისგან და დაპრინტავს 
პირველი რიცხვი მეორეზე მეტია, ნაკლები თუ მისი ტოლი
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is greater than second number")
elif num1 < num2:
    print("First number is less than second number")       
else:
    print("First number equals second number")