# ააწყვეთ ჯეირანის პროგრამა სადაც ორი მომხმარებელი ერთმანეთს ეთამაშება ჯეირანს

user_1 = input("el_1, el_2 or el_3: ")
user_2 = input("el_1, el_2 or el_3: ")
el_1 = "მაკრატელი"
el_2 = "ქვა"
el_3 = "ფურცელი"
if user_1 == el_1 and user_2 == el_2:
    print("user_2 won")
elif user_1 == el_1 and user_2 == el_3:
    print("user_1 won")
elif user_1 == el_1 and user_2 == el_1:
    print("Drav")
elif user_1 == el_2 and user_2 == el_2:
    print("Draw")
elif user_1 == el_2 and user_2 == el_3:
    print("user_2 won")
elif user_1 == el_2 and user_2 == el_1:
    print("user_1 won")
elif user_1 == el_3 and user_2 == el_2:
    print("user_1 won")
elif user_1 == el_3 and user_2 == el_3:
    print("Draw")
elif user_1 == el_3 and user_2 == el_1:
    print("user_2 won")
else:
    print("wrong input")