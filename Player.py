import pygame
import os  
import time
import random
import math
from Platform import Platform

Floor = pygame.image.load("Assets/Floor.png")
Width, Height = (1280, 720)





class Player():


    def __init__(self, number, x, y, health, skin, name, color):
        self.number = number
        self.x = x
        self.y = y
        self.health = health
        self.skin = skin
        self.name = name
        self.color = color
        self.image = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{skin}.png"), (75, 100))
        # self.HUD = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{color}.png"), (120, 150))
        self.image_points_left = False
        # Now we make a mask of the self, the mask built into pygame makes it so that when the image collides with something its not the entire file that colides its the actual image.
        self.max_health = health
        self.current_animation = "middle"
        self.velocity = 15
        self.lives = 5   

        self.gravity = 0.8
        self.jump_count = -16
        self.is_jump = True

        self.direction = pygame.math.Vector2(0,0)



        self.left_key = pygame.K_a
        self.right_key = pygame.K_d
        self.up_key = pygame.K_w
        self.down_key = pygame.K_s
        self.jump_key = pygame.K_SPACE


        self.rect = pygame.Rect(self.x, self.y , 75, 100)        

        




    def draw(self,screen):
        screen.blit(self.image, (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y , 75, 100)


        # if self.y < 900: 
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)




    def flip_character(self,type_of_flip):
        if type_of_flip == "left":
            if not self.image_points_left:
                self.image = pygame.transform.flip(self.image, True, False)
                self.image_points_left = not self.image_points_left
        else:
            if self.image_points_left:
                self.image = pygame.transform.flip(self.image, True, False)
                self.image_points_left = not self.image_points_left


    def playeranimation(self, type_of_flip, screen):

        if type_of_flip == "left":
            if self.current_animation == "middle":
                self.image = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{self.skin}right.png"), (75, 100))
                self.image = pygame.transform.flip(self.image, True, False)
                screen.blit(self.image,(self.x, self.y))  
                self.current_animation = "right"

            elif self.current_animation == "right":
                self.image = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{self.skin}left.png"), (75, 100))
                self.image = pygame.transform.flip(self.image, True, False)
                screen.blit(self.image,(self.x, self.y))
                self.current_animation = "left"

            elif self.current_animation == "left":
                self.image = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{self.skin}.png"), (75, 100))
                self.image = pygame.transform.flip(self.image, True, False)
                screen.blit(self.image,(self.x, self.y))
                self.current_animation = "middle"

        else: 
            if self.current_animation == "middle":
                self.image = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{self.skin}right.png"), (75, 100))
                screen.blit(self.image,(self.x, self.y))  
                self.current_animation = "right"

            elif self.current_animation == "right":
                self.image = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{self.skin}left.png"), (75, 100))
                screen.blit(self.image,(self.x, self.y))
                self.current_animation = "left"

            elif self.current_animation == "left":
                self.image = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{self.skin}.png"), (75, 100))
                screen.blit(self.image,(self.x, self.y))
                self.current_animation = "middle"

    def movement(self, screen):

        keys = pygame.key.get_pressed()

        if self.name == "LRUD":
            self.left_key = pygame.K_LEFT
            self.right_key = pygame.K_RIGHT
            self.up_key = pygame.K_UP
            self.down_key = pygame.K_DOWN


        if keys[self.left_key] and self.x - self.velocity + (self.velocity / 2) > 0: 
            self.flip_character("left")
            self.x -= self.velocity
            self.direction.x -= self.velocity




        if keys[self.right_key] and self.x + self.velocity + self.image.get_width() - 10 < Width:
            self.flip_character("right")
            self.x += self.velocity
            self.direction.x += self.velocity

        if self.direction.y < 0:
            self.image = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{self.skin}.png"), (75, 100))

        else:

            self.image = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{self.skin}fall.png"), (75, 100))





        # if self.is_jump == True:
        #     self.is_jump = False


        # if keys[self.jump_key] or keys[self.up_key]:
        #     self.y = self.y - 5 
        #     self.direction.y = self.jump_count
        #     self.is_jump = True
 
        # # if not self.is_jump: 
        #     if keys[self.jump_key] or keys[self.up_key]:

        #         self.is_jump = True
        #         print (self.jump_count)

        

            if keys[self.left_key]:
                self.image = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{self.skin}.png"), (75, 100))

                self.flip_character("right")
                screen.blit(self.image, (self.x, self.y))

            elif keys[self.right_key]:
                self.image = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{self.skin}.png"), (75, 100))
                screen.blit(self.image, (self.x, self.y))

            # if self.jump_count >= -10:
            #     self.y -= (self.jump_count * abs(self.jump_count)) * 0.5
            #     print (self.jump_count)
            #     self.jump_count -= 1
            # else: 
            #     self.jump_count = 10
            #     self.is_jump = False

        # self.direction.y += self.gravity
        # self.y += self.direction.y


    def firsty(self):
        self.FirstY = self.y

    def CoordsCalculationP(self):

        self.topleftx = self.x
        self.toplefty = self.y
        self.toprightx = self.x + self.image.get_width()
        self.toprighty = self.y
        self.bottomrighty = self.y + self.image.get_height()
        self.bottomrightx = self.x + self.image.get_width()
        self.bottomlefty = self.y + self.image.get_height()
        self.bottomleftx = self.x
   

    def Gravity(self):


        self.direction.y += self.gravity
        self.y += self.direction.y




    def player_collision(self, platforms):



        for platform in platforms:

            if self.bottomleftx < platform.toprightx and self.bottomleftx > platform.topleftx and self.bottomlefty < platform.toplefty and self.bottomlefty > platform.toplefty:


                self.direction.y = 0 

                self.bottomlefty = platform.toplefty

                print("genius")