#Name: Jiacheng Chen

p1shipArr = [
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

p2shipArr = [
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

def canonicalizeParts(parts):
     parts1 = sorted(parts, key=lambda part: part[0])
     parts2 = sorted(parts1, key=lambda part: part[1])
     return parts2

def isAdjacent(parts):
    keyX = list(set([x[0] for x in parts]))
    keyY = list(set([x[1] for x in parts]))
    if (len(keyX) == 1):
        #In the same row
        if len(keyY) != len(parts):
            return False
        #Adjacent
        if keyY[len(keyY) - 1] - keyY[0] + 1 != len(parts):
            return False
    elif (len(keyY) == 1):
        #In the same col
        if len(keyX) != len(parts):
            return False 
        #Adjacent
        if keyX[len(keyX) - 1] - keyX[0] + 1 != len(parts):
            return False 
    else:
        #Neither in row nor in col
        return False
    return True

def overlaps(parts, shipArr):
    for part in parts:
        x = part[0]
        y = part[1]
        if shipArr[x][y] != 0:
            return True
    return False

def placeBody(parts, shipArr):
    for part in parts:
        x = part[0]
        y = part[1]
        shipArr[x][y] = 1
        
#Will place a single ship in shipArr. Will throw runtime error if ship doesnt fit in array or overlaps w/ another ship.
def placeShip(player, shipCount):
    #player 1 = 1, player 2 = 2
    parts = []
    for shipBodyPart in range(1, shipCount +1):
        print('Place the #' + str(shipBodyPart) + 'of' + str(shipCount) + 'of the ship')
        #A-J and 1-10 notation for consistency
        repeat = True
        while repeat == True:
            repeat = False
            xChar = input('Enter a column [A-J] to fire upon: ')
            print("xChar:", xChar)
            if xChar == "A" or xChar == "a":
                xCoord = 0
            elif xChar == "B" or xChar == "b":
                xCoord = 1
            elif xChar == "C" or xChar == "c":
                xCoord = 2
            elif xChar == "D" or xChar == "d":
                xCoord = 3
            elif xChar == "E" or xChar == "e":
                xCoord = 4
            elif xChar == "F" or xChar == "f":
                xCoord = 5
            elif xChar == "G" or xChar == "g":
                xCoord = 6
            elif xChar == "H" or xChar == "h":
                xCoord = 7
            elif xChar == "I" or xChar == "i":
                xCoord = 8
            elif xChar == "J" or xChar == "j":
                xCoord = 9
            else:
                print("Invalid input. Try again")
                repeat = True
        yCoord = int(input('Enter a row [1-10] to fire upon: '))
        yCoord = yCoord - 1
        parts.append((xCoord, yCoord))
    parts = canonicalizeParts(parts)
    if not isAdjacent(parts):
            raise Exception()
    if player == 1:
        #Player 1
        if overlaps(parts, p1shipArr):
            raise Exception()
        placeBody(parts,p1shipArr)
    else:
        #Player 2
        if overlaps(parts, p1shipArr):
            raise Exception()
        placeBody(parts, p2shipArr)