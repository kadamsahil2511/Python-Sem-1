#Accept the market price from the user and calculate the net amount as (marked price- discount) to pay according to the criteria
markedprice=int(input("Enter the cost price of the bike : "))
if markedprice<=7000:
    print("The Price after discount is Rs.", 0.1*markedprice)
elif markedprice>7000 and markedprice<=10000:
    print("The Price after discount is Rs.", 0.15*markedprice) 
else :
    print("The Price after discount is Rs.", 0.20*markedprice)