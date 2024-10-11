# Lottery
'''
Ques - Develop a game where user will enter a number and system will generate a number and it'll match both user wins but if it won't user loses user will get 3 chances to enter number between 1-10
Score will be first attempt score = 10
Score will be second attempt score = 7
Score will be third attempt score = 5
'''
import random
score=0
count=0
for i in range(4):
    a=input("Enter your lucky number between 1 & 10")
    if a==2 : #random.randrange(1,11):
        print("Congrats ! you've won 10 points ")
        count+=1
        if count==1:
            score+=10
        elif count==2:
            score+=7
        elif count==3:
            score+=5
    else :
        print("Try again")