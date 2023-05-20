import pygame
import random
import wall

screenWidth=720
screenHeight=480
# pygame setup
pygame.init()
pygame.display.set_caption('Python101 Snake')
screen = pygame.display.set_mode((screenWidth, screenHeight))
fps = pygame.time.Clock()
running = True

snakeSpeed=3
snake_position = [100, 50]
direction = 'RIGHT'
nextDirection="RIGHT"


#culori
wallColor=pygame.Color(255,0,180)
green = pygame.Color(0, 255, 0)



def drawWall(wall, startPosition):
    #draw all the squares in position as described in the wall variation
    for square in wall:
        pygame.draw.rect(screen, wallColor, pygame.Rect(startPosition[0] + 10*square[0], startPosition[1] + 10*square[1], 10,10))

def readKey():
    global running
    global nextDirection
    # read events and update next direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                nextDirection="UP"
            if event.key == pygame.K_DOWN:
                nextDirection="DOWN"
            if event.key== pygame.K_RIGHT:
                nextDirection="RIGHT"
            if event.key == pygame.K_LEFT:
                nextDirection="LEFT"

def setDirection():
    global direction
    print(nextDirection)
    print(direction)
    if nextDirection=="UP" and direction!="DOWN":
        direction= "UP"
    if nextDirection=="DOWN" and direction!="UP":
        direction=  "DOWN"
    if nextDirection=="RIGHT" and direction!="LEFT":
        direction=  "RIGHT"
    if nextDirection=="LEFT" and direction!="RIGHT":
        direction=  "LEFT"

def updateSnakePosition():
    global direction
    global snake_position
    #updatare pozitie sarpe spre directia de deplasare
    if direction=="RIGHT":
        snake_position[0]+=snakeSpeed
    if direction=="LEFT":
        snake_position[0]-=snakeSpeed
    if direction=="UP":
        snake_position[1]-=snakeSpeed
    if direction=="DOWN":
        snake_position[1]+=snakeSpeed

    #daca sarpele trece de limita ecranului se reintoarce in cealalta parte a ecranului
    #verificare pe axa X
    if snake_position[0]<0:
        snake_position[0]=screenWidth+snake_position[0]
    if snake_position[0]>screenWidth:
        snake_position[0]=snake_position[0]-screenWidth
    #verificare pe axa Y
    if snake_position[1]<0:
        snake_position[1]=screenHeight+snake_position[1]
    if snake_position[1]>screenHeight:
        snake_position[1]=snake_position[1]-screenHeight




while running:
    # poll for events

    
        
    readKey()
    setDirection()

    updateSnakePosition()

    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.rect(screen, green, pygame.Rect(snake_position[0], snake_position[1], 10,10))

    for wallType in wall.variations:
        drawWall(wallType, [40,120 ])
    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.update()
    # pygame.display.flip()

    fps.tick(60)  # limits FPS to 60

pygame.quit()