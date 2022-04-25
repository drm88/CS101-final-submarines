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


#get the initial position and orientation of the player's submarine
x = input('Enter X coordinate: ') #X coordinate
y = input('Enter Y coordinate: ') #Y coordinate
horizontal = input('Is your submarine positioned horizontally? (y/n): ')
orientation = str(horizontal).lower() in ("yes", "true", "t", "1", 'Y', 'y') #If true, orientatin is horizontal, otherwise orientation is vertical
player_sub = submarine(x, y, orientation)
print(player_sub)