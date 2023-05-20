import pygame

def display_leaderboard(screen, resolution):
	
	white = (255, 255, 255)
	yellow = (255, 191, 0)
	light_yellow = (255, 234, 0)
	light = (190, 245, 245)

	screen.fill(light)

	font = pygame.font.SysFont('Arial', 50)
	text_leaderboard = font.render('Leaderboard', True , yellow)
	screen.blit(text_leaderboard, (120, 40))

	font = pygame.font.SysFont('Arial', 40)
	text_menu = font.render('Menu', True , white)

	image_resolution = (100, 50)
	image = pygame.image.load("Crown.png")
	image = pygame.transform.scale(image, image_resolution)
	screen.blit(image, (500, 40))

	button_resolution = (150, 50)
	button_pos = ((resolution[0] - button_resolution[0]) / 2, 400)

	

	height = 120
	file = open("score.in", "r")
	for player in range(5):
		
		name = file.readline()
		score = file.readline()
		
		text_player = font.render(score + " --- " + name, True , yellow)
		screen.blit(text_player, (150, height))
		height += 50

	
	while(True):
		for event in pygame.event.get():
			mouse = pygame.mouse.get_pos()

			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN: 
				if (button_pos[0] <= mouse[0] <= button_pos[0] + button_resolution[0] and 
					button_pos[1] <= mouse[1] <= button_pos[1] + button_resolution[1]):
					return

		if (button_pos[0] <= mouse[0] <= button_pos[0] + button_resolution[0] and 
			button_pos[1] <= mouse[1] <= button_pos[1] + button_resolution[1]):
			pygame.draw.rect(screen, light_yellow, [button_pos[0], button_pos[1], button_resolution[0], button_resolution[1]])
		else:
			pygame.draw.rect(screen, yellow, [button_pos[0], button_pos[1], button_resolution[0], button_resolution[1]])

		screen.blit(text_menu, (button_pos[0] + 20, button_pos[1]))

		pygame.display.update()