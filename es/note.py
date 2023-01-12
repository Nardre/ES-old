# import
import pygame
from pygame.locals import *

# initialisation
height, width = 1200, 1920

# color
black = (0, 0, 0)
white = (255, 255, 255)
grey = (127, 127, 127)
red = (255, 0, 0)
blue = (0, 0, 255)

# fenetre
pygame.init()
fenetre = pygame.display.set_mode(height, width))
pygame.display.set_caption('ray')

# boucle infini
continuer = True
while continuer:
    for event in pygame.event.get():    
        if event.type == QUIT:
            continuer = False 
            
# quit
pygame.quit()

# sprite
{self} = pygame.image.load("{self}.jpeg").convert()
{self}_position = {self}.get_rect()
{self}_position = position_{self}.move({x}, {y}) 

# texte
{self}_font= pygame.font.SysFont('mono', 25)
{self}_text = {self}_font.render("{texte}", True, ({r}, {g}, {b}), ({r}, {g}, {b})

#affichage
fenetre.blit({self}, {self_position})
pygame.draw.rect(fenetre, ({r}, {g}, {b}), {rect})
{}.fill({r}, {g}, {b})
pygame.display.flip()
circle(surface, color, center, radius, width=0, draw_top_right=None, draw_top_left=None, draw_bottom_left=None, draw_bottom_right=None)


#auto
AUTO{SELF} = USEREVENT + 1
pygame.time.set_timer(AUTO{SELF}, {ms})
if event.type == AUTO{SELF}:
    
#collision
if pygame.Rect.colliderect({self}_position, {self}_position):

# Déplacement maintenue
pygame.key.set_repeat(400, 30) 

# keyboard
if event.type == KEYDOWN :                            
    if event.key == K_{self}:

#Déplacement maintenue
pygame.key.set_repeat(400, 30) 

#redimensoiner 
picture = pygame.transform.scale(picture, (picture.get_rect().size[0]//2, picture.get_rect().size[1]//2))

#souris
if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and event.pos[0] < {x} and event.pos[0] > {x} and event.pos[1] < {y} and event.pos[1] > {y}:
pygame.mouse.get_pos()
