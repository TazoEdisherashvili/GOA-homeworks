# გააკეთეთ პაროლის შესაყვანი ინფუთის დახმარებით

password = "455"
guess = input("Enter the password: ")

while guess != password:
    guess = input("Wrong password, try again: ")
print("Correct password")