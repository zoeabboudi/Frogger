import Draw
import random

#Set the Canvas
canvasSize = 1000
Draw.setCanvasSize(canvasSize, canvasSize) 

#Global variables representing the starting point of the frog
startingPointX = canvasSize//2
startingPointY = canvasSize - 300

#Functions to Draw the board
def drawWater():
    WATER = Draw.color(100, 130, 250) #Water color
    Draw.setColor(WATER)    
    Draw.filledRect(0, 445, canvasSize, 145)
    
def drawRoad():
    ROAD = Draw.color(170, 170, 170)
    Draw.setColor(ROAD) 
    Draw.filledRect(0, 95, canvasSize, 250)
    Draw.setColor(Draw.WHITE)
    for i in range (10, canvasSize, 120):
        Draw.filledRect(i, 150, 60, 10)
    for i in range (10, canvasSize, 120):
        Draw.filledRect(i, 250, 60, 10)    

#Draw the frog    
def drawfrog(curX, curY):  
    Draw.setColor(Draw.DARK_GREEN)
    Draw.filledOval(curX, curY, 25, 35)  #Body

    Draw.line(curX+2, curY+10, curX-5, curY+25) #Front Left Leg
    Draw.line(curX-5, curY+25, curX-3, curY+27)

    Draw.line(curX+22, curY+10, curX+30, curY+25) #Front Right Leg
    Draw.line(curX+30, curY+25, curX+28, curY+27)
    
    Draw.line(curX+2, curY+25, curX-5, curY+40) #Back Left Leg
    Draw.line(curX-5, curY+40, curX-3, curY+42)
    
    Draw.line(curX+22, curY+25, curX+30, curY+40) #Back Right Leg
    Draw.line(curX+30, curY+40, curX+28, curY+42) 
    
    Draw.setColor(Draw.GREEN)
    Draw.filledOval(curX+6, curY+5, 5, 5)     #Eyes
    Draw.filledOval(curX+15, curY+5, 5, 5)
    Draw.setColor(Draw.BLACK)

    Draw.filledOval(curX+7, curY+6, 2, 2)
    Draw.filledOval(curX+16, curY+6, 2, 2)
    
    
########### Functions for the moving elements of the water ###############
#Pass through the list w to draw all the floats according to their type
def drawFloats(w):
    for lanes in w:
        for floaty in lanes:
            if floaty[2] == "log":
                drawLogs(floaty)
            elif floaty[2] == "pad":
                drawPads(floaty)
            elif floaty[2] == "log":
                drawLogs(floaty)            

