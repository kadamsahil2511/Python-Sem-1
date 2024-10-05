#Write a progam to calculate the electricity bill 
unit=int(input("Enter the number of units : "))
if unit>0 and unit<=100 :
    print("The electricity bill is Rs. 0")
elif unit>100 and unit<=200:
    print("The electricity bill is Rs.", (unit-100)*5)
else :
    print("The elcectricity bill is Rs.", 500+((unit-200)*10))