#!/usr/bin/python3
from random import randint 
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)] 
player = False
score = 0
cs=0
ps=0
while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
        score=score+1
        cs=score
        ps=score
        print("Your score is:",ps)
        print("The computer's score is:",cs)
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("Check your spelling!")
    player = False
    computer = t[randint(0,2)]