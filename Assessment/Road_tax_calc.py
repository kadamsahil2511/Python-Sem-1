# write a program to accept the cost price of a bike and display the raod tax to be paid according to the criteria
costprice=int(input("Enter the cost price of the bike : "))
if costprice<=50000:
    print("The Road Tax is Rs.", 0.05*costprice)
elif costprice>50000 and costprice<=100000:
    print("The Road Tax is Rs.", 0.1*costprice) 
else :
    print("The Road Tax is Rs.", 0.15*costprice)