# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
import math


def Julia((x,y)):
   i=1
   r=0
   x1=x
   y1=y
   while((i<100) and(r<4)):
      x=x1*x1-y1*y1+xc
      y=2*x1*y1+yc
      x1=x
      y1=y
      r=(x*x+y*y)
      i=i+1
   if (i>98):
      return(200)
   else:
      if (5*i)>255:
         c=255
      else:
         c=5*i
      return(c)

def Coord((x,y)):
   xcal=0.5*largeur*(x-xcentre)/(xfen-xcentre)+xcen
   ycal=0.5*hauteur*(y-ycentre)/(yfen-ycentre)+ycen
   return((xcal,ycal))   
      





xfen=800
yfen=600
xcen=0.0
ycen=0.0
largeur=2.0
hauteur=2.0

#xc=input("L'abcisse de c est:")
xc=0.3
yc=0.2
#yc=input("L'ordonnée de c est:")
xcentre=400
ycentre=300
pygame.init()
#Ouverture de la fenêtre 
fenetre = pygame.display.set_mode((xfen, yfen))
#Chargement et collage du fond
fond = pygame.image.load("FondJulia.jpg").convert()
fenetre.blit(fond, (0,0))
#Centre de l'image- le zéro- à(405,300)
#Rafraîchissement de l'écran
pygame.display.flip()

cont=1
while cont:
   for x in range(xfen):
        for y in range(yfen):
            couleur=Julia(Coord((x,y)))
            fond.set_at((x, y),(couleur, 23, 23)) #Affiche un pixel à l'adresse (x;y)
        fenetre.blit(fond, (0,0))	
   
   pygame.display.flip()
         
   continuer=1
   while continuer:
       for event in pygame.event.get():    #Attente des événements
           if event.type == QUIT:
               cont = 0
               continuer=0
           if event.type ==   (MOUSEMOTION and MOUSEBUTTONDOWN):
               x1 = event.pos[0]
               y1 = event.pos[1]#On affiche le rectangle de sélection
               rectangle(fenetre,rect((x0,y0),(x1,y1)),(0,255,255))
                 
           if event.type == MOUSEBUTTONUP:
               if event.button == 1:   #Si clic gauche
                 x1 = event.pos[0]
                 y1 = event.pos[1]
                 continuer=0
                 (x0,y0)=Coord((x0,y0))
                 (x1,y1)=Coord((x1,y1))
                 largeur=abs(x1-x0)
                 hauteur=abs(y1-y0)
                 xcen=min(x0,x1)+largeur/2
                 ycen=min(y0,y1)+hauteur/2
           if event.type == MOUSEBUTTONDOWN:
               if event.button == 3:   #Si clic droit
                  xcen=0.0
                  ycen=0.0
                  largeur=2.0
                  hauteur=2.0
                  continuer=0
               if event.button == 1:   #Si clic gauche
                   #On change les coordonnées de la fenêtre de calcul
                      if continuer == 1:
                          x0 = event.pos[0]
                          y0 = event.pos[1]
                          continuer=2
 #     fenetre.blit(fond, (0,0))	
#     fenetre.blit(perso, (perso_x, perso_y))
	#Rafraichissement
#      pygame.display.flip()
  
pygame.quit()

