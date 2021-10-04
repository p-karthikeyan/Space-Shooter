# SPACE SHOOTER #

import pygame
import random 
import math
from pygame import mixer
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Space Shooter")

icon = pygame.image.load('launch.png')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('ufo.png')
playerimg = pygame.transform.scale(playerimg, (90,90))
playerX = 370
playerY = 480
playerX_change = 0

alienimg = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
no_of_aliens = 6

alien = pygame.image.load('alien.png')
alien = pygame.transform.scale(alien, (60,60))

mixer.music.load('bgmusic.mp3')
mixer.music.play(-1)

for i in range(no_of_aliens):
	alienimg.append(alien)	
	alienX.append(random.randint(0,740))
	alienY.append(random.randint(50,150))
	alienX_change.append(1)
	alienY_change.append(40)

buletimg = pygame.image.load('bulet.png')
buletimg = pygame.transform.scale(buletimg, (30,30))
buletX = 0
buletY = 480
buletX_change = 0
buletY_change = 10
bulet_state = "ready"

SCORE = 0
font = pygame.font.Font('freesansbold.ttf',20)
textX=10
textY=10

background = pygame.image.load('space.png')
background = pygame.transform.scale(background,(800,600))

running = True
def score(x,y):
	Score = font.render("Score : "+str(SCORE),True,(62, 79, 107))
	screen.blit(Score,(x,y))
def collide(alienX,alienY,buletX,buletY):
	distances = math.sqrt((math.pow(buletX-alienX,2))+(math.pow(buletY-alienY,2)))
	if distances <=20 :
		return True
	else:
		return False
def on_fire(x,y):
	global bulet_state
	bulet_state = "fire"
	screen.blit(buletimg,(x+30,y+20))
def bg():
	screen.blit(background,(0,0))
def player(x,y):
	screen.blit(playerimg,(x,y))
def alien(x,y,i):
	screen.blit(alienimg[i],(x,y))

while running:
	screen.fill((0,0,20))	
	bg()
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
			elif event.key == K_LEFT:
				playerX_change = -2
			elif event.key == K_RIGHT:
				playerX_change = 2 
			elif event.key == K_SPACE:
				if bulet_state is "ready":
					on_fire(playerX,buletY)
					buletX = playerX
					shoot_sound = mixer.Sound('Gun Shot.mp3')
					shoot_sound.play()

		if event.type == KEYUP:
			if event.key == K_LEFT or event.key == K_RIGHT:
				playerX_change = 0
		elif event.type == QUIT:
			running = False

	playerX += playerX_change
	if playerX <=0 :
		playerX = 0
	elif playerX >=710 :
		playerX =710 
	player(playerX,playerY)
	
	for i in range(no_of_aliens):
		alienX[i] += alienX_change[i]	
		if alienX[i] <=0 :
			alienX_change[i] = 1
			alienY[i] += alienY_change[i]
		elif alienX[i] >=740 :
			alienX_change[i] = -1
			alienY[i] += alienY_change[i]
		colide = collide(alienX[i],alienY[i],buletX,buletY)
		if colide:
			buletY = 480
			bulet_state = "ready"
			SCORE += 1
			alienX[i] = random.randint(0,740)
			alienY[i] = random.randint(50,150)
			dead = mixer.Sound('death.mp3')
			dead.play()
		alien(alienX[i],alienY[i],i)
	score(textX,textY)
		
	if buletY <=0 :
		buletY = 480
		bulet_state = "ready"
	if bulet_state is "fire":
		on_fire(buletX,buletY)
		buletY -= buletY_change
	
	pygame.display.update()

pygame.quit()

