from random import randint


class submarine:
    #The basic class of the submarine in this game. 
    #It is 3 tiles long, and oriented either vertically or horizontally, and the "Bow" is defined
    #by its postion as an X,Y cordinate (positionx, positiony), for simplicity sake, the 
    #submarine is positoned left to right or top to bottom i.e. bow -> stern
    
    def __init__(self, positionx, positiony, orientation): #positionx and poistiony are int, orientation is a bool
        self.positionx = positionx
        self.positiony = positiony
        self.orientation = orientation
    
    def __repr__(self):
        xycoord = str(self.positionx) + ',' + str(self.positiony)
        if self.orientation == True:
            oriented = 'horizontally.'
        else:
             oriented = 'vertically.'
        return 'The submarine is postioned at ' + xycoord + ' and is oriented ' + oriented

def check_position(x, y, horizontal):
    on_board = True
    if horizontal == True and int(x) > 7:
        on_board  = False
    
    if horizontal == False and int(y) > 7:
        on_board = False
    return on_board


#get the initial position and orientation of the player's submarine
x = input('Enter X coordinate: ') #X coordinate
y = input('Enter Y coordinate: ') #Y coordinate
horizontal = input('Is your submarine positioned horizontally? (y/n): ')
orientation = str(horizontal).lower() in ("yes", "true", "t", "1", 'Y', 'y') #If true, orientation is horizontal, otherwise orientation is vertical

valid_position = check_position(x, y, orientation)
if valid_position == False:
    print('This position is out of bounds. Please enter a new position or change orientation')
else:
    player_sub = submarine(x, y, orientation)

#intial conditions for the enemy submarine
#enemy_sub = submarine(randint(0, 9), randint(0, 9), True)

#print(player_sub)
#print(enemy_sub)