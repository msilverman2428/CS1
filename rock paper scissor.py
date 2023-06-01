#Maxine Silverman 
#Rock Paper Scissor 

import random 
answers = ['rock', 'paper', 'scissors']
print("pick your weapon: rock, paper, or scissors")
print("type 'stop' to end game")

while True :
    bot = random.choice(answers)
    player = input("rock, paper, scissors")

    if player == "stop":
        break

    if player == "rock" and bot == "scissors":
         print ("you win I choose scissors")
    elif player == "rock" and bot == "paper":
         print ("you loose I chose rock")
    elif player == "rock" and bot == "rock":
         print ("we tied I choose rock")


    if player == "scissors" and bot == "rock":
        print("you loose I choose rock")
    elif player == "scissor" and bot == "paper":
        print("you win I choose paper")
    elif player == "scissor" and bot == "scissor":
        print("tie I choose scissors")


    if player == "paper" and bot == "rock":
        print("you win I choose rock")
    elif player == "paper" and bot == "paper":
        print("tie I choose paper")
    elif player == "paper" and bot == "scissor":
        print("you loose I choose scissors")


    
      
