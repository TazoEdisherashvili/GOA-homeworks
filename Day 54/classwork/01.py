# შექმენით პროგრამა რომელშიც მომხმარებელს შემოატანინებთ 2 რიცხვს (input), 
# შემდეგ პირობითი განცხადებების საშვალებით (if-else) შეამოწმებთ რომელია უდიდესი, შემდეგ უმცირესიდან უდიდესამდე 
# for ციკლის გამოყენებით (for loop) დაბეჭდეთ ყველა 
# რიცხვი და თითეულს გვერდზე მიუწერეთ ლუწია თუ კენტი

user_1 = int(input("Enter the number: "))
user_2 = int(input("Enter the number: "))

if user_1 > user_2:
    print("user_1 is the highest")
    for i in range(user_2,user_1):
        print(i, i%2 == 0)
else:
    print("user_2 is the higheat")
    for i in range(user_1,user_2):
        print(i, i%2 == 0)