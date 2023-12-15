import pygame
import random
import time

pygame.init()


largeur_fenetre = 800
hauteur_fenetre = 600
taille_bloc = 20
vitesse_serpent = 10
distance_collision = 10


blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu de serpent")

def jeu():
    serpent = [[100, 50], [90, 50], [80, 50]]
    direction = 'RIGHT'
    changement_direction = direction
    nourriture = [random.randrange(1, (largeur_fenetre//taille_bloc)) * taille_bloc,
                  random.randrange(1, (hauteur_fenetre//taille_bloc)) * taille_bloc ]
    score = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    changement_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    changement_direction = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    changement_direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    changement_direction = 'DOWN'
            direction = changement_direction


        if direction == 'RIGHT':
            for i in range(len(serpent)-1, 0, -1):
                serpent[i] = list(serpent[i-1])
            serpent[0][0] += taille_bloc
        elif direction == 'LEFT':
            for i in range(len(serpent)-1, 0, -1):
                serpent[i] = list(serpent[i-1])
            serpent[0][0] -= taille_bloc
        elif direction == 'UP':
            for i in range(len(serpent)-1, 0, -1):
                serpent[i] = list(serpent[i-1])
            serpent[0][1] -= taille_bloc
        elif direction == 'DOWN':
            for i in range(len(serpent)-1, 0, -1):
                serpent[i] = list(serpent[i-1])
            serpent[0][1] += taille_bloc


        if (serpent[0][0] + distance_collision >= nourriture[0] >= serpent[0][0] - distance_collision and serpent[0][1] + distance_collision >= nourriture[1] >= serpent[0][1] - distance_collision):
            score += 1
            nourriture = [random.randrange(1, (largeur_fenetre//taille_bloc)) * taille_bloc,
                  random.randrange(1, (hauteur_fenetre//taille_bloc)) * taille_bloc ]
            serpent.append([0, 0])



        if serpent[0][0] >= largeur_fenetre or serpent[0][0] < 0 or serpent[0][1] >= hauteur_fenetre or serpent[0][1] < 0:
            jeu()


        for segment in serpent[1:]:
            if serpent[0] == segment:
                jeu()

        fenetre.fill(blanc)
        for segment in serpent:
            pygame.draw.rect(fenetre, noir, [segment[0], segment[1], taille_bloc, taille_bloc])
        pygame.draw.rect(fenetre, rouge, [nourriture[0], nourriture[1], taille_bloc, taille_bloc])

        font = pygame.font.SysFont(None, 25)
        score_text = font.render("score: " + str(score), True, noir)
        fenetre.blit(score_text, [10, 10])

        pygame.display.update()
        time.sleep(1/vitesse_serpent)

jeu()