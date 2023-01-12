import pygame
from pygame.locals import *

class Carte:
    def __init__(self, nom, fenetre):
        self.carte = []
        self.fenetre = fenetre
        self.arbreList = []

        with open("images/"+nom, "r+") as file:
            for line in file:
                self.carte += [line]
        
        for i in range(len(self.carte)):
            for y in range(len(self.carte[i])):
                if self.carte[i][y] == "A":
                    self.arbreList += [(i, y)]
        
    def affiche(self, nom, pos):
        image = pygame.image.load(f"images/{nom}").convert()
        y, x = pos
        self.fenetre.blit(image, (64+x*32, 64+y*32))


    def afficheAll(self):
        for pos in self.arbreList:
            self.affiche("arbre.xcf", pos)

    def estLibre(self, pos):
        y, x = pos
        return self.carte[x][y] == " "


    
