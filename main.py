# Members: I.V. = Iggy Villar 20961016 |  N.G. = Neo Glykis 21023327 |   R.D. = Roshan Dayananda 21013286
import random, pygame, sys
from pygame.locals import *
# Section 1: I.V.
FPS = 15 # This line of code controls the frames per second that the game will run on
WINDOWWIDTH = 640 #This line sets the size of the width of the window in which the game will be played on 
WINDOWHEIGHT = 480 #Sets the size of the hieght of the windown in which the game will be played on
CELLSIZE = 20 #The game is set ina grid, the background, as well as the snake segments, this alters the size of the squares of the grid.
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE) #
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
#             R    G    B
WHITE     = (255, 255, 255) #This whole subsection of code is setting colours as variables so that they can be more easily accessed and readable, rather than inputting them as a set of numbers.
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK
UP = 'up'                   #Similar to the previous little subsection, this area is setting variables for the movement keys, eliminating the extra quotation marks added.
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
HEAD = 0 # syntactic sugar: index of the worm's head

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT #sets up the variables in the global scope so that they can be accessed by other functions
    pygame.init() #initializes imported modules
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) #setting the display size, using the window width and window hieght stated previously
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18) #sets the font type and size for the words that will be displayed
    pygame.display.set_caption('Wormy') #The piece of text that will appear when you start the game
    showStartScreen() 
    while True: #This while loop keeps the game running and the game over screen appearing until 'while True' , which is later defined is still true
        runGame()
        showGameOverScreen()
def runGame():
    # Set a random start point.
    startx = random.randint(5, CELLWIDTH - 6)   #determines a random x coordinate in which the snake will be spawned
    starty = random.randint(5, CELLHEIGHT - 6)  #determines a random y coordinate in which the snake will be spawned
    wormCoords = [{'x': startx,     'y': starty}, #variable for the coordinates of the snake
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT       #determines the starting direction of which the snake will go, when the game starts
    
 #Section 2: N.G.
    # Start the apple in a random place.
while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT: #Assigns an if statememnt to what would happen if the player would press the quit button. N.G
                terminate() #The game will close. N.G
            elif event.type == KEYDOWN: #assigns if statement to if any of the direction buttons are pressed. N.G
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT: #If the player presses the left key, and not the right key. N.G
                    direction = LEFT #The worm will move left. N.G
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT: #If the player presses the right key, and not the let key. N.G
                    direction = RIGHT #The worm will move right. N.G
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN: #If the player presses the up key, and not the down key. N.G
                    direction = UP #The worm will move up. N.G
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP: #If the player presses the down key, and not the up key. N.G
                    direction = DOWN #The worm will move down. N.G
                elif event.key == K_ESCAPE: #If the player presses the escape key. N.G
                    terminate() #The game will close. N.G

        # check if the worm has hit itself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT: #Assiging an if statement to what would happen if the head of the worm would hit one of the walls. N.G
            #Cellwidth being the walls on the left and right, cellheight being the walls on the top and bottom. It would hit the left and right walls when travelling in the x direction, and would hit the top and bottom walls when moving in the y direction. N.G
            return game over #The game would end when the player hits the wall. N.G
        for wormBody in wormCoords[1:]: #Assigning a for statement to what would happen if the worm hits itself. N.G
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']: #If the head of the worm hits its own body, or when the position of the bodyequals the position of the head. N.G
                return game over #The game will end when this happens. N.G

        # check if worm has eaten an apple
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']: #when the position of the head of the worm equals the position of an apple. N.G
            # don't remove worm's tail segment
            apple = getRandomLocation() # set a new apple somewhere
        else:
            del wormCoords[-1] # remove worm's tail segment

        # move the worm by adding a segment in the direction it is moving
        if direction == UP: #if the worm is currently moving upwards. N.G
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1} #The new addition to the worm will spawn at the lowest y-value of the worms body that it will allow(very bottom of the snake). N.G
        elif direction == DOWN: #If the worm is currently moving downwards. N.G
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1} #The new addition to the worm will spawn at the highest y-value of the worms body that it will allow(very top of the snake). N.G
        elif direction == LEFT: #if the worm is currently moving to the left. N.G
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']} #The new addition to the worm will spawn at the rightmost x-value of the worms body that it will allow. N.G
        elif direction == RIGHT: #if the worm is currently mvoing to the right. N.G
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']} #The new addition to the worm will spawn at the leftmost x-value of the worms body that it will allow. N.G
        wormCoords.insert(0, newHead) #inserts a new head for the body of the worm. N.G
        DISPLAYSURF.fill(BGCOLOR) #matches the colour of the new body to the rest of the snake. N.G
        drawGrid() #spawns grid at tiles in which the worm just left(swaps a worm value for a grid value). N.G
        drawWorm(wormCoords) #spawns thw worm at tiles in which it moves to. N.G
        drawApple(apple) #draws the apple onto the grid. N.G
        drawScore(len(wormCoords) - 3) #displays the score on the screen, increases with more apples that the worm eats N.G
        pygame.display.update() #displays game updates. N.G
        FPSCLOCK.tick(FPS) #FPS(frames per second) is how many times a game reloads in one second. High frames are desirable for smoother gameplay. This functiom enables a clock to count the seconds in which the frame rate will be based off of. N.G

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
    
#Section 3: R.D.
def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key
def showStartScreen(): # Function for showing the start screen RD
    titleFont = pygame.font.Font('freesansbold.ttf', 100) # Assigns the freesansbold as the font for the game title, 100 is the font size RD
    titleSurf1 = titleFont.render('Wormy!', True, WHITE, DARKGREEN) # Renders one display of the title with the colours white and dark green RD
    titleSurf2 = titleFont.render('Wormy!', True, GREEN)# Assigns the secondary title green RD
    degrees1 = 0 # default degrees the title starts at for title 1 RD
    degrees2 = 0 # default degrees the title starts at for titles 2 RD
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)
        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)
        drawPressKeyMsg()
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame
def terminate():
    pygame.quit()
    sys.exit()
def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}
def showGameOverScreen(): # defines the function that displays the GAME OVER screen RD
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150) # assigns the font and text size of the GAME OVER text RD
    gameSurf = gameOverFont.render('Game', True, WHITE) # Renders the text in white for the word GAME RD
    overSurf = gameOverFont.render('Over', True, WHITE) # Renders the text in white for the word OVER RD
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)
    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue
    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return

def drawScore(score): # defines Function that places the players score in the top left RD
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE) # This line dictates the colour in which the score is displayed and the accompanying string RD 
    scoreRect = scoreSurf.get_rect() # Draws a recctangle around the score and text RD
    scoreRect.topleft = (WINDOWWIDTH - 120, 10) # Places the socre in the topleft and indicates the exact co-ordinates RD
    DISPLAYSURF.blit(scoreSurf, scoreRect) # Moves the score onto another surface RD

def drawWorm(wormCoords): # defines function that draws the worm RD
    for coord in wormCoords: # worm coords is a list of coordinates, the for function  runs the function for every coordinate in the list RD 
        x = coord['x'] * CELLSIZE 
        y = coord['y'] * CELLSIZE
        pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)


def drawApple(coord): # defines Function that draws apple, input is coords which is a list of coordinates RD
    x = coord['x'] * CELLSIZE # Isolates the x cooridinate in the 
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)
def drawGrid(): # defines the function that is used to draw the grid RD
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))
if __name__ == '__main__':
    main()
