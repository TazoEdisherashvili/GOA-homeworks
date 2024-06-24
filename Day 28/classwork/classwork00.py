"""
მომხმარებელს შემოატანინეთ ქულა 0-100, თუ ქულა იქნება 90ზე მეტი დაბეჭდოს რომ შენ შეგიძლია აიღო სერთიფიკატი,
თუ ქულა იქნება 70-ზე მეტი დაბეჭდოს რომ გააუმჯობესე, სხვა შემთხვევაში დაბეჭდოს რომ არის ძალიან ცუდი 
შედეგი და ის ვერ აიღებს სერთიფიკატს
"""

point = int(input("Enter Your point: "))
if point > 90:
    print("You can get your certificate")
elif point > 70: 
    print("Upgrade it!")            
else:
    print("Very bad result")