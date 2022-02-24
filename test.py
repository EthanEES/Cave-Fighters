import pygame


pygame.font.init()
pygame.init()






def properties():
    run = True
    main_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 20)

    Width, Height = (1280, 720)
    pygame.display.set_caption("Ice Cave")
    screen = pygame.display.set_mode((Width, Height))


    def game():

        pygame.display.flip()
        pygame.display.update()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False





















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
        self.HUD = pygame.transform.scale(pygame.image.load(f"Assets/Penguins/{color}.png"), (120, 150))
        self.max_health = health
        self.velocity = 15 
        self.topleft = x
        self.topright = x + self.image.get_width()
        self.bottomright = self.topright + int(self.image.get_height())
        self.bottomleft = y + self.image.get_height()

        self.left_key = pygame.K_a
        self.right_key = pygame.K_d
        self.up_key = pygame.K_w
        self.down_key = pygame.K_s
        self.jump_key = pygame.K_SPACE
        self.jump_count = 10
        self.is_jump = False
































    def FirstPlatformGenerations(self):
        for x in range(0, 3):
            x = Platform()
            x.x = random.randint(0, 1000)
            self.PlatformArray.append(x)
            




































properties()
