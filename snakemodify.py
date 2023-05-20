import pygame
import random
def snake_modify(snake_body,snake_position, fruit_position, score, fruit_spawn, screen, green, notlist):
    k=1
    snake_body.insert(0, list(snake_position))
    if fruit_spawn == False:
        fruit_position = [random.randrange(23, (720//10)) * 10,
                          random.randrange(67, (480//10)) * 10]
    if snake_position[0] <= fruit_position[0] + 5 and snake_position[0] >= fruit_position[0] - 5 and snake_position[1] <= fruit_position[1] + 5 and snake_position[1] >= fruit_position[1] - 5:
        score = score + 10
        fruit_spawn = False
    else:
        snake_body.pop()
    if fruit_spawn == False:
        while k==1: 
            fruit_position = [random.randrange(1, (720//10)) * 10,
                          random.randrange(1, (480//10)) * 10]
            k=1
            for i in notlist:
                if  not(fruit_position[0] >=i[0] - 7 and  fruit_position[0] <= i[0] + 7 and fruit_position[1] >=i[1] - 7 and  fruit_position[1] <= i[1] + 7):
                    k=0
        
    fruit_spawn = True
    screen.fill(pygame.Color(15, 59, 28))
    
    for pos in snake_body:
        pygame.draw.rect( screen, green, pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(screen, pygame.Color(255,0,0), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    return snake_body,snake_position, fruit_position, score, fruit_spawn, screen, green
