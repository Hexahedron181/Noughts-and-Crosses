import random
import time

print("\n\n----- WELCOME TO NOUGHTS AND CROSSES -----")

playAgain = "y"

while playAgain == "y" or playAgain == "Y":
    
    while True:
        playerTwo = int(input("\n1. Two Player\n\n2. Against AI\n\n=  "))
        playAgain = "n"
        break
        if playerTwo != 1 or playerTwo != 2:
            print("Input in valid please try again")

    ########## Table ##########

    slotsA = ["--", "--", "--"]
    slotsB = ["--", "--", "--"]
    slotsC = ["--", "--", "--"]

    def Table():
        line = 1
        space = "    "
        print("\n\n")
        letter = ["a", "b", "c"]
        slot = 0
        coordsNum = 1
        coordsLetter = 0
        print(end=space)
        for i in range(0, 3):
            print("{0:3}".format(coordsNum), end=space)
            coordsNum = coordsNum + 1
            #Top numbers
        for i in range(0, 3):
            print("\n")
            print(letter[coordsLetter], end=space)
            slot = 0
            #Side letters
            if line == 1:
                for i in range(0,3):
                    print("{0:3}".format(slotsA[slot]), end=space)
                    slot = slot + 1
            elif line == 2:
                for i in range(0,3):
                    print("{0:3}".format(slotsB[slot]), end=space)
                    slot = slot + 1
            elif line == 3:
                for i in range(0,3):
                    print("{0:3}".format(slotsC[slot]), end=space)
                    slot = slot + 1
            line = line + 1
                #Centre slots
            coordsNum = coordsNum + 1
            coordsLetter = coordsLetter + 1

    ########## WINNER ##########

    def checkWinner():
        #Horizontal
        if slotsA[0] == "x" and slotsA[1] == "x" and slotsA[2] == "x" or slotsA[0] == "o" and slotsA[1] == "o" and slotsA[2] == "o":
            if slotsA[0] == "x":
                print("\n\nPLAYER 1 WINNER!!!")
                return 1
            else:
                print("\n\nPLAYER 2 WINNER!!!")
                return 1

        
        elif slotsB[0] == "x" and slotsB[1] == "x" and slotsB[2] == "x" or slotsB[0] == "o" and slotsB[1] == "o" and slotsB[2] == "o":
            if slotsB[0] == "x":
                print("\n\nPLAYER 1 WINNER!!!")
                return 1
            else:
                print("\n\nPLAYER 2 WINNER!!!")
                return 1

        
        elif slotsC[0] == "x" and slotsC[1] == "x" and slotsC[2] == "x" or slotsC[0] == "o" and slotsC[1] == "o" and slotsC[2] == "o":
            if slotsC[0] == "x":
                print("\n\nPLAYER 1 WINNER!!!")
                return 1
            else:
                print("\n\nPLAYER 2 WINNER!!!")
                return 1

        #Vertical
        elif slotsA[0] == "x" and slotsB[0] == "x" and slotsC[0] == "x" or slotsA[0] == "o" and slotsB[0] == "o" and slotsC[0] == "o":
            if slotsA[0] == "x":
                print("\n\nPLAYER 1 WINNER!!!")
                return 1
            else:
                print("\n\nPLAYER 2 WINNER!!!")
                return 1
        elif slotsA[1] == "x" and slotsB[1] == "x" and slotsC[1] == "x" or slotsA[1] == "o" and slotsB[1] == "o" and slotsC[1] == "o":
            if slotsA[1] == "x":
                print("\n\nPLAYER 1 WINNER!!!")
                return 1
            else:
                print("\n\nPLAYER 2 WINNER!!!")
                return 1
            
        elif slotsA[2] == "x" and slotsB[2] == "x" and slotsC[2] == "x" or slotsA[2] == "o" and slotsB[2] == "o" and slotsC[2] == "o":
            if slotsA[2] == "x":
                print("\n\nPLAYER 1 WINNER!!!")
                return 1
            else:
                print("\n\nPLAYER 2 WINNER!!!")
                return 1
            
        #Diagonal
        elif slotsA[0] == "x" and slotsB[1] == "x" and slotsC[2] == "x" or slotsA[0] == "o" and slotsB[1] == "o" and slotsC[2] == "o":
            if slotsA[0] == "x":
                print("\n\nPLAYER 1 WINNER!!!")
                return 1
            else:
                print("\n\nPLAYER 2 WINNER!!!")
                return 1
            
        elif slotsA[2] == "x" and slotsB[1] == "x" and slotsC[0] == "x" or slotsA[2] == "o" and slotsB[1] == "o" and slotsC[0] == "o":
            if slotsA[2] == "x":
                print("\n\nPLAYER 1 WINNER!!!")
                return 1
            else:
                print("\n\nPLAYER 2 WINNER!!!")
                return 1
        #Draw
        Num = 0
        Draw = 0
        for i in range(0, 3):
            if slotsA[Num] == "x" or slotsA[Num] == "o": 
                Draw = Draw + 1
                Num = Num + 1
        Num = 0
        for i in range(0, 3):
            if slotsB[Num] == "x" or slotsB[Num] == "o":
                Draw = Draw + 1
                Num = Num + 1
        Num = 0
        for i in range(0, 3):
            if slotsC[Num] == "x" or slotsC[Num] == "o":
                Draw = Draw + 1
                Num = Num + 1
        if Draw == 9:
            print("\n\nDRAW!!!")
        else:
            return 0

    ########## PLAYER 2 ##########

    def player2():
        
        playerNum = 2
        
        while playerNum == 2:
            
            print("\n")
            P2 = input("Player 2 - Input Coordinates: ")
            playerNum = 1
            if P2[1] == "a":
                Num = int(P2[0])
                Num = Num - 1
                #Change the first number to an integer and minus 1
                if slotsA[Num] == "x" or slotsA[Num] == "o":
                    print("Spot aready taken. Please try again")
                    playerNum = 2
                else:
                    slotsA[Num] = "o"
                    Table()
                    Win = checkWinner()
                    playerNum = 1
            elif P2[1] == "b":
                Num = int(P2[0])
                Num = Num - 1
                #Change the first number to an integer and minus 1
                if slotsB[Num] == "x" or slotsB[Num] == "o":
                    print("Spot aready taken. Please try again")
                    playerNum = 2
                else:
                    slotsB[Num] = "o"
                    Table()
                    Win = checkWinner()
                    playerNum = 1
            elif P2[1] == "c":
                Num = int(P2[0])
                Num = Num - 1
                #Change the first number to an integer and minus 1
                if slotsC[Num] == "x" or slotsC[Num] == "o":
                    print("Spot aready taken. Please try again")
                    playerNum = 2
                else:
                    slotsC[Num] = "o"
                    Table()
                    Win = checkWinner()
                    playerNum = 1
            else:
                print("Input invalid")
                playerNum = 2

        return Win

    ########## AI ##########

    def AI():

        playerNum = 2

        while playerNum == 2:
            
            coordinates = ["1a", "1b", "1c", "2a", "2b", "2c", "3a", "3b", "3c"]
            P2 = random.choice(coordinates)
            playerNum = 1
            if P2[1] == "a":
                Num = int(P2[0])
                Num = Num - 1
                #Change the first number to an integer and minus 1
                if slotsA[Num] == "x" or slotsA[Num] == "o":
                    playerNum = 2
                else:
                    time.sleep(1)
                    slotsA[Num] = "o"
                    Table()
                    Win = checkWinner()
                    playerNum = 1
            elif P2[1] == "b":
                Num = int(P2[0])
                Num = Num - 1
                #Change the first number to an integer and minus 1
                if slotsB[Num] == "x" or slotsB[Num] == "o":
                    playerNum = 2
                else:
                    time.sleep(1)
                    slotsB[Num] = "o"
                    Table()
                    Win = checkWinner()
                    playerNum = 1
            elif P2[1] == "c":
                Num = int(P2[0])
                Num = Num - 1
                #Change the first number to an integer and minus 1
                if slotsC[Num] == "x" or slotsC[Num] == "o":
                    playerNum = 2
                else:
                    time.sleep(1)
                    slotsC[Num] = "o"
                    Table()
                    Win = checkWinner()
                    playerNum = 1
        return Win
            
    ########## USERINPUT ##########

    Table()
    playerNum = 1
    Win = 0

    while Win == 0:

        ### Player 1 ###
        if playerNum == 1:
            print("\n")
            P1 = input("Player 1 - Input Coordinates: ")
            playerNum = 2
            #Ensures next round is next player
            if P1[1] == "a":
                Num = int(P1[0])
                Num = Num - 1
                #Change the first number to an integer and minus 1
                if slotsA[Num] == "x" or slotsA[Num] == "o":
                    print("Spot already taken. Please try again")
                    playerNum = 1
                else:
                    slotsA[Num] = "x"
                    Table()
                    Win = checkWinner()
                    playerNum = 2
            elif P1[1] == "b":
                Num = int(P1[0])
                Num = Num - 1
                #Change the first number to an integer and minus 1
                if slotsB[Num] == "x" or slotsB[Num] == "o":
                    print("Spot already taken. Please try again")
                    playerNum = 1
                else:
                    slotsB[Num] ="x"
                    Table()
                    Win = checkWinner()
                    playerNum = 2
            elif P1[1] == "c":
                Num = int(P1[0])
                Num = Num - 1
                #Change the first number to an integer and minus 1
                if slotsC[Num] == "x" or slotsC[Num] == "o":
                    print("Spot already taken. Please try again")
                    playerNum = 1
                else:
                    slotsC[Num] = "x"
                    Table()
                    Win = checkWinner()
                    playerNum = 2
            else:
                print("Input invalid, try again")
                playerNum = 1

        ### Player 2 ###
        elif playerNum == 2:
            #Ensures next round is next player
            if playerTwo == 1:
                Win = player2()
                playerNum = 1
            elif playerTwo == 2:
                Win = AI()
                playerNum = 1


    tryAgain = 1
    
    while tryAgain == 1:
        playAgain = input("\nDo you wish to play again Y/N: ")
        if playAgain != "Y" and playAgain != "y" and playAgain != "N" and playAgain != "n":
            tryAgain = 1
        else:
            tryAgain = 0






