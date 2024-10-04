# Write a program to convert a month name to a number of days
month=("january","march", "may", "july", "august", "october", "december")
month2="feburary"
data=input("Enter the name of them month : ").lower()
if data in month:
    print("The month has 31 days")
elif data == month2:
    print("The months has 28 days and 29 if it's a leap year ")
else :
    print("The month has 30 days")