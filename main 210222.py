import pygame
import os  
import random
import math
import time
from Player import Player
from Platform import Platform
from Hole import Hole
from Game import Game




#Initalize the game and its properties
pygame.font.init()
pygame.init()



Width, Height = (1280, 720)
pygame.display.set_caption("Cave Fighters")
screen = pygame.display.set_mode((Width, Height))
Platform_placement = 0




# Loading Images/Sprites
Winner1 = pygame.transform.scale(pygame.image.load("Assets/Winner1.png"), (Width, Height))
Winner2 = pygame.transform.scale(pygame.image.load("Assets/Winner2.png"), (Width, Height))
Background = pygame.transform.scale(pygame.image.load("Assets/BAckground.png"), (Width, Height))
Background = pygame.transform.flip(Background, True, False)
Background2 = pygame.transform.scale(pygame.image.load("Assets/BAckground.png"), (Width, Height))
Background2 = pygame.transform.flip(Background2, True, False)
Background3 = pygame.transform.scale(pygame.image.load("Assets/BAckground.png"), (Width, Height))
Background3 = pygame.transform.flip(Background3, True, False)
HolePit = pygame.transform.scale(pygame.image.load("Assets/HolePit.png"), (Width, Height))

Floor = pygame.image.load("Assets/Floor.png")



Fog = pygame.transform.scale(pygame.image.load("Assets/fog.png"), (Width, Height))

Torch = pygame.image.load("Assets/Torch.png")
Torch = pygame.transform.scale(pygame.image.load("Assets/Torch.png"), (350, 350))

pygame.mixer.music.load("Assets/Background.mp3") 
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.01)

player = Player(1, 550, 545, 1030, "Blue", "WASD", "HUDBlue")
player2 = Player(2, 700, 545, 100, "Lilac", "LRUD", "HUDPurple")
Floorect = pygame.Rect(0, 700 , 1280, 100)

Game = Game(player, player2, Floorect)

global Planks_Boltzman_constant 
Planks_Boltzman_constant = 1

Game.PlatformGeneration()
Game.HoleGeneration()
Game.HoleArray[0].x = 0
Game.HoleArray[0].width = Width


FirstPlat = Game.PlatformArray[0].x

global Clock
Clock = 1





def Void():
    screen.blit(HolePit, (0, 0))

def Timer(Clocky):
    Clocky += 1



