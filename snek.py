import pygame
import random
import wall
import menu
from snakemodify import snake_modify

screenWidth=720
screenHeight=480
# pygame setup
pygame.init()
pygame.display.set_caption('Python101 Snake')

fps = pygame.time.Clock()
running = False

#initialise snake variables

snakeSpeed=3
snake_position = [100, 50]
snake_body = [[100, 50],
              [80, 50],
              [60, 50],
              [40, 50]
              ]

#initial directions
direction = 'RIGHT'
nextDirection="RIGHT"

#fruit variables initializations
fruit_spawn=False
fruit_position= [random.randrange(1, (720//10)) * 10,
                          random.randrange(1, (480//10)) * 10]
score=0

#colors
wallColor=pygame.Color(0,0,0)
green = pygame.Color(0, 255, 0)
white = pygame.Color(255, 255, 255)

def check_collisions():
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            pygame.quit()
    # Touching a wall
    for wallType in wallObject:
        for square in wall.variations[wallType[0]]:
            if snake_position[0]<= wallType[1] + 10*square[0]+7 and snake_position[0]>= wallType[1] + 10*square[0] -7 and  snake_position[1]<= wallType[2] + 10*square[1]+7 and snake_position[1]>= wallType[2] + 10*square[1] -7:
                print("assasas")
                # pygame.quit()

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

#initialize walls
wallNumber=random.randrange(5,18)
zoneRadiusX=int(screenWidth/wallNumber)
zoneRadiusY=int(screenHeight/wallNumber)
wallObject=[]

for i in range(wallNumber):
    wallObject.append( [ random.randrange(0, len(wall.variations)) , zoneRadiusX*i + random.randrange(-120,120), zoneRadiusY*i + random.randrange(-120,120)  ] )

print(wallObject)

screen = pygame.display.set_mode((1200, 800))
running = menu.display_menu_window(screen, [1200,800])
screen = pygame.display.set_mode((screenWidth, screenHeight))

while running:
    # poll for events

    
        
    readKey()
    setDirection()

    updateSnakePosition()

    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    # pygame.draw.rect(screen, green, pygame.Rect(snake_position[0], snake_position[1], 10,10))

    # draw snake, draw fruit, update score
    [snake_body,snake_position, fruit_position, score, fruit_spawn, screen, white] =snake_modify(snake_body,snake_position, fruit_position,score,fruit_spawn, screen, white )

    for wallType in wallObject:
        drawWall(wall.variations[wallType[0]], [wallType[1],wallType[2] ])
        
    
    check_collisions()
   

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.update()
    # pygame.display.flip()

    fps.tick(60)  # limits FPS to 60

pygame.quit()