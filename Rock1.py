#!/usr/bin/python3
from random import randint    #importing random integer from random
t = ["Rock", "Paper", "Scissors"]    #choices
computer = t[randint(0,2)]    #gives random no. 0&2
player = False
while player == False:   #while command
    player = input("Rock, Paper, Scissors?")  #input command
    if player == computer:   #if condition
        print("Tie!")   #print command
    elif player == "Rock":   #if else condition
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
