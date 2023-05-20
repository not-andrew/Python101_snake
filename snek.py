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

#wall variables initialization
wallObject=[]
wallSquares=[]
zoneRadiusX=0
zoneRadiusY=0
wallNumber=0

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
            game_over(screen, score)

def reinitialiseVariables():
    global score
    global snake_position
    global snake_body
    global fruit_position
    global fruit_spawn
    score=0
    snake_position = [100, 50]
    snake_body = [[100, 50],
              [80, 50],
              [60, 50],
              [40, 50],
              [20, 50],
              [0, 50]
              ]
    #initialise fruit
    fruit_spawn=False
    fruit_position= [random.randrange(1, (720//10)) * 10,
                          random.randrange(1, (480//10)) * 10]

    #initialize walls
    wallObject.clear()
    wallSquares.clear()
    wallNumber=random.randrange(3,5)
    zoneRadiusX=int(screenWidth/wallNumber)
    zoneRadiusY=int(screenHeight/wallNumber)

    for i in range(wallNumber):
        for j in range(wallNumber):
            wallObject.append( [ random.randrange(0, len(wall.variations)) , zoneRadiusX*i + random.randrange(-100,100), zoneRadiusY*j + random.randrange(-100,100)  ] )

    for wallType in wallObject:
        for square in wall.variations[wallType[0]]:
            wallSquares.append([wallType[1]+ square[0]*10 , wallType[2]+square[1]*10])
    
    
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


def game_over(screen, score):
    screen.fill(pygame.Color(0,0,0))

    game_over_font = pygame.font.SysFont('times new roman', 70)
    game_over_text = game_over_font.render('GAME OVER',True,pygame.Color(255, 255, 255))
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (720 // 2, 480 // 2 - 50)

    score_font = pygame.font.SysFont('times new roman', 40)
    game_over_surface = score_font.render(' Your Score is: ' + str(score), True, pygame.Color(255, 255, 255))
    score_text = score_font.render('Your Score is: ' + str(score), True, pygame.Color(255, 255, 255))
    score_rect = score_text.get_rect()
    score_rect.center = (720 // 2, 480 // 2 + 50)

    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)

    pygame.display.update()
    pygame.time.wait(2000)
    reinitialiseVariables()
    score=0
    running = menu.display_menu_window(screen, [screenWidth,screenHeight])

running = menu.display_menu_window(screen, [screenWidth,screenHeight])

reinitialiseVariables()

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

    #draw wall squares
    drawWall(wallSquares,1)
    
    #check collision with snake body and walls
    check_collisions()
    #display the current score
    show_score(pygame.Color(255,255,255),pygame.Color(0,0,0), 'times new roman', 20, screen, score)

    # RENDER YOUR GAME HERE

    # update the screen
    pygame.display.update()

    fps.tick(30)  # limits FPS to 30

pygame.quit()