#  4) შექმენით კალკულატორის ფუნქცია რომელიც მომხმარებელს ეკითხება ორ რიცხვს და ასევე რა მათემატიკური 
# მოქმედება სურს რომ შესრულდეს, შემდეგ კი ასრულებს მომხმარებლის შემოტანილ რიცხვებზე იმ მოქმედებას რაც მან თქვა

def calculator():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    operation = input("Enter a operation: ")
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "//":
        print(num1 // num2)
    else:
        print("no such operation")
calculator()