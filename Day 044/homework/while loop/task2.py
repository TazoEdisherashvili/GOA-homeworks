# Write a while loop that asks the user to guess a number between 1 and 10 until they get it right. The correct
# number is 7.

num = "7"
guess = input("Guess a number (from 1 to 10): ")
while guess != num:
    guess = input("Wrong number, try again: ")
print("Correct number")