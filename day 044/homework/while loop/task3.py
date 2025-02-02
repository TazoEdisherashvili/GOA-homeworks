# Write a while loop that processes a list of numbers, doubling each number, and prints the new list.

numbers = [1, 2, 33]
result = []

while len(result) != len(numbers):
    for num in numbers:
        result.append(num * 2)
print(result)