""" 
take a number from the user and then using a for loop output the sum of all the numbers up to this number 
(for example, if he enters 10, output the sum of all the numbers up to 10, for example).
"""
user_num = int(input("Enter a number: "))
sum = 0

for num in range(1, user_num + 1):
    sum += num
print(sum)