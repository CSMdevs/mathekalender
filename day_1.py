#Cemre Süler

import numpy
import random
#8 is defined
#11 is defined
#29 is defined

#define the grid
grid = numpy.array([
        [0, 0, 1, 4, 4, 0, 5, 2, 0, 3],
        [8, 0, 7, 4, 4, 0, 5, 0, 6, 6],
        [8, 9, 7, 0, 10, 10, 0, 0, 0, 0],
        [8, 0, 11, 12, 0, 13, 0, 14, 0, 0],
        [0, 0, 0, 0, 15, 0, 0, 0, 16, 16],
        [17, 0, 18, 18, 15, 19, 20, 21, 21, 22],
        [0, 0, 18, 18, 0, 19, 20, 23, 0, 0],
        [24, 24, 25, 0, 26, 26, 0, 0, 27, 0],
        [0, 0, 25, 0, 0, 0, 0, 0, 27, 28],
        [0, 29, 29, 29, 0, 0, 0, 0, 30, 28]
        ])

#print the grid
for i in range(0,10):
    print(grid[i])

alles_gedaan = False
random_goed = False
max_proberen = 9

while(alles_gedaan == False):
    aantal_nul = 0
    
    #generates random x and y
    randomY = random.randint(0,9)
    randomX = random.randint(0,9)
    random_goed == False
    #checks if these values are already defined
    while(random_goed == False):
        if(randomX == 0 and (randomY == 1 or randomY == 2 or randomY == 3)):
            randomY = random.randint(0,9)
            randomX = random.randint(0,9)
        elif(randomX == 2 and randomY == 3):
            randomY = random.randint(0,9)
            randomX = random.randint(0,9)
        elif((randomX == 1 or randomX == 1 or randomX == 3) and randomY == 9):
            randomY = random.randint(0,9)
            randomX = random.randint(0,9)
        else:
            random_goed = True

    if(grid[randomY, randomX] != 0):
        random_kant = random.randint(0,1)
        print(randomY, randomX)
        #links en rechts
        if(random_kant == 0 and randomX != 0 and randomX != 9 and grid[randomY,randomX-1] == 0 and grid[randomY,randomX+1] == 0):
            grid[randomY, randomX-1] = grid[randomY, randomX]
            grid[randomY, randomX+1] = grid[randomY, randomX]
            print(randomY, randomX)
       
        #boven en onder
        if(random_kant == 1 and randomY != 0 and randomY != 9 and grid[randomY-1,randomX] == 0 and grid[randomY+1,randomX] == 0):
            grid[randomY-1, randomX] = grid[randomY, randomX]
            grid[randomY+1, randomX] = grid[randomY, randomX]
            print(randomY, randomX)
        

    
    #checks if everything is filled in and gives the answer if that is true
    for y in range(0,10):
        for x in range(0,10):
            if(grid[y,x] == 0):
                aantal_nul += 1
            if(aantal_nul == 0):
                alles_gedaan = True
    #prints the new grid
    print("")

    for i in range(0,10):
        print(grid[i])
