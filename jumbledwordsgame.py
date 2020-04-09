# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:39:42 2020

@author: LAKSHMANA RAO

"""
import random
def choose():
    lists=['computer','competition','accomplishment','mathematics','engineering']
    word=random.choice(lists)
    return word
def pick(jumble):
    question=",".join(random.sample(jumble,len(jumble)))
    return  question
def tnku(p1,p2,pp1,pp2):
    print("thank you for playing")
    print("the points of ",p1,"are",pp1)
    print("the points of",p2,"are",pp2)
    if(pp1>pp2):
        print(p1,"won the game")
    elif(pp1<pp2):
        print(p2,"won the game")
    else:
        print("its a draw!!!!!!nice game guys!!!!!")
def play():
    p1=input("enter the name of player 1")
    p2=input("enter the name of player 2")
    pp1=0
    pp2=0
    turn=0
    while(1):
        if(turn%2==0):
            print("player 1 its your turn")
            jumble=choose()
            qn=pick(jumble)
            print(qn)
            n=input("enter your answer")
            if(n==jumble):
                print("hip hip hurray!!you r right")
                pp1=pp1+1
            else:
                print("your r wrong!!!better luck next time!!")
            print("your points:",pp1)
            ans=int(input("do you want to continu(0/1):"))
            if(ans==0):
                break
            
            
            
        else:
            print("player 2 its your turn")
            jumble=choose()
            qn=pick(jumble)
            print(qn)
            n=input("enter your answer")
            if(n==jumble):
                print("hip hip hurray!!you r right")
                pp2=pp2+1
            else:
                print("your r wrong!!!better luck next time!!")
            print("your points:",pp2)
            ans=int(input("do you want to continu(0/1):"))
            if(ans==0):
                break
            
        turn=turn+1
    
    tnku(p1,p2,pp1,pp2)        
            
            
            
play()
    
    