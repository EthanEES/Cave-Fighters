import pygame
import os  
import time
import random

#Initalize the game and its properties
pygame.font.init()
pygame.init()



Width, Height = (1280, 720)
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Ice Cave")



# Loading Images/Sprites

Background = pygame.transform.scale(pygame.image.load("Assets/BAckground.png"), (Width, Height))
Background = pygame.transform.flip(Background, True, False)
Background2 = pygame.transform.scale(pygame.image.load("Assets/BAckground.png"), (Width, Height))
Background2 = pygame.transform.flip(Background2, True, False)
Background3 = pygame.transform.scale(pygame.image.load("Assets/BAckground.png"), (Width, Height))
Background3 = pygame.transform.flip(Background3, True, False)


Floor = pygame.image.load("Assets/Floor.png")
Platform = pygame.transform.scale(pygame.image.load("Assets/Platform.png"), (300, 50))

Penguin = pygame.transform.scale(pygame.image.load("Assets/Blue.png"), (75, 100))
Penguin2 = pygame.transform.scale(pygame.image.load("Assets/Purple.png"), ((75, 100)))

Fog = pygame.transform.scale(pygame.image.load("Assets/fog.png"), (Width, Height))

Torch = pygame.image.load("Assets/Torch.png")
Torch = pygame.transform.scale(pygame.image.load("Assets/Torch.png"), (350, 350))

