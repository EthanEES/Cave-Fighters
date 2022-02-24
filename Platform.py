import pygame
import os  
import time
import random

Width, Height = (1280, 720)


class Platform():

	def __init__(self):

		self.x  = random.randint(1300, 1400)
		self.y = random.randint(150, 500)
		self.xright = random.randint(1380, 1500)
		self.yright = random.randint(100, 450)
		self.width = random.randint(150, 300)
		self.image = pygame.transform.scale(pygame.image.load("Assets/Platform.png"), (self.width, 50))
		self.height = self.image.get_height()
		

		
		self.CoordsCalculation()

		self.rect = pygame.Rect(self.x, self.y , self.width, 50)


	def RenderPlatform(self, screen):

		self.rect = pygame.Rect(self.x, self.y , self.width, 50)
		screen.blit(self.image, (self.x, self.y))
		pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)




	def CoordsCalculation(self):

		self.topleftx = self.x
		self.toplefty = self.y
		self.toprightx = self.x + self.image.get_width()
		self.toprighty = self.y
		self.bottomrighty = self.y + self.image.get_height()
		self.bottomrightx = self.x + self.image.get_width()
		self.bottomlefty = self.y + self.image.get_height()
		self.bottomleftx = self.x








