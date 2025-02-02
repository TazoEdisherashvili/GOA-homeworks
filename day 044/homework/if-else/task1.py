# Write an if-else statement that checks if a number is even or odd. If the number is even, print "Even"; 
# otherwise, print "Odd."

num = int(input("Enter a number: "))
if num < 0:
    print("Wrong input!")
elif num % 2 == 0:
    print(str(num) + " is even")
else:
    print(str(num) + " is odd") 