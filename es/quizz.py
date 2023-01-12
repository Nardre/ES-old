import pygame
from pygame.locals import *

class Quizz:
    def __init__(self, fenetre, question, listCase):
        self.fenetre = fenetre
        self.listCase = listCase
        self.font = pygame.font.SysFont('mono', 20)
        self.question = question

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

    def affiche(self, nom, pos):
        image = pygame.image.load(f"images/{nom}").convert_alpha()
        self.fenetre.blit(image, pos)

    def afficheAll(self):
        # texte
        for i in range(len(self.question)):
            texte = self.font.render(self.question[i], True, self.black, self.white)
            self.fenetre.blit(texte, (300, 100 + i*20))

        for i in range(3):
            bouton, textes = self.listCase[i]
            bouton.afficheAll()

            # texte
            for i in range(len(textes[0])):
                xpos, ypos = textes[-1]
                texte = self.font.render(textes[0][i], True, self.black, self.white)
                self.fenetre.blit(texte, (xpos+64, ypos+(i*20)))
