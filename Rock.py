#!/usr/bin/python3
from random import randint 
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)] 
player = False
cs=0
ps=0
while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
        cs=cs+1
        ps=ps+1
        print("Your score is:",ps)
        print("The computer's score is:",cs)
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cs=cs+1
            print("Your score is:",ps)
            print("The computer's score is:",cs)
        else:
            print("You win!", player, "smashes", computer)
            ps=ps+1
            print("Your score is:",ps)
            print("The computer's score is:",cs)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cs=cs+1
            print("Your score is:",ps)
            print("The computer's score is:",cs)
        else:
            print("You win!", player, "covers", computer)
            ps=ps+1
            print("Your score is:",ps)
            print("The computer's score is:",cs)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cs=cs+1
            print("Your score is:",ps)
            print("The computer's score is:",cs)
        else:
            print("You win!", player, "cut", computer)
            ps=ps+1
            print("Your score is:",ps)
            print("The computer's score is:",cs)
    else:
        print("Check your spelling!")
    player = False
    computer = t[randint(0,2)]