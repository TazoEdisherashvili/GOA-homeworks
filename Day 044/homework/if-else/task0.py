# Write an if-else statement that prints "Good morning!" if the current hour is less than 12 and 
# "Good afternoon!" otherwise.

time = int(input("What time is it right now in 24-hour format: "))

if time < 12:
    print("Good morning!")  
elif time >= 12 and time <= 24:
    print("Good afternoon!")
else:
    print("Wrong input!")