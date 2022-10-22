#!/usr/bin/env python3

import random
from secret import FLAG
import pyfiglet


result = pyfiglet.figlet_format("Game Of Chance")
print(result)
print()

name=input("What is your name: ")
try:
    seed=int(input("How old are you: "))
except:
    print("Bruh whot?")
    exit()

print()
print(f"Welcome! {name}")
print("Lets play a game!")
print()
score=0
random.seed(seed)

tries=0
while(tries<32):
    x=random.randint(0,255)
    print(f"Current score: {score}")
    if(x%2==0):
        print("""Options:
        1) Increment your score
        2) Exit
        > """,end="")
        try:
            option=int(input())
        except:
            print("Umm?!")
            exit()
        if(option==1):
            score+=1
        elif(option==2):
            print("Thanks for playing!")
            exit()
        else:
            print("Huh?!")
            exit()
    else:
        print("""Options:
        1) Decrement your score
        2) Exit
        >""",end="")
        try:
            option=int(input())
        except:
            print("Umm?!")
            exit()
        if(option==1):
            score-=1
        elif(option==2):
            print("Thanks for playing!")
            exit()
        else:
            print("Huh?!")
            exit()
    if(score>=32):
        print()
        print("Congratulations! You lucky AF boi")
        print(FLAG)
        exit()
    tries+=1
    
print()
print("Seems like you didn't make it")
print("Better luck next time")