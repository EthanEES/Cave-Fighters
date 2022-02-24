import pygame
import os  
import random
from Player import Player
from Platform import Platform
from Hole import Hole




class Game():


	def __init__(self, player, player2, Floorect):
		self.PlatformArray = []
		self.HoleArray = []
		self.PlayerArray = [player, player2]
		self.PlatformCounter = 0
		self.HoleCounter = 0
		self.RightThresh = 0
		self.LeftThresh = 0
		self.LeftDeath = pygame.Rect(0, 0 , 10, 720)



	def Death(self, screen):
		pygame.draw.rect(screen, (255, 225, 225), self.LeftDeath)


	def HoleGeneration(self):
		y = Hole()
		self.HoleArray.append(y)
		self.LeftThresh = random.randint(0, 1280)

	def HoleCheck(self, screen):
		if self.HoleArray[self.HoleCounter].toprightx < self.LeftThresh:
			self.HoleGeneration()
			self.HoleArray[self.HoleCounter].RenderHole(screen)
			self.HoleCounter += 1

		print(self.HoleCounter)



	def PlatformGeneration(self):
		x = Platform()
		self.PlatformArray.append(x)
		self.RightThresh = random.randint(600, 1280)


	def PlatformCheck(self, screen, player, player2, Floorect):
	
		keys = pygame.key.get_pressed()

		if self.PlatformArray[self.PlatformCounter].toprightx < self.RightThresh:
			self.PlatformGeneration()
			self.PlatformArray[self.PlatformCounter].RenderPlatform(screen)
			self.PlatformCounter += 1




		for platform in self.PlatformArray:
			for player in self.PlayerArray:
				if player.rect.colliderect(platform.rect):
					if player.rect.bottom >= platform.rect.top:
						player.rect.bottom = platform.rect.top
						player.direction.y = -20

					elif player.rect.top <= platform.rect.bottom:
						player.rect.top = platform.rect.bottom
						player.direction.y = 0

					elif player.rect.right >= platform.rect.left:
						player.rect.right = platform.rect.left 
						player.direction.x = 0

					else:
						player.rect.left = platform.rect.right
						player.direction.x = 0
						print("working")

		for hole in self.HoleArray:
			for player in self.PlayerArray:
				if player.rect.colliderect(hole.rect):
					if player.rect.bottom >= hole.rect.top:
						player.rect.bottom = hole.rect.top
						player.direction.y = -20

					elif player.rect.top <= hole.rect.bottom:
						player.rect.top = hole.rect.bottom
						player.direction.y = 0

					elif player.rect.right >= hole.rect.left:
						player.rect.right = hole.rect.left 
						player.direction.x = 0

					else:
						player.rect.left = hole.rect.right
						player.direction.x = 0
						print("working")


		# for platform in self.PlatformArray:
		# 	for player in self.PlayerArray:
		# 		if player.rect.colliderect(platform.rect):
		# 			if player.rect.bottom > platform.rect.top and player.rect.bottom < platform.rect.bottom:
		# 				player.gravity = 0
		# 				player.direction.y = 0
		# 				player.bottomrighty = platform.toprighty
		# 				player.is_jump = False
						
		# 				print("on top")

		# 			elif player.rect.top < platform.rect.bottom and player.rect.top > platform.rect.top:
		# 				player.gravity = 0
		# 				player.direction.y = 0
		# 				player.rect.top = platform.rect.bottom
		# 				print("on bottom")

		# 			elif player.rect.right >= platform.rect.left:
		# 				player.rect.right = platform.rect.left 
		# 				player.direction.x = 0

		# 			else:
		# 				player.rect.left = platform.rect.right
		# 				player.direction.x = 0
		# 				print("working")

		# 		else:
		# 			player.gravity = 0.8










		# # for player in self.PlayerArray:
		# # 	if not player.rect.colliderect(Floorect) or not player.rect.colliderect(Floorect):
		# # 		player.gravity = 0.8

		# # 	elif player.rect.colliderect(Floorect) or player.rect.colliderect(Floorect):
		# # 		if player.direction.y > 0:
		# # 			player.gravity = 0
		# # 			player.direction.y = 0
		# # 			player.rect.bottom = Floorect.top
		# # 			print("heyyy")



					


		# 		elif player.direction.y < 0:
		# 			player.rect.top = Floorect.bottom					


		# for platform in self.PlatformArray:
		# 	for player in self.PlayerArray:
		# 		if not player.rect.colliderect(platform.rect):
		# 			player.direction.y += player.gravity
		# 			player.y = player.direction.y

		# 			print ("hi")


	# def colllision(self, Floorect):



		# for platform in self.PlatformArray:
		# 	for player in self.PlayerArray:
		# 		if player.rect.colliderect(platform.rect):
		# 			if player.direction.x < 0:
		# 				player.rect.left = platform.rect.right
		# 				player.direction.x = 0

		# # 			elif player.direction.x > 0:
		# 				player.rect.right = platform.rect.left
		# 				player.direction.x = 0

				


		# for platform in self.PlatformArray:
		# 	for player in self.PlayerArray:

		# 		print(player.jump_count)
		# 		print(player.direction.y)
		# 		print(player.gravity)
					

		# 		if player.rect.collidepoint(platform.toprightx, ):
		# 			if player.direction.y > 0:
		# 				player.bottomlefty = platform.toprighty
		# 				player.direction.y = 0
		# 				player.gravity = 0

		# 			elif player.direction.y < 0:
		# 				player.rect.top = platform.rect.bottom

		# 		elif Floorect.collidepoint(player.rect.bottom):
		# 			if player.direction.y > 0:
		# 				player.bottomrighty = Floorect.top
		# 				player.direction.y = 0
		# 				print("id")

		# 		else:
		# 			player.gravity = 0.8
		# 			player.direction.y += player.gravity
		# 			player.y += player.direction.y

