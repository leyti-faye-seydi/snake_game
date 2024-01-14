import pygame
import sys
import random
import time

pygame.init()

# Initialiser pygame
largeur_fenetre = 800
hauteur_fenetre = 600
taille_bloc = 20
distance_collision = 10
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu de serpent")
police = pygame.font.Font(None, 25)

# Définition des couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)

# Defintion du menu de jeu
def menu():
    ecrire_nom_jeu = police.render("Jeu de serpent", True, noir)
    ecrire_jouer = police.render("1 - commencer le jeu", True, noir)
    ecrire_option = police.render("2 - Options", True, noir)
    ecrire_quitter = police.render("3 - Quitter", True, noir)

    fenetre.blit(ecrire_nom_jeu, (300, 50))
    fenetre.blit(ecrire_jouer, (300, 200))
    fenetre.blit(ecrire_option, (300, 250))
    fenetre.blit(ecrire_quitter, (300, 300))

def option():
    print("Les options du jeu")

# Definition du jeu
def jeu():
    # Declaration des objets necessaire pou, le jeu
    serpent = [[100, 50], [90, 50], [80, 50]]
    direction = 'RIGHT'
    changement_direction = direction
    nourriture = [random.randrange(1, (largeur_fenetre//taille_bloc)) * taille_bloc,
                  random.randrange(1, (hauteur_fenetre//taille_bloc)) * taille_bloc ]
    score = 0
    niveau = 1
    vitesse_serpent = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                # Deplacement du serpent
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    changement_direction = 'LEFT' # vers la gauche
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    changement_direction = 'RIGHT' # vers la droite
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    changement_direction = 'UP' #vers le haut
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    changement_direction = 'DOWN' #vers le bas
            direction = changement_direction

        # Verifier que le reste du serpent suive la tete
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

        # Verification de la collision du serpent avec la nourriture
        if (serpent[0][0] + distance_collision >= nourriture[0] >= serpent[0][0] - distance_collision and serpent[0][1] + distance_collision >= nourriture[1] >= serpent[0][1] - distance_collision):
            score += 1
            nourriture = [random.randrange(1, (largeur_fenetre//taille_bloc)) * taille_bloc,
                  random.randrange(1, (hauteur_fenetre//taille_bloc)) * taille_bloc ]
            serpent.append([0, 0])




        fenetre.fill(blanc)

        # dessin du serpent et de la nourriture
        for segment in serpent:
            pygame.draw.rect(fenetre, noir, [segment[0], segment[1], taille_bloc, taille_bloc])
        pygame.draw.rect(fenetre, rouge, [nourriture[0], nourriture[1], taille_bloc, taille_bloc])

        #calcule de score, augmentation de la vitesse du serpent et du niveau
        if score == 10 :
            niveau += 1
            score = 0
            vitesse_serpent += 5

        # ecriture du score
        font = pygame.font.SysFont(None, 25)
        score_text = font.render("score: " + str(score), True, noir)
        fenetre.blit(score_text, [10, 10])

        # ecriture du niveau
        font = pygame.font.SysFont(None, 25)
        niveau_text = font.render("niveau: " + str(niveau), True, noir)
        fenetre.blit(niveau_text, [100, 10])

        # Reprise du jeu quand le serpent sortira de la fenetre de jeu
        if serpent[0][0] >= largeur_fenetre or serpent[0][0] < 0 or serpent[0][1] >= hauteur_fenetre or serpent[0][1] < 0:
            menu()


        for segment in serpent[1:]:
            if serpent[0] == segment:
                menu()

        pygame.display.update()
        time.sleep(1/vitesse_serpent)

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 300 <= x <= 500 and 200 <= y <= 230:  # Zone du bouton "Commencer le jeu"
                jeu()
            elif 300 <= x <= 500 and 250 <= y <= 280:  # Zone du bouton "Options"
                afficher_options()
            elif 300 <= x <= 500 and 300 <= y <= 330:  # Zone du bouton "Quitter"
                pygame.quit()
                sys.exit()
    fenetre.fill(noir)
    menu()
    pygame.display.flip()