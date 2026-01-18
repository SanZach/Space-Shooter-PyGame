import pygame
from random import randint

#general setup
pygame.init()  #important initialize module
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #display surface
pygame.display.set_caption('Space Shooter by SanZ')
running= True

#plain surface
Psurface = pygame.Surface((100,200))
Psurface.fill('blue')
X= 100
#player sprite
player = pygame.image.load('images/player.png').convert_alpha()
#star sprite
star = pygame.image.load('images/star.png').convert_alpha()
star_pos = [(randint(0,SCREEN_WIDTH),randint(0,SCREEN_HEIGHT)) for i in range(20)]  #generate 20 star positions

while running:
    for event in pygame.event.get():   #event loop
        if event.type== pygame.QUIT:
            running= False   #closable window made
    #drawing the game elements
    screen.fill('midnight blue')
    for position in star_pos:
        screen.blit(star, position)
    X += 0.1
    screen.blit(player,(X,150))
    pygame.display.update()    #or update/flip except flip can specify updating a part of window  



pygame.quit()  #uninitializes the pygame initialization - important for closing properly and avoiding backward behaviour by pygame