def properties():
    run = True
    FPS = 300

    
    lives = 5


    clock = pygame.time.Clock()




    Direction = 1





        # Player positions

    Background_placement = 0
    Platform_placement = 0

    







    def game():

        global Clock



        # Placing the images in the game 
        

        
        screen.blit(Torch, (player.x - 120 , player.y - 120 ))
        screen.blit(Torch, (player2.x - 120 , player2.y - 120 ))

        Game.Death(screen)
        
        player.draw(screen)
        player2.draw(screen)

        # for i in range(len(Game.PlatformArray)):
        #     Game.PlatformArray[i].RenderPlatform(screen)

        for platform in Game.PlatformArray:
            platform.RenderPlatform(screen)
            platform.CoordsCalculation()
            
        for hole in Game.HoleArray:
            hole.RenderHole(screen)
            hole.CoordsCalculation()

        Void()


        player.CoordsCalculationP()
        player2.CoordsCalculationP()



        print(Game.HoleArray[len(Game.HoleArray) - 1].x)        

        if player.x < 0 or player.y > 720:
            screen.blit(Winner2, (0, 0))
            player.x = -200
            if Clock < 5:
                Clock += 1
                print (Clock)
            else:
                time.sleep(3)
                Clock += 1


        if player2.x < 0 or player2.y > 720:
            screen.blit(Winner1, (0,0))
            
            if Clock < 5:
                Clock += 1
                print (Clock)
            else:
                time.sleep(3)
                Clock += 1












        # Flip the display
        pygame.display.flip()
        pygame.display.update()




    while run:

        global Planks_Boltzman_constant
        global Clock

        clock.tick(FPS)
        
        game()

        Game.PlatformCheck(screen, player, player2, Floorect)
        Game.HoleCheck(screen)

        # Checks if the user clicked the close button, if so end loop/ close game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or Clock > 5:
                run = False


          
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and player.is_jump == False:
                    
                    player.direction.y = player.jump_count
                    player.is_jump = True
                    
                if event.key == pygame.K_UP and player2.is_jump == False:
                    
                    player2.direction.y = player2.jump_count
                    player2.is_jump = True
                                                            




        



        player.movement(screen)
        player2.movement(screen)
        player.Gravity()
        player2.Gravity()


        # for i in Platforms:

        #     if Platform_Number == Array_Number:
        #         i = Platform()
        #         i.CreatePlatform(screen)
        #         print (i.x)

        #     else:
        #         Array_Number = Array_Number + 1
        #         print(Array_Number, Platform_Number)

                
        # if Platform_placement != 0 and Platform_placement % 100 == 0 and Platform_placement != Platforms:
        #     Platforms.append(Platform_placement)
        #     Platforms.sort()
        #     Platform_Number = Platform_Number + 1 
        #     print(Platforms)

       


        


        keys = pygame.key.get_pressed()



 






        #========================Parallax Background=============================

    
        screen.blit(Background, (Background_placement, 0))
        screen.blit(Background2, (Background_placement + 1270, 0))
        screen.blit(Background3, (Background_placement - 1270, 0))

        if Background_placement - 1450 < -2720:
            Background_placement = 0

        elif Background_placement > 1270:
            Background_placement = 0



        Background_placement -= (player.velocity - 10)+Planks_Boltzman_constant

        player.x -= (player.velocity - 10)
        player2.x -= (player.velocity - 10)
        


        for platform in Game.PlatformArray:
            platform.x -= (player.velocity - 10)+Planks_Boltzman_constant
            platform.toprightx -= player.velocity

        for hole in Game.HoleArray:
            hole.x -= (player.velocity - 10)+Planks_Boltzman_constant


        if Planks_Boltzman_constant:
            Planks_Boltzman_constant = Planks_Boltzman_constant + 0.01




        # if player.x + 100 > 1270 and player2.x > 50 and keys[player.right_key]:
        #     Background_placement -= player.velocity
        #     player2.x -= player.velocity
        #     # for i in range(len(Game.PlatformArray)):
        #     #     Game.PlatformArray[i].x -= player.velocity
        #     #     Game.PlatformArray[i].toprightx -= player.velocity

        #     for platform in Game.PlatformArray:
        #         platform.x -= player.velocity
        #         platform.toprightx -= player.velocity


            

        # elif player.x < 50 and player2.x + 100 < 1270 and keys[player.left_key] and Game.PlatformArray[0].toprightx < FirstPlat:
        #     Background_placement += player.velocity
        #     Platform_placement = Platform_placement + player.velocity
        #     player2.x += player.velocity

        #     for platform in Game.PlatformArray:
        #         platform.x += player.velocity
        #         platform.toprightx += player.velocity



        # elif player2.x + 100 > 1270 and player.x > 50 and keys[player2.right_key]:
        #     Background_placement -= player.velocity
        #     Platform_placement = Platform_placement - player.velocity
        #     player.x -= player.velocity

        #     for platform in Game.PlatformArray:
        #         platform.x -= player.velocity
        #         platform.toprightx -= player.velocity


        # elif player2.x < 50 and player.x + 100 < 1270 and keys[player2.left_key] and Game.PlatformArray[0].x < FirstPlat:
        #     Background_placement += player.velocity
        #     Platform_placement = Platform_placement + player.velocity
        #     player.x += player.velocity

        #     for platform in Game.PlatformArray:
        #         platform.x += player.velocity
        #         platform.toprightx += player.velocity



        # #=======================Collision==============================




        # player.player_collision(Game.PlatformArray)




        # if player.y < randheight + Platform.get_height() and player.x < randwidth + Platform.get_width() and player.x > randwidth:
        #     #Penguin_topleft < randheight + Platform.get_height() and Penguin_topleft < randwidth + Platform.get_width() and Penguin_topleft > randwidth and Penguin_topright > randheight + Platform.get_height() and Penguin_topright < randwidth + Platform.get_width() and Penguin_topright > randwidth:

            
        #     #player.y < randheight + Platform.get_height() and player.y > randheight and player.x > randwidth and player.x < randwidth + Platform.get_width() and player.x + player.image.get_width() > randwidth and player.x + player.image.get_width() < randwidth :
        #     player.y = randheight + Platform.get_height() + 5
        #     player.jumpCount = -5
        #     print("collision detected")

        #     if player.x == 500 + Platform.get_width():
        #         player_velocity = 0

        # elif player.y < randheight + Platform.get_height() and player.x + player.image.get_width() < randwidth + Platform.get_width() and player.x + player.image.get_width() > randwidth:
            
        #     player.y = randheight + Platform.get_height() + 5
        #     player.jumpCount = -5
        #     print("collision detected")

        #     if player.x == 500 + Platform.get_width(): player_velocity = 0






    
    
















properties()
pygame.quit()