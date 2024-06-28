# მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ კი დაბეჭდეთ ამ რიცხვამდე ყველა რიცხვი და მათ გვერდით მიუწერეთ ლუწია თუ კენტი.

number = int(input("Enter a number: "))

for num in range(number):
    if num % 2 == 0:
        print(str(num) + " is even.")
    else:
        print(str(num) + " is odd.")    