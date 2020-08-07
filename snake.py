import pygame
import time
import random
pygame.init()
clock = pygame.time.Clock()

display_width = 500
display_height = 500
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('Snake Game')

snake_size = 10
snake_speed = 15
def snake(snake_body, snake_size):
	for cell in snake_body:
		pygame.draw.rect(win,(0,255,0),(cell[0], cell[1], snake_size, snake_size))

def game():
	x = display_width/2
	y = display_height/2

	x1 = y1 = 0
	run = True
	game_end = False

	snake_body = []
	snake_length = 1

	food_x = round(random.randrange(0, display_width - snake_size)/10.0) *10.0
	food_y = round(random.randrange(0, display_height - snake_size)/10.0) *10.0
	while run:
		while game_end == True:
			score = snake_length-1
			score_font = pygame.font.SysFont("comicsansms", 35)
			value = score_font.render("Your Score: "+str(score), True, (0,255,0))
			win.blit(value, (display_width/3, display_height/5))
			msg = score_font.render("Press P to play again", True, (255, 0, 0))
			win.blit(msg, (display_width/3, display_height/3))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					game_end = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						game()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x1 = -snake_size
					y1 = 0
				elif event.key == pygame.K_RIGHT:
					x1 = snake_size
					y1 = 0
				elif event.key == pygame.K_UP:
					y1 = -snake_size
					x1 = 0
				elif event.key == pygame.K_DOWN:
					y1 = snake_size
					x1 = 0

		if x>= display_width or x<0 or y>=display_height or y<0:
			game_end = True

		x += x1
		y += y1
		win.fill((0,0,0))
		pygame.draw.rect(win, (0,0,255), (food_x, food_y, snake_size, snake_size))
		snake_cell=[]
		snake_cell.append(x)
		snake_cell.append(y)
		snake_body.append(snake_cell)

		if len(snake_body)>snake_length:
			del snake_body[0]

		for cell in snake_body[:-1]:
			if cell == snake_cell:
				game_end = True

		snake(snake_body, snake_size)
		pygame.display.update()

		if x == food_x and y == food_y:
			food_x = round(random.randrange(0, display_width - snake_size)/10.0) *10.0
			food_y = round(random.randrange(0, display_height - snake_size)/10.0) *10.0
			snake_length += 1

		clock.tick(snake_speed)

	pygame.quit()
	quit()


game()
"""def update_screen():
	win.fill((0,0,0))
	pygame.draw.rect(win, (0,0,255), (x,y,snake_size,snake_size))
	pygame.display.update()"""