pygame.mixer.music.load("Assets/Background.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0)
















class Enemy:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.image = None

 
    def draw(self,screen):
            screen.blit(self.image, (self.x, self.y))

class Player1(Enemy):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.image = Penguin
        self.image_points_left = False
        # Now we make a mask of the player, the mask built into pygame makes it so that when the image collides with something its not the entire file that colides its the actual image.
        self.mask = pygame.mask.from_surface(self.image)
        self.max_health = health
        self.current_animation = "middle"   


    def flip_character(self,type_of_flip):
        if type_of_flip == "left":
            if not self.image_points_left:
                self.image = pygame.transform.flip(self.image, True, False)
                self.image_points_left = not self.image_points_left
        else:
            if self.image_points_left:
                self.image = pygame.transform.flip(self.image, True, False)
                self.image_points_left = not self.image_points_left


    def playeranimation(self, type_of_flip):

        if type_of_flip == "left":
            if self.current_animation == "middle":
                self.image = pygame.transform.scale(pygame.image.load("Assets/Playerright.png"), (75, 100))
                self.image = pygame.transform.flip(self.image, True, False)
                screen.blit(self.image,(self.x, self.y))  
                self.current_animation = "right"

            elif self.current_animation == "right":
                self.image = pygame.transform.scale(pygame.image.load("Assets/Playerleft.png"), (75, 100))
                self.image = pygame.transform.flip(self.image, True, False)
                screen.blit(self.image,(self.x, self.y))
                self.current_animation = "left"

            elif self.current_animation == "left":
                self.image = pygame.transform.scale(pygame.image.load("Assets/Blue.png"), (75, 100))
                self.image = pygame.transform.flip(self.image, True, False)
                screen.blit(self.image,(self.x, self.y))
                self.current_animation = "middle"

        else: 
            if self.current_animation == "middle":
                self.image = pygame.transform.scale(pygame.image.load("Assets/Playerright.png"), (75, 100))
                screen.blit(self.image,(self.x, self.y))  
                self.current_animation = "right"

            elif self.current_animation == "right":
                self.image = pygame.transform.scale(pygame.image.load("Assets/Playerleft.png"), (75, 100))
                screen.blit(self.image,(self.x, self.y))
                self.current_animation = "left"

            elif self.current_animation == "left":
                self.image = pygame.transform.scale(pygame.image.load("Assets/Blue.png"), (75, 100))
                screen.blit(self.image,(self.x, self.y))
                self.current_animation = "middle"


            







class Player2(Enemy):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.image = Penguin2
        self.image_points_left = False
        # Now we make a mask of the player, the mask built into pygame makes it so that when the image collides with something its not the entire file that colides its the actual image.
        self.mask = pygame.mask.from_surface(self.image)
        self.max_health = health
        self.current_animation = "middle"

    def flip_character(self,type_of_flip):
        if type_of_flip == "left":
            if not self.image_points_left:
                self.image = pygame.transform.flip(self.image, True, False)
                self.image_points_left = not self.image_points_left
        else:
            if self.image_points_left:
                self.image = pygame.transform.flip(self.image, True, False)
                self.image_points_left = not self.image_points_left


    def playeranimation(self, type_of_flip):

        if type_of_flip == "left" :
            if self.current_animation == "middle":
                self.image = pygame.transform.scale(pygame.image.load("Assets/Player2right.png"), ((75, 100)))
                self.image = pygame.transform.flip(self.image, True, False)
                screen.blit(self.image,(self.x, self.y))  
                self.current_animation = "right"

            elif self.current_animation == "right":
                self.image = pygame.transform.scale(pygame.image.load("Assets/Player2left.png"), ((75, 100)))
                self.image = pygame.transform.flip(self.image, True, False)
                screen.blit(self.image,(self.x, self.y))
                self.current_animation = "left"

            elif self.current_animation == "left":
                self.image = pygame.transform.scale(pygame.image.load("Assets/Purple.png"), ((75, 100)))
                self.image = pygame.transform.flip(self.image, True, False)
                screen.blit(self.image,(self.x, self.y))
                self.current_animation = "middle"

        else: 
            if self.current_animation == "middle":
                self.image = pygame.transform.scale(pygame.image.load("Assets/Player2right.png"), ((75, 100)))
                screen.blit(self.image,(self.x, self.y))  
                self.current_animation = "right"

            elif self.current_animation == "right":
                self.image = pygame.transform.scale(pygame.image.load("Assets/Player2left.png"), ((75, 100)))
                screen.blit(self.image,(self.x, self.y))
                self.current_animation = "left"

            elif self.current_animation == "left":
                self.image = pygame.transform.scale(pygame.image.load("Assets/Purple.png"), ((75, 100)))
                screen.blit(self.image,(self.x, self.y))
                self.current_animation = "middle"












def properties():
    run = True
    FPS = 60

    level = 1
    lives = 5
    player_velocity = 15

    randheight = random.randint(349, 350)
    randwidth = random.randint(30, 1170)
    randheight2 = random.randint(349, 350)
    randwidth2 = random.randint(30, 1170)

    main_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 20)
    clock = pygame.time.Clock()

    player = Player1(550, 545)
    player2 = Player2(700, 545)


        # Blue positions

    Penguin_topleft = player.x
    Penguin_topright = player.x + Penguin.get_width()
    Penguin_bottomright = Penguin_topright + Penguin.get_height()
    Penguin_bottomleft = player.y + Penguin.get_height()







    is_Jump = False
    jumpCount = 10

    is_Jump2 = False
    jumpCount2 = 10

    Background_placement = 0
        

    def game():

        # Placing the images in the game 
        
        screen.blit(Floor,(0,900))
        


        lives_label = main_font.render(f"Lives: {lives}", 1, (0, 0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (0, 0, 0))
        FPS_label = main_font.render(f"FPS: {FPS}", 1, (0, 0, 0))


        screen.blit(level_label, (10, 10))
        screen.blit(lives_label, (20 + level_label.get_width(), 10))
        screen.blit(FPS_label, (25 + level_label.get_width() + lives_label.get_width(), 10))

      

        screen.blit(Torch, (player.x - 120 , player.y - 120 ))
        screen.blit(Torch, (player2.x - 120 , player2.y - 120 ))
        
        
        player.draw(screen)
        player2.draw(screen)

        # Flip the display
        pygame.display.flip()
        pygame.display.update()




    while run:
        clock.tick(FPS)
        game()

        # Checks if the user clicked the close button, if so end loop/ close game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



        # Assigning keys in pygame

        #========================PLAYER 1=============================

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and player.x - player_velocity + (player_velocity / 2) > 0: 
            player.flip_character("left")
            player.x -= player_velocity

            if is_Jump == False:
                player.playeranimation("left")


        if keys[pygame.K_d] and player.x + player_velocity + Penguin.get_width() - 10 < Width:
            player.flip_character("right")
            player.x += player_velocity

            if is_Jump == False:
                player.playeranimation("right")


        if keys[pygame.K_s] and player.y + player_velocity + 50 < Height - Floor.get_height() and not is_Jump: 
            player.y += player_velocity


        if not is_Jump: 
            if keys[pygame.K_SPACE] or keys[pygame.K_w]:
                is_Jump = True

        else:
            if keys[pygame.K_a]:
                player.image = pygame.transform.scale(pygame.image.load("Assets/Blue.png"), (75, 100))
                player.flip_character("right")
                screen.blit(player.image, (player.x, player.y))

            elif keys[pygame.K_d]:
                player.image = pygame.transform.scale(pygame.image.load("Assets/Blue.png"), (75, 100))
                screen.blit(player.image, (player.x, player.y))

            if jumpCount >= -10:
                player.y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else: 
                jumpCount = 10
                is_Jump = False




        #========================PLAYER 2=============================

        if keys[pygame.K_LEFT] and player2.x - player_velocity + (player_velocity / 2) > 0: 
            player2.flip_character("left")
            player2.x -= player_velocity

            if is_Jump2 == False:
                player2.playeranimation("left")

        if keys[pygame.K_RIGHT] and player2.x + player_velocity + Penguin2.get_width() < Width:
            player2.flip_character("right")
            player2.x += player_velocity

            if is_Jump2 == False:
                player2.playeranimation("right")

        if keys[pygame.K_DOWN] and player2.y + player_velocity + 50 < Height - Floor.get_height() and not is_Jump2: 
            player2.y += player_velocity


        if not is_Jump2: 
            if keys[pygame.K_UP]:
                is_Jump2 = True

        else:

            if keys[pygame.K_LEFT]:
                player2.image = pygame.transform.scale(pygame.image.load("Assets/Purple.png"), ((75, 100)))
                player2.flip_character("right")
                screen.blit(player2.image, (player2.x, player2.y))

            elif keys[pygame.K_RIGHT]:
                player2.image = pygame.transform.scale(pygame.image.load("Assets/Purple.png"), ((75, 100)))
                screen.blit(player2.image, (player2.x, player2.y))


            if jumpCount2 >= -10:
                player2.y -= (jumpCount2 * abs(jumpCount2)) * 0.5
                jumpCount2 -= 1
            else: 
                jumpCount2 = 10
                is_Jump2 = False



        #========================Parallax Background=============================

    
        screen.blit(Background, (Background_placement, 0))
        screen.blit(Background2, (Background_placement + 1270, 0))
        screen.blit(Background3, (Background_placement - 1270, 0))

        if Background_placement - 1450 < -2720:
            Background_placement = 0

        elif Background_placement > 1270:
            Background_placement = 0



            # If the Blue 1 is hugging right wall and left wall
       



        if player.x + 100 > 1270 and player2.x > 50 and keys[pygame.K_d]:
            Background_placement -= 13
            player2.x -= 13

        elif player.x < 50 and player2.x + 100 < 1270 and keys[pygame.K_a]:
            Background_placement += 13
            player2.x += 13

        elif player2.x + 100 > 1270 and player.x > 50 and keys[pygame.K_RIGHT]:
            Background_placement -= 13
            player.x -= 13

        elif player2.x < 50 and player.x +100 < 1270 and keys[pygame.K_LEFT]:
            Background_placement += 13
            player.x += 13


        #========================Collision=============================

        if player.y < randheight + Platform.get_height() and player.x < randwidth + Platform.get_width() and player.x > randwidth:
            #Penguin_topleft < randheight + Platform.get_height() and Penguin_topleft < randwidth + Platform.get_width() and Penguin_topleft > randwidth and Penguin_topright > randheight + Platform.get_height() and Penguin_topright < randwidth + Platform.get_width() and Penguin_topright > randwidth:

            
            #player.y < randheight + Platform.get_height() and player.y > randheight and player.x > randwidth and player.x < randwidth + Platform.get_width() and player.x + Penguin.get_width() > randwidth and player.x + Penguin.get_width() < randwidth :
            player.y = randheight + Platform.get_height() + 5
            jumpCount = -5
            print("collision detected")

            if player.x == 500 + Platform.get_width():
                player_velocity = 0

        elif player.y < randheight + Platform.get_height() and player.x + Penguin.get_width() < randwidth + Platform.get_width() and player.x + Penguin.get_width() > randwidth:
            
            player.y = randheight + Platform.get_height() + 5
            jumpCount = -5
            print("collision detected")

            if player.x == 500 + Platform.get_width(): player_velocity = 0





        if player.y > 545:
            player.y = 545



        screen.blit(Platform, (randwidth, randheight))
        screen.blit(Platform, (randwidth2, randheight2))






        
        
















properties()
pygame.quit()