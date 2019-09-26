# Write a Python program to make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

while True:
    choice = 1
    while choice == 1:
        player1 = input("Enter rock or paper or scissors : ")
        player2 = input("Enter rock or paper or scissors : ")

        if player1 == player2:
            print("Both players choose the same. ")
        elif player1 == "rock":
            if player2 == "scissors":
                print("Player1 is the winner.")
            else:
                print("player2 is the winner.")
        elif player1 == "paper":
            if player2 == "rock":
                print("Player1 is the winner")
            else:
                print("Player2 is the winner")
        elif player1 == "scissors":
            if player2 == "paper":
                print("player1 is the winner")
            else:
                print("player2 is the winner")
        else:
            print("You have not entered the correct choice.")

        choice = int(input("Press 1 to continue or 2 to exit program : "))
        if choice == 2:
            print("You are exiting the program.")
        break
