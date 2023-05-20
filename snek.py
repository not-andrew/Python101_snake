import pygame

# pygame setup
pygame.init()
pygame.display.set_caption('Python101 Snake')
screen = pygame.display.set_mode((720, 480))
fps = pygame.time.Clock()
running = True

snake_position = [100, 50]
direction = 'RIGHT'
nextDirection="RIGHT"
green = pygame.Color(0, 255, 0)


direction="RIGHT"

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

while running:
    # poll for events

    
        
    readKey()
    setDirection()

    if direction=="RIGHT":
        snake_position[0]+=3
    if direction=="LEFT":
        snake_position[0]-=3
    if direction=="UP":
        snake_position[1]-=3
    if direction=="DOWN":
        snake_position[1]+=3

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.rect(screen, green, pygame.Rect(snake_position[0], snake_position[1], 10,10))

    
    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.update()
    # pygame.display.flip()

    fps.tick(30)  # limits FPS to 60

pygame.quit()