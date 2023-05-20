import pygame
def show_score(score_color, background_color, font, size, screen, score):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render('Score: ' + str(score), True, score_color)
    score_obj = score_surface.get_rect()
    print (score_surface.get_height())
    score_background = pygame.Surface((score_surface.get_width() + 5,score_surface.get_height() + 5))
    score_background.fill(background_color)
    pygame.draw.rect(score_background, pygame.Color(255,255,255), score_background.get_rect(), 2)
    screen.blit(score_background, (0, 0))
    screen.blit(score_surface, score_obj)
