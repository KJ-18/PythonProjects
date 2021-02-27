from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False
e = 0
c = 0
p = 0
a = int(input("Enter the number of matches:"))
for x in range(a):
        while player == False:
            #set player to True
                player = input("Rock, Paper, Scissors? ")
                if player == computer:
                    print("Tie!")
                    e += 1
                elif player == "Rock":
                    if computer == "Paper":
                        print("You lose!", computer, "covers", player)
                        c += 1
                    else:
                        print("You win!", player, "smashes", computer)
                        p += 1
                elif player == "Paper":
                    if computer == "Scissors":
                        print("You lose!", computer, "cut", player)
                        c += 1
                    else:
                        print("You win!", player, "covers", computer)
                        p += 1
                elif player == "Scissors":
                    if computer == "Rock":
                        print("You lose...", computer, "smashes", player)
                        c += 1
                    else:
                        print("You win!", player, "cut", computer)
                        p += 1
                else:
                    print("That's not a valid play. Check your spelling!")
        #player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[randint(0,2)]
print("Total No. of matches:", a)
print("Computer Wins ", c, " times!!")
print("You Win ", p, " times!!")
print("And No of tied matches is ", e, "!")
