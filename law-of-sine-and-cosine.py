import math


#law of cosine
def SSS():
    c = float(input("What is the length of the first side?"))
    b = float(input("What is the length of the second side?"))
    a = float(input("What is the length of the third side?"))
    cosA = float((b * b + c * c - a * a) / (2 * b * c))
    cosB = float((a * a + c * c - b * b) / (2 * a * c))
    cosC = float((a * a + b * b - c * c) / (2 * a * b))
    C = round(math.degrees(math.acos(cosC)), 2)
    B = round(math.degrees(math.acos(cosB)), 2)
    A = round(math.degrees(math.acos(cosA)), 2)
    if cosA <= 1 and cosB <= 1 and cosC <= 1:
        print("The angle opposite the first side = " + str(C))
        print("The angle opposite the second side = " + str(B))
        print("The angle opposite the third side = " + str(A))
    else:
        print("No such triangle exists")


#law of cosine
def SAS():
    C = float(input("What is the measure of the given angle?"))
    a = float(
        input(
            "What is the length of the side to the left of the given angle?"))
    b = float(
        input(
            "What is the length of the side to the right of the given angle?"))
    cosC = round(float(math.cos(math.radians(C))), 2)
    c_squared = (a * a + b * b - cosC * 2 * a * b)
    c = round(math.sqrt(c_squared), 2)
    cosA = (b * b + c * c - a * a) / (2 * b * c)
    cosB = (a * a + c * c - b * b) / (2 * a * c)
    A = round(math.degrees(math.acos(cosA)), 2)
    B = round(math.degrees(math.acos(cosB)), 2)
    if cosA <= 1 and cosB <= 1 and cosC <= 1:
        print("The length of the non included side = " + str(c))
        print("The angle opposite the side to the left of the given angle = " +
              str(A))
        print("The angle opposite the side to the right of the given angle = "
              + str(B))
    else:
        print("No such triangle exists")


#law of sine
def ASA():
    b = float(input("What is the length of the given side?"))
    A = float(
        input(
            "What is the measure of the angle to the left of the given side?"))
    C = float(
        input(
            "What is the measure of the angle to the right of the given side?")
    )
    sinA = round(float(math.sin(math.radians(A))), 2)
    sinC = round(float(math.sin(math.radians(C))), 2)
    B = round(float(180 - C - A), 2)
    sinB = round(float(math.sin(math.radians(B))), 2)
    a = round(b * sinA / sinB, 2)
    c = round(b * sinC / sinB, 2)
    if sinA <= 1 and sinB <= 1 and sinC <= 1:
        print("The non included angle = " + str(B))
        print("The side opposite the angle to the left of the given side = " +
              str(a))
        print("The side opposite the angle to the right of the given side = " +
              str(c))
    else:
        print("No such triangle exists")


#law of sine
def AAS():
    a = float(input("What is the length of the given side?"))
    A = float(
        input("What is the measure of the angle opposite the given side?"))
    C = float(input("What is the measure of the other given angle"))
    sinA = round(float(math.sin(math.radians(A))), 2)
    sinC = round(float(math.sin(math.radians(C))), 2)
    B = round(float(180 - C - A), 2)
    sinB = round(float(math.sin(math.radians(B))), 2)
    c = round(a * sinC / sinA, 2)
    b = round(a * sinB / sinA, 2)
    if sinA <= 1 and sinB <= 1 and sinC <= 1:
        print("The non included angle = " + str(B))
        print("The side opposite the non included angle = " + str(b))
        print("The side opposite the given angle = " + str(c))
    else:
        print("No such triangle exists")


#law of sine
def SSA():
    A = float(input("What is the measure of the given angle?"))
    c = float(
        input("What is the length of the side adjacent to the given angle?"))
    a = float(
        input("What is the length of the side opposite the given angle?"))
    sinA = round(float(math.sin(math.radians(A))), 2)
    altitude = float(sinA * c)
    if a > altitude and a < c and A < 90:  #ambiguous case
        sinC = c * sinA / a
        C = round(float(math.degrees(math.asin(sinC))), 2)
        C2 = round(float(180 - C), 2)
        B = round(float(180 - A - C), 2)
        sinB = round(float(math.sin(math.radians(B))), 2)
        B2 = round(float(180 - A - C2), 2)
        sinB2 = round(float(math.sin(math.radians(B2))), 2)
        b = round(a * sinB / sinA, 2)
        b2 = round(a * sinB2 / sinA, 2)
        print("The non included side = " + str(b) + " or " + str(b2))
        print("The angle opposite the side adjacent to the given angle = " +
              str(C) + " or " + str(C2))
        print("The angle opposite the non included side = " + str(B) + " or " +
              str(B2))
    else:  #not ambiguous, only one triangle
        sinC = c * sinA / a
        if sinC < 1:
            C = round(float(math.degrees(math.asin(sinC))), 2)
            B = float(180 - A - C)
            sinB = round(float(math.sin(math.radians(B))), 2)
            b = round(a * sinB / sinA, 2)
            print("The non inluded side = " + str(b))
            print("The angle opposite the side adjacent to the given angle = "
                  + str(C))
            print("The angle opposite the non included side = " + str(B))
        else:
            print("No such triangle exists")


#main program
print(
    "This program assumes a GENERAL TRIANGLE. In any problem, you are either given SAS, SSS, ASA, AAS, or SSA."
)
gameplay = True
while gameplay:
    valid = False
    valid_givens = ["SAS", "SSA", "AAS", "SSS", "ASA"]
    while not valid:
        prompt = input("What are you given?")
        if prompt in valid_givens:
            valid = True
        else:
            print(
                "Sorry. The givens are not sufficient to solve the triangle.")
            valid = False
    if prompt == "SSS":
        SSS()
    elif prompt == "SAS":
        SAS()
    elif prompt == "ASA":
        ASA()
    elif prompt == "AAS":
        AAS()
    elif prompt == "SSA":
        SSA()
