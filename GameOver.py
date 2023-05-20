import pygame
import time
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

    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()
