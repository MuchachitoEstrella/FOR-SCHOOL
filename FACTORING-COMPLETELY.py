# WHY AM I SCREAMING??? IDK THIS IS MATH ALGEBRA 1 LESSON 75 OF 160 Factoring Completely

# I'LL USE QUESTION 5 FROM ACTIVITY 1 AS AN EXAMPLE, I STILL HAVEN'T ANSWERED IT
# ACTIVITY: IDENTIFY WEATHER OR NOT EACH POLYNOMIAL IS A PERFECT SQUARE TRINOMIAL. FACTOR ALL PERFECT TRINOMIAL
# GUESTION: x^2+9x+9
# DECIDED ON MAKING PYTHON CODE BECAUSE I HATE FINDING SQUARE TRINOMIAL I'M NOT GOOD AT IT

import math

print("FILL IN VALUE FOR A, B MARKS: ax^2 sing1 ab sing2 b") # I'TS CONFUSING I'M SORRY

def getinfo():
    a = False
    b2 = False
    sing1 = False
    sing2 = False

    while a == False:
        try:
            a = float(input("VALUE OF a: "))        
        except:
            print("try again")

    while sing1 == False:
        sing1 = input("VALUE OF sing1 -, +: ")
        if sing1 != "+" and sing1 != "-":
            sing1 = False
            print("TRY AGAIN")

    while sing2 == False:
        sing2 = input("VALUE OF sing2 -, +: ")
        if sing2 != "+" and sing2 != "-":
            sing2 = False
            print("TRY AGAIN")

    while b2 == False:
        try:
            b2 = float(input("value of b^2: "))        
        except:
            print("TRY AGAIN")

    b = math.sqrt(b2)
    ab = 2 * (a * b)
    iscorrect = input(f"THE QUESTION IS {a}x {sing1} {ab} {sing2} {b2} correct [y]es, [n]o? ")

    if iscorrect == "n":
        awnser = "NOT PERFECT SQUARE TRINOMIAL"

    p1 = a * a - b2 #-8
    p2 = (a + b) * (a - b) # -8
    p3 = a * a + ab + b2
    p4 = pow(a + b, 2)
    difference = f"{p1} = {p2} FACTORED DIFFERENCE BETWEEN TWO SQUARES"
    perfect = f"{p3} = {p4} FACTORING PERFECT SQUARE TRINOMIALS"

    print(awnser)
    print(difference)
    print(perfect)

getinfo()

input("PRESS ENTER TO EXIT")



