import pygame
import sys

def display_menu_window(screen, resolution):

	black = (0, 0, 0)
	green = (50,205,50)
	lime = (0,255,0)
	light = (190, 245, 245)

	screen.fill(light)
	
	# Create the image and buttons.

	image = pygame.image.load("Snake.png")
	image_resolution = (resolution[0] / 2.5, resolution[1] / 1.8)
	image = pygame.transform.scale(image, image_resolution)
	
	screen.blit(image, ((resolution[0] - image_resolution[0]) / 2, 10))

	font_size = 40
	font = pygame.font.SysFont('Arial', font_size)
	text_start = font.render('Start', True , black)
	text_score = font.render('Score', True , black)
	text_quit = font.render('Quit', True , black)

	button_resolution = (150, 50)
	button_pos = []
	button_pos.append(((resolution[0] - button_resolution[0]) / 2, image_resolution[1] + 20))
	button_pos.append(((resolution[0] - button_resolution[0]) / 2, image_resolution[1] + 80))
	button_pos.append(((resolution[0] - button_resolution[0]) / 2, image_resolution[1] + 140))

	pygame.draw.rect(screen, green, [button_pos[0][0], button_pos[0][1], button_resolution[0], button_resolution[1]])
	pygame.draw.rect(screen, green, [button_pos[1][0], button_pos[1][1], button_resolution[0], button_resolution[1]])
	pygame.draw.rect(screen, green, [button_pos[2][0], button_pos[2][1], button_resolution[0], button_resolution[1]])

	while(True):
		for event in pygame.event.get():
			mouse = pygame.mouse.get_pos()

			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN: 
				if (button_pos[0][0] <= mouse[0] <= button_pos[0][0] + button_resolution[0] and 
					button_pos[0][1] <= mouse[1] <= button_pos[0][1] + button_resolution[1]):
					return True
				if (button_pos[1][0] <= mouse[0] <= button_pos[1][0] + button_resolution[0] and 
					button_pos[1][1] <= mouse[1] <= button_pos[1][1] + button_resolution[1]):
					pass
				if (button_pos[2][0] <= mouse[0] <= button_pos[2][0] + button_resolution[0] and 
					button_pos[2][1] <= mouse[1] <= button_pos[2][1] + button_resolution[1]):
					quit()
				
			if (button_pos[0][0] <= mouse[0] <= button_pos[0][0] + button_resolution[0] and 
				button_pos[0][1] <= mouse[1] <= button_pos[0][1] + button_resolution[1]):
				pygame.draw.rect(screen, lime, [button_pos[0][0], button_pos[0][1], button_resolution[0], button_resolution[1]])
			else:
				pygame.draw.rect(screen, green, [button_pos[0][0], button_pos[0][1], button_resolution[0], button_resolution[1]])
				
			if  (button_pos[1][0] <= mouse[0] <= button_pos[1][0] + button_resolution[0] and 
				button_pos[1][1] <= mouse[1] <= button_pos[1][1] + button_resolution[1]):
				pygame.draw.rect(screen, lime, [button_pos[1][0], button_pos[1][1], button_resolution[0], button_resolution[1]])
			else:
				pygame.draw.rect(screen, green, [button_pos[1][0], button_pos[1][1], button_resolution[0], button_resolution[1]])

			if  (button_pos[2][0] <= mouse[0] <= button_pos[2][0] + button_resolution[0] and 
				button_pos[2][1] <= mouse[1] <= button_pos[2][1] + button_resolution[1]):
				pygame.draw.rect(screen, lime, [button_pos[2][0], button_pos[2][1], button_resolution[0], button_resolution[1]])
			else:
				pygame.draw.rect(screen, green, [button_pos[2][0], button_pos[2][1], button_resolution[0], button_resolution[1]])
				
			screen.blit(text_start, (button_pos[0][0] + 25, button_pos[0][1]))
			screen.blit(text_score, (button_pos[1][0] + 20, button_pos[1][1]))
			screen.blit(text_quit, (button_pos[2][0] + 30, button_pos[2][1]))

			pygame.display.update()