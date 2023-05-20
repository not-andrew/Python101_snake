import pygame
import random
import wall
import menu
from snakemodify import snake_modify
from Score import show_score

screenWidth=720
screenHeight=480
# pygame setup
pygame.init()
pygame.display.set_caption('Python101 Snake')
screen = pygame.display.set_mode((screenWidth, screenHeight))
fps = pygame.time.Clock()
running = False

#initialise wall variables
wallSquares=[]
wallObject=[]

#initialise snake variables

snakeSpeed=5
snake_position = [100, 50]
snake_body = [[100, 50],
              [80, 50],
              [60, 50],
              [40, 50],
              [20, 50],
              [0, 50]
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
    for square in wallSquares:
        if snake_position[0]<= square[0]+10 and snake_position[0]>= square[0] -10 and  snake_position[1]<= square[1]+10 and snake_position[1]>=square[1] -10:
            print("assasas")
            pygame.quit()

def drawWall(wall, startPosition):
    #draw all the squares in position as described in the wall variation
    for square in wall:
        pygame.draw.rect(screen, wallColor, pygame.Rect(square[0], square[1], 10,10))

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
            if event.key == pygame.K_ESCAPE:
                running = menu.display_menu_window(screen, [screenWidth,screenHeight])

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
wallNumber=random.randrange(3,5)
zoneRadiusX=int(screenWidth/wallNumber)
zoneRadiusY=int(screenHeight/wallNumber)

for i in range(wallNumber):
    for j in range(wallNumber):
        wallObject.append( [ random.randrange(0, len(wall.variations)) , zoneRadiusX*i + random.randrange(-100,100), zoneRadiusY*j + random.randrange(-100,100)  ] )




for wallType in wallObject:
    for square in wall.variations[wallType[0]]:
        wallSquares.append([wallType[1]+ square[0]*10 , wallType[2]+square[1]*10])
# wallSquares=[[wallType[1]+ square[0]*10 , wallType[2]+square[1]*10]  for square in wall.variations[wallType[0]] for wallType in wallObject ]
print(wallSquares)


running = menu.display_menu_window(screen, [screenWidth,screenHeight])


while running:
    # poll for events

    
        
    readKey()
    setDirection()

    updateSnakePosition()

    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(pygame.Color(15, 59, 28))
    # pygame.draw.rect(screen, green, pygame.Rect(snake_position[0], snake_position[1], 10,10))

    # draw snake, draw fruit, update score
    [snake_body,snake_position, fruit_position, score, fruit_spawn, screen, white] =snake_modify(snake_body,snake_position, fruit_position,score,fruit_spawn, screen, white, wallSquares )

    # for wallType in wallObject:
    #     drawWall(wall.variations[wallType[0]], [wallType[1],wallType[2] ])
    drawWall(wallSquares,1)
    
    
    check_collisions()
    show_score(pygame.Color(255,255,255),pygame.Color(0,0,0), 'times new roman', 20, screen, score)


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.update()
    # pygame.display.flip()

    fps.tick(30)  # limits FPS to 60

pygame.quit()