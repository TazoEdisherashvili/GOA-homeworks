# დავალება: მომხმარებელს შემოატანინეთ 4 სხვადასხვა ტიპის მონაცემი (string,integer,float,boolean) 
# შემდეგ დაბეჭდეთ ეს შემოტანილი მონაცემები და მათი მონაცემთა ტიპები.

string_input = input("Enter a string: ")
integer_input = int(input("Enter an integer: "))
float_input = float(input("Enter a float: "))
boolean_input = bool(input("Enter a boolean (True/False): "))

print(string_input, type(string_input))
print(integer_input, type(integer_input))
print(float_input, type(float_input))
print(boolean_input, type(boolean_input))