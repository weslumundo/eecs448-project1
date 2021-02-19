#Name: Caden Kroonenberg

import Print, shotDetection, shipPlacement2

def run(shipCount):
    endGame = False
    player = 1
    
    print()
    print("Player 1:")
    shipPlacement2.placeShip(0, shipCount)
    player = 2
    print()
    print("Player 2:")
    shipPlacement2.placeShip(1, shipCount)
    player = 1

    while not endGame:
        if player == 1:
            print("Player 1:")
        elif player == 2:
            print("Player 2:")
        Print.printTopMap(player)
        print()
        Print.printBottomMap(player)
        shotDetection.shot(player)
    
        #check win condition and switch players if not
        if player == 1:
            if shotDetection.p1shotArr == shipPlacement2.p2shipArr:
                endGame = True
                print("\nPlayer 1 Wins!\n")
            else:
                player = 2
                print(chr(27) + "[2J")
        elif player == 2:
            if shotDetection.p2shotArr == shipPlacement2.p1shipArr:
                endGame = True
                print("\nPlayer 2 Wins!\n")
            else:
                player = 1
                print(chr(27) + "[2J")

print("\nBATTLESHIP\n")

repeat = True
while repeat == True:
        repeat = False
        shipCount = int(input("Enter ship count [1-5]: "))
        if shipCount > 5 or shipCount < 1:
            print("Invalid input. Try again")
            repeat = True

run(shipCount)