import pygame
from pygame.locals import *

class Joueur:
    def __init__(self, nom, pos, fenetre):
        self.nom = nom
        self.pos = list(pos)
        self.fenetre = fenetre

    def affiche(self, nom, pos):
        image = pygame.image.load(f"images/{nom}").convert()
        x, y = pos
        self.fenetre.blit(image, (64+x*32, 64+y*32))

    def afficheAll(self):
       self.affiche(self.nom, self.pos)

    def reset(self):
        self.pos = list((1, 1))

    def getPos(self):
        return self.pos 
    
    def deplacement(self, x, y):
       self.pos[0] += x
       self.pos[1] += y
