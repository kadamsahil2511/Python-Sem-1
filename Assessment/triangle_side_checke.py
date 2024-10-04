# write a program to check whether a triangle is isosceles or scalane
sides1 = float(input("Enter the side 1 of traiangle : "))
side2 = float(input("Enter the side 2 of traiangle : "))
side3 = float(input("Enter the side 3 of traiangle : "))

if sides1==side2==side3 :
    print("It is an equilateral triange")
elif sides1==side2 or side2==side3 or side3==sides1 :
    print("It is an isosceles triagnle")
else :
    print("It is a scalane triangle")