#How to draw each float           
def drawLogs(floaty): 
    sizeOfLogX = 90
    sizeOfLogY = 25
    BROWN = Draw.color(120, 90, 90)
    Draw.setColor(BROWN)
    Draw.filledRect(floaty[0], floaty[1], sizeOfLogX, sizeOfLogY)
    Draw.filledOval(floaty[0] - sizeOfLogY//2, floaty[1], sizeOfLogY, sizeOfLogY)
    Draw.filledOval(floaty[0] + sizeOfLogX - sizeOfLogY//2, floaty[1], sizeOfLogY, sizeOfLogY)
    Draw.setColor(Draw.BLACK)
    Draw.line(floaty[0], floaty[1] +7, floaty[0]+20, floaty[1]+7)
    Draw.line(floaty[0] + 40, floaty[1] + 10, floaty[0]+80, floaty[1]+10)
    Draw.line(floaty[0] + 10, floaty[1] + 15, floaty[0]+50, floaty[1]+15)

def drawPads (floaty):
    sizeOfPad = 60
    padGreen = Draw.color(100, 190, 100)
    Draw.setColor(padGreen)
    Draw.filledOval(floaty[0]+8, floaty[1], sizeOfPad//2, sizeOfPad//2)
    Draw.filledOval(floaty[0], floaty[1]+10, sizeOfPad//2, sizeOfPad//2)
    Draw.filledOval(floaty[0]+ sizeOfPad//4, floaty[1]+10, sizeOfPad//2, sizeOfPad//2)

#How to move the floats for level 1
def moveFloatsLevel1(w, sizeOfLogX, sizeOfLogY, curX, curY, sizeOfPad):
    for lanes in w:
        for floaty in lanes:
            floaty[0] += floaty[3] ##XCoord += the float's speed 
            if floaty[2] == "log":
                if curX +30 >= floaty[0] and curX <= floaty[0] + sizeOfLogX and curY == floaty[1]: ##if the frog is on the object, move frog with the object
                    curX += floaty[3]
            if floaty[2] == "pad":
                if curX +30 >= floaty[0] and curX <= floaty[0] + 30 and curY == floaty[1]:
                    curX += floaty[3]       
        if lanes[len(lanes)-1][2] == "log":  ##if the last float has reached its specified clearance, amend a new float to the list 
            if lanes[len(lanes)-1][0] <= lanes[len(lanes)-1][4]:  
                lanes.append([canvasSize+20, lanes[len(lanes)-1][1], lanes[len(lanes)-1][2], lanes[len(lanes)-1][3], lanes[len(lanes)-1][4] ])
        elif lanes[len(lanes)-1][2] == "pad":
            if lanes[len(lanes)-1][0] >= lanes[len(lanes)-1][4]:
                lanes.append([-20, lanes[len(lanes)-1][1], lanes[len(lanes)-1][2], lanes[len(lanes)-1][3], lanes[len(lanes)-1][4] ]) 
    return curX, curY

#How to move the floats for level 2
##essentially the same as level 1, except it is randomized
def moveFloatsLevel2(w, sizeOfLogX, sizeOfLogY, curX, curY, sizeOfPad):
    for lanes in w:
        for floaty in lanes:
            floaty[0] += floaty[3] ##XCoord += the speed 
            if floaty[2] == "log":
                if curX +30 >= floaty[0] and curX <= floaty[0] + sizeOfLogX and curY == floaty[1]:
                    curX += floaty[3]   
            if floaty[2] == "pad":
                if curX +30 >= floaty[0] and curX <= floaty[0] + 30 and curY == floaty[1]:
                    curX += floaty[3]
                 
    if w[0][-1][0] <= w[0][-1][4]: ##if the last float has reached its specified clearance, randomly select the components of a new float and amend it to the list
            w[0].append([canvasSize+20, w[0][-1][1], random.choice(["log", "pad"]), w[0][-1][3], w[0][-1][4] ])
    if w[1][-1][0] >= w[1][-1][4]:
            w[1].append([-50, w[1][-1][1], random.choice(["log", "pad"]), w[1][-1][3], w[1][-1][4] ])
    if w[2][-1][0] <= w[2][-1][4]:
            w[2].append([canvasSize+30, w[2][-1][1], random.choice(["log", "pad"]), w[2][-1][3], w[2][-1][4] ])
        
    return curX, curY    

#This function allows the program to evaluate if the frog is in the water but not on a float
def seeFrogInWater(w, curX, curY, sizeOfLogX, sizeOfLogY, lives):
    if curY >= 445 and curY <=580:  ##if the frog is in the water and on a float, no changes made. Otherwise, subtract a life and start over. 
        for lanes in w:
            for floaty in lanes:
                if floaty[2] == "log":
                    if curX +20 >= floaty[0] and curX <= floaty[0] + sizeOfLogX and curY == floaty[1]: return lives, curX, curY
                    
                if floaty[2] == "pad":
                    if curX +20 >= floaty[0] and curX <= floaty[0] + 30 and curY == floaty[1]: return lives, curX, curY
        lives -= 1
        drawSplash(curX, curY, 10)
        curX = startingPointX
        curY = startingPointY        
        
    return lives, curX, curY           
        
            

############# Functions for all vehicles ################
#Pass through the list v and draw each vehicle according to its type
def drawVehicles(v):
    for lanes in v:
        for vehicle in lanes:
            if vehicle[2] == "truck":
                drawTrucks(vehicle)
            elif vehicle[2] == "car":
                drawCars(vehicle)
            elif vehicle[2] == "bus":
                drawBusses(vehicle)
                
#Pass though the list motor and draw each motorcycle                
def drawAllMotorcycles(motor):
    for lanes in motor:
        for vehicle in lanes:
            drawMotorcycle(vehicle)

#How to draw each type of vehicle                    
def drawCars(vehicle):
    sizeOfCar = 30
    sizeOfWheel = 10
    TORQUISE = Draw.color(0,180, 180)
    Draw.setColor(TORQUISE)   
    Draw.filledOval(vehicle[0], vehicle[1], sizeOfCar+10, sizeOfCar)
    Draw.setColor(Draw.RED)
    Draw.filledOval(vehicle[0] + 5, vehicle[1]+ (sizeOfCar-5) , sizeOfWheel, sizeOfWheel)
    Draw.filledOval(vehicle[0] + 22, vehicle[1]+ (sizeOfCar-5), sizeOfWheel, sizeOfWheel)
    Draw.setColor(Draw.BLACK)   
    Draw.oval(vehicle[0], vehicle[1], sizeOfCar+10, sizeOfCar)
    Draw.filledOval(vehicle[0]+sizeOfCar-2, vehicle[1]+5, 10, 10)
    Draw.line(vehicle[0] +6, vehicle[1] + (sizeOfCar//2), vehicle[0]+10, vehicle[1]+(sizeOfCar//2))
    Draw.line(vehicle[0] +20, vehicle[1] + (sizeOfCar//2), vehicle[0]+25, vehicle[1]+(sizeOfCar//2))
    Draw.oval(vehicle[0] + 5, vehicle[1]+ (sizeOfCar-5) , sizeOfWheel, sizeOfWheel)
    Draw.oval(vehicle[0] + 22, vehicle[1]+ (sizeOfCar-5), sizeOfWheel, sizeOfWheel)
    
def drawTrucks(vehicle):
    sizeOfTruckX = 50
    sizeOfTruckY = 30
    sizeOfWheel = 10
    Draw.setColor(Draw.ORANGE)
    Draw.filledRect(vehicle[0], vehicle[1], sizeOfTruckX, sizeOfTruckY)
    Draw.filledRect(vehicle[0]+sizeOfTruckX, (vehicle[1] + sizeOfTruckY//2)-5, 10, (sizeOfTruckY//2)+5)
    Draw.setColor(Draw.BLACK)
    Draw.rect(vehicle[0], vehicle[1], sizeOfTruckX, sizeOfTruckY)
    Draw.rect(vehicle[0]+sizeOfTruckX, (vehicle[1] + sizeOfTruckY//2)-5, 10, (sizeOfTruckY//2)+5)
    Draw.setColor(Draw.PINK)
    Draw.filledOval(vehicle[0] + 5, vehicle[1] + (sizeOfTruckY -5), sizeOfWheel, sizeOfWheel)
    Draw.filledOval(vehicle[0] + 20, vehicle[1] + (sizeOfTruckY -5), sizeOfWheel, sizeOfWheel)
    Draw.filledOval(vehicle[0] + 35, vehicle[1] + (sizeOfTruckY -5), sizeOfWheel, sizeOfWheel)
    Draw.setColor(Draw.BLACK)
    Draw.oval(vehicle[0] + 5, vehicle[1] + (sizeOfTruckY -5), sizeOfWheel, sizeOfWheel)
    Draw.oval(vehicle[0] + 20, vehicle[1] + (sizeOfTruckY -5), sizeOfWheel, sizeOfWheel)
    Draw.oval(vehicle[0] + 35, vehicle[1] + (sizeOfTruckY -5), sizeOfWheel, sizeOfWheel)

def drawBusses(vehicle):
    sizeOfBusX = 55
    sizeOfBusY = 25
    sizeOfWheel = 10
    Draw.setColor(Draw.YELLOW)
    Draw.filledRect(vehicle[0], vehicle[1], sizeOfBusX, sizeOfBusY)
    Draw.setColor(Draw.BLACK)
    Draw.rect(vehicle[0], vehicle[1], sizeOfBusX, sizeOfBusY)
    Draw.filledOval(vehicle[0] + 10, vehicle[1] + (sizeOfBusY -5), sizeOfWheel, sizeOfWheel)
    Draw.filledOval(vehicle[0] + 30, vehicle[1] + (sizeOfBusY -5), sizeOfWheel, sizeOfWheel)
    for i in range(2, 61, 12):
        Draw.filledRect(vehicle[0]+i, vehicle[1] + 5, 6, 6)
        
def drawMotorcycle(motor):
    Draw.setColor(Draw.BLACK)
    Draw.filledOval(motor[0] +15, motor[1], 20, 18)
    Draw.filledOval(motor[0], motor[1], 20, 7)
    Draw.line(motor[0] +43, motor[1]+10, motor[0] +35, motor[1]-7)
    Draw.line(motor[0] +42, motor[1]+10, motor[0] +34, motor[1]-7)
    Draw.line(motor[0] +41, motor[1]+10, motor[0] +33, motor[1]-7)
    Draw.line(motor[0] +40, motor[1]+10, motor[0] +32, motor[1]-7)
    Draw.filledOval(motor[0] +22, motor[1]-2, 15, 7)
    NAVY = Draw.color(0, 0, 50)
    Draw.setColor(NAVY)        
    DARK_RED = Draw.color(100, 0, 0) 
    Draw.setColor(DARK_RED)        
    Draw.filledOval(motor[0] , motor[1]+5, 20, 20)
    Draw.filledOval(motor[0] +35, motor[1]+10, 15, 15)

#How to move the vehicles for level 1   
def moveVehiclesLevel1(v, curX, curY, sizeOfTruckX, sizeOfTruckY,sizeOfWheel, sizeOfBusX, sizeOfBusY,  sizeOfCar, lives): 
    for lanes in v:
        for vehicle in lanes:
            vehicle[0] += vehicle[3] ##XCoord += the speed 
            if vehicle[2] == "truck":  ##if frog hits the vehicle, subtract a life and start over
                if curX +20 >= vehicle[0] and curX <= vehicle[0] + sizeOfTruckX and curY >= vehicle[1] and curY <= vehicle[1] + sizeOfTruckY+sizeOfWheel:
                    lives -=1
                    drawSplat(curX, curY,20)
                    curX = startingPointX
                    curY = startingPointY       
            elif vehicle[2] == "car":
                if curX +20 >= vehicle[0] and curX <= vehicle[0] + sizeOfCar and curY >= vehicle[1] and curY <= vehicle[1] + sizeOfCar+sizeOfWheel:
                    lives -= 1
                    drawSplat(curX, curY,10)
                    curX = startingPointX
                    curY = startingPointY                        
            elif vehicle[2] == "bus":
                if curX +20 >= vehicle[0] and curX <= vehicle[0] + sizeOfBusX and curY >= vehicle[1] and curY <= vehicle[1] + sizeOfBusY + sizeOfWheel:
                    lives -= 1 
                    drawSplat(curX, curY,10)
                    curX = startingPointX
                    curY = startingPointY                        
        if lanes[len(lanes)-1][0] >= lanes[len(lanes)-1][4]:  ##(X coordinate of the last vehicle in the list is greater than clearance)
            lanes.append([-15, lanes[len(lanes)-1][1], lanes[len(lanes)-1][2], lanes[len(lanes)-1][3], lanes[len(lanes)-1][4] ]) ##copy a new vehicle list at X=0
    return lives,curX,curY

#How to move the vehicles for level 2
##essentially the same as level 1, but randomized
def moveVehiclesLevel2(v, curX, curY, sizeOfTruckX, sizeOfTruckY,sizeOfWheel, sizeOfBusX, sizeOfBusY,  sizeOfCar, lives): 
    for lanes in v:
        for vehicle in lanes:
            vehicle[0] += vehicle[3] ##XCoord += the speed 
            if vehicle[2] == "truck": ##if frog hits a vehicle, subtract a life and start over
                if curX +20 >= vehicle[0] and curX <= vehicle[0] + sizeOfTruckX and curY >= vehicle[1] and curY <= vehicle[1] + sizeOfTruckY+sizeOfWheel:
                    lives -=1
                    drawSplat(curX, curY,20)
                    curX = startingPointX
                    curY = startingPointY
            elif vehicle[2] == "car":
                if curX +20 >= vehicle[0] and curX <= vehicle[0] + sizeOfCar and curY >= vehicle[1] and curY <= vehicle[1] + sizeOfCar+sizeOfWheel:
                    lives -= 1
                    drawSplat(curX, curY,10)
                    curX = startingPointX
                    curY = startingPointY                        
            elif vehicle[2] == "bus":
                if curX +20 >= vehicle[0] and curX <= vehicle[0] + sizeOfBusX and curY >= vehicle[1] and curY <= vehicle[1] + sizeOfBusY + sizeOfWheel:
                    lives -= 1 
                    drawSplat(curX, curY,10)
                    curX = startingPointX
                    curY = startingPointY  
        
        if lanes[len(lanes)-1][0] >= lanes[len(lanes)-1][4]: ##if the last vehicle in the list reached its clearance, randomly select the attributes of a new vehicle
            lanes.append([-15, lanes[len(lanes)-1][1], random.choice(["truck", "bus", "car"]), lanes[len(lanes)-1][3], random.choice([350, 300, 250, 200] )] )
            ##append that new vehicle to the list
    return lives,curX,curY 

#How to move motorcycles
def moveMotorcycle(motor, curX, curY, lives):
    for lanes in motor:
        for vehicle in lanes: 
            vehicle[0] += vehicle[3] ##XCoord += the speed
            if curX +20 >= vehicle[0] and curX <= vehicle[0] + 60 and curY >= vehicle[1] and curY <= vehicle[1] + 40: ##if frog hits a motorcycle, lose life, start over
                lives -= 1 
                drawSplat(curX, curY,10)
                curX = startingPointX
                curY = startingPointY
        if vehicle[0] >= canvasSize-20:
            lanes.append([-550, lanes[len(lanes)-1][1], "motorcycle", 10])
    return lives, curX, curY



#How to draw a "splat" when frog hits a vehicle
def drawSplat(curX, curY, i):        
    Draw.setColor(Draw.YELLOW)
    Draw.filledPolygon([curX, curY,
              curX + i, curY +i*2,
              curX + i*2, curY +i*2,
              curX +i, curY +i*3,
              curX +i*2, curY +i*4,
              curX , curY +i*3,
              curX -i*2, curY +i*4,
              curX -i, curY +i*3,
              curX -i*2, curY +i*2,
              curX -i, curY +i*2])    
    Draw.setColor(Draw.ORANGE)
    Draw.polygon([curX, curY,
              curX + i, curY +i*2,
              curX + i*2, curY +i*2,
              curX +i, curY +i*3,
              curX +i*2, curY +i*4,
              curX , curY +i*3,
              curX -i*2, curY +i*4,
              curX -i, curY +i*3,
              curX -i*2, curY +i*2,
              curX -i, curY +i*2]) 

#How to draw a "splash" when frog falls in the water    
def drawSplash(curX, curY, i):        
    Draw.setColor(Draw.WHITE)
    Draw.filledPolygon([curX, curY,
              curX + i, curY +i*2,
              curX + i*2, curY +i*2,
              curX +i, curY +i*3,
              curX +i*2, curY +i*4,
              curX , curY +i*3,
              curX -i*2, curY +i*4,
              curX -i, curY +i*3,
              curX -i*2, curY +i*2,
              curX -i, curY +i*2])    
    Draw.filledOval(curX - 15, curY+5, 9, 9)
    Draw.filledOval(curX - 15, curY-3, 5, 5)
    Draw.filledOval(curX - 27, curY+1, 5, 5)
    Draw.filledOval(curX + 10, curY+7, 9, 9)
    Draw.filledOval(curX + 15, curY-3, 5, 5)
    Draw.filledOval(curX + 27, curY+1, 5, 5) 
    Draw.filledOval(curX , curY+35, 5, 5)
    Draw.filledOval(curX-20, curY+45, 5, 5)
    Draw.filledOval(curX+20, curY+45, 5, 5)

#This function is responsible for tracking and displaying the status of the game
def status(lives, curX, curY):
    Draw.setColor(Draw.RED) ##display lives remaining
    Draw.setFontSize(18)
    Draw.string("Lives Remaining: " + str(lives), 100, 10)       
    Draw.setFontBold(True)
    Draw.setFontSize(20)  ##display the back button
    Draw.string("< BACK", canvasSize - 100, 10)
    
    if curY <= 95:  ##if the frog crosses sucessfully, give the player an option to play again or quit  
        Draw.setColor(Draw.MAGENTA)
        Draw.setFontSize(80)
        Draw.string("PHEW!", 400, 200)
        GREY = Draw.color(170, 170, 170)
        for i in range (340, 500, 100):
            Draw.setColor(GREY)
            Draw.filledRect(400, i, 200, 60)
            Draw.setColor(Draw.BLACK)
            Draw.rect(400, i, 200, 60)            
        Draw.setColor(Draw.BLACK)
        Draw.setFontSize(20)
        Draw.string("Play Again?", 450, 360) 
        Draw.string("Quit", 460, 460)  
        
    if Draw.mousePressed():      ##respond to user clicks: return or start over
        if Draw.mouseX() >= canvasSize-100 and Draw.mouseX() <= canvasSize and Draw.mouseY() <= 30:
            playGame()
        if curY <= 95 and Draw.mouseX() >= 400 and Draw.mouseX() <= 600 and Draw.mouseY() >= 340 and Draw.mouseY() <= 400:
            curX = startingPointX
            curY = startingPointY
        elif curY <= 95 and Draw.mouseX() >= 400 and Draw.mouseX() <= 600 and Draw.mouseY() >= 440 and Draw.mouseY() <= 500:
            playGame()
    return curX, curY 



#Function for level 1   
def Level1():
    LIGHT_BLUE = Draw.color(190, 200, 250)
    Draw.setBackground(LIGHT_BLUE)  
    
    GameOn = True
    lives = 3
    
    #The following are 3-D lists that contain the attributes of each car or float in a lane: [X-coorinate, Ycoordinate, type, velocity, clearance]
    v = [ [ [710, 100, "truck", 5, 300], [310, 100, "truck", 5, 350], [10, 100, "truck", 5, 300] ],  #lane 1 
    [ [600, 200, "car", 8, 250], [350, 200, "car", 8, 250], [100, 200, "car", 8, 250] ],             #lane 2
    [ [660, 300, "bus", 5, 300], [360, 300, "bus", 5, 300], [60, 300, "bus", 5, 300] ]  ]            #lane 3
    
    w = [ [ [10, 550, "log", -1, canvasSize-200], [210, 550, "log", -1, canvasSize-200], [410, 550, "log", -1, canvasSize-200], [610, 550, "log", -1, canvasSize-200], \
            [810, 550, "log", -1, canvasSize-200] ],      #lane 1
          [ [780, 500, "pad", 1, 250], [530, 500, "pad", 1, 250], [280, 500, "pad", 1, 250], [30, 500, "pad", 1, 250] ], #lane 2
          [ [50, 450, "log", -1, canvasSize-200], [250, 450, "log", -1, canvasSize-200], [450, 450, "log", -1, canvasSize-200], [650, 450, "log", -1, canvasSize-200],\
            [850, 450, "log", -1, canvasSize-200] ] ] #lane 3
    
    #initialize size of moving vehicles and floats, and position of the frog
    sizeOfCar = 30 
    sizeOfWheel = 10
    sizeOfTruckX = 50
    sizeOfTruckY = 30
    sizeOfBusX = 55
    sizeOfBusY = 25
    sizeOfLogX = 90
    sizeOfLogY = 25  
    sizeOfPad = 60
    curX = startingPointX          
    curY = startingPointY
    
    while GameOn:
        if Draw.hasNextKeyTyped():             #Respond to user buttons
            newKey = Draw.nextKeyTyped()
            if newKey == "Up":
                curY -= 50
            elif newKey == "Down":
                curY += 50      
            elif newKey == "Right":
                curX += 50
            elif newKey == "Left":
                curX -= 50
                
        if lives == 0:
            GameOn = False
    
        Draw.clear()
        #draw the board, floats, vehicles, status, and frog
        drawRoad()
        drawWater()
        drawFloats(w)
        drawVehicles(v)
        drawfrog(curX, curY)
        curX, curY = status(lives, curX, curY)
        lives, curX, curY = seeFrogInWater(w, curX, curY, sizeOfLogX, sizeOfLogY, lives)
        lives, curX, curY = moveVehiclesLevel1(v, curX, curY, sizeOfTruckX, sizeOfTruckY,sizeOfWheel, sizeOfBusX, sizeOfBusY,  sizeOfCar, lives)
        curX, curY = moveFloatsLevel1(w, sizeOfLogX, sizeOfLogY, curX, curY, sizeOfPad)
        Draw.show()


#Function for level 2    
def Level2():
    DARK_PURPLE = Draw.color(220, 180, 240)
    Draw.setBackground(DARK_PURPLE)
    
    #The following are 3-D lists that contain the attributes of each car, float, or motorcycle in a lane: [X-coorinate, Ycoordinate, type, velocity, clearance]
    ##list of vehicles:
    v = [ [ [710, 100, "bus", 8, 300], [310, 100, "truck", 8, 350], [10, 100, "car", 8, 300] ],  #lane 1 
    [ [600, 200, "truck", 5, 250], [350, 200, "car", 5, 250], [100, 200, "truck", 5, 250] ],     #lane 2
    [ [660, 300, "truck", 5, 300], [360, 300, "bus", 5, 300], [60, 300, "car", 5, 300] ]  ]      #lane 3
    ##list of floats
    w = [ [ [10, 550, "pad", -1, canvasSize-200], [210, 550, "log", -1, canvasSize-200], [410, 550, "log", -1, canvasSize-200], [610, 550, "pad", -1, canvasSize-200], \
            [810, 550, "log", -1, canvasSize-200] ],        #lane 1
          [ [780, 500, "pad", 1, 200], [530, 500, "log", 1, 200], [280, 500, "pad", 1, 200], [30, 500, "log", 1, 200] ],   #lane 2
          [ [50, 450, "log", -1, canvasSize-200], [250, 450, "log", -1, canvasSize-200], [450, 450, "pad", -1, canvasSize-200], [650, 450, "log", -1, canvasSize-200], \
            [850, 450, "pad", -1, canvasSize-200] ] ]      #lane 3
    ##list of motorcycles
    motor = [ [ [canvasSize-300, 150, "motorcycle", 10] ], #lane 1
             [ [-50, 250, "motorcycle", 10] ] ]            #lane 2
    
    GameOn = True
    lives = 3
    
    #initialize size of vehicles and floats, and position of frog
    sizeOfCar = 30 
    sizeOfWheel = 10
    sizeOfTruckX = 50
    sizeOfTruckY = 30
    sizeOfBusX = 55
    sizeOfBusY = 25
    curX = startingPointX          ##Initialize Position of the frog
    curY = startingPointY
    sizeOfLogX = 90
    sizeOfLogY = 25  
    sizeOfPad = 60
    while GameOn:
        if Draw.hasNextKeyTyped():             #Respond to user buttons
            newKey = Draw.nextKeyTyped()
            if newKey == "Up":
                curY -= 50
            elif newKey == "Down":
                curY += 50
            elif newKey == "Right":
                curX += 50
            elif newKey == "Left":
                curX -= 50
        if lives == 0:
            GameOn = False
        
        #Draw board, vehicles, cloats, motorcycles, frog, and status
        Draw.clear()
        drawRoad()
        drawWater()
        drawFloats(w)
        drawVehicles(v)
        drawAllMotorcycles(motor)
        drawfrog(curX, curY)
        curX, curY = status(lives, curX, curY)
        (lives, curX, curY) = seeFrogInWater(w, curX, curY, sizeOfLogX, sizeOfLogY, lives)
        lives, curX, curY = moveVehiclesLevel2(v, curX, curY, sizeOfTruckX, sizeOfTruckY,sizeOfWheel, sizeOfBusX, sizeOfBusY,  sizeOfCar, lives)
        curX, curY = moveFloatsLevel2(w, sizeOfLogX, sizeOfLogY, curX, curY, sizeOfPad)
        lives, curX, curY = moveMotorcycle(motor, curX, curY, lives)
        Draw.show()    


#The main function
def playGame():
    while True:
        Draw.clear()
        x = 200
        l = 0
        #Draw Play Game and Level options
        colors = [Draw.YELLOW, Draw.BLUE, Draw.RED, Draw.GREEN, Draw.ORANGE]
        Draw.setBackground(Draw.BLACK)
        Draw.setFontBold(False)
        Draw.setFontSize(80)
        Draw.setColor(Draw.YELLOW)
        for i in "PLAY GAME":
            x += 60
            Draw.setColor(random.choice(colors))
            Draw.string(i, x, 200)
        GREY = Draw.color(170, 170, 170)
        for i in range (340, 500, 100):
            Draw.setColor(GREY)
            Draw.filledRect(400, i, 200, 60)
            Draw.setColor(Draw.BLACK)
            Draw.setFontSize(20)
            l += 1
            Draw.string("LEVEL " + str(l), 455, i +20)
        
        if Draw.mousePressed():             #Respond to user buttons
            if Draw.mouseX() >= 400 and Draw.mouseX() <= 600 and Draw.mouseY() >= 340 and Draw.mouseY() <= 400:
                Level1()
            elif Draw.mouseX() >= 400 and Draw.mouseX() <= 600 and Draw.mouseY() >= 440 and Draw.mouseY() <= 500:
                Level2()

        Draw.show(100) #slow down the flashing
    

playGame()
    