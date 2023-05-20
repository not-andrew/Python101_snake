import pygame
import random
def snake_modify(snake_body,snake_position, fruit_position, score, fruit_spawn, screen, green):
    snake_body.insert(0, list(snake_position))
    if snake_position[0] <= fruit_position[0] + 5 and snake_position[0] >= fruit_position[0] - 5 and snake_position[1] <= fruit_position[1] + 5 and snake_position[1] >= fruit_position[1] - 5:
        score = score + 10
        fruit_spawn = False
        print("DA")
        
    else:
        snake_body.pop()
    
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (720//10)) * 10,
                          random.randrange(1, (480//10)) * 10]
        
    fruit_spawn = True
    screen.fill("purple")
    
    for pos in snake_body:
        pygame.draw.rect( screen, green, pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(screen, green, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    return snake_body,snake_position, fruit_position, score, fruit_spawn, screen, green
