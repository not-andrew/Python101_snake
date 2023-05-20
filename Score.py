import pygame
def show_score(score_color, background_color, font, size, screen, score, width, height, posx, posy):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render('Score: ' + str(score), True, score_color)
    score_obj = score_surface.get_rect()
    print (score_surface.get_height())
    score_background = pygame.Surface((score_surface.get_width(),score_surface.get_height()))
    score_background.fill(background_color)
    screen.blit(score_background, (posx, posy))
    screen.blit(score_surface, score_obj)
