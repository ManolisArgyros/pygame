# ΜΑΘΗΜΑ 8: Εχθρός και Game Over
# Τι θα μάθουμε: κινούμενος εχθρός, colliderect, κατάσταση παιχνιδιού (game_active)

import os
import pygame
from sys import exit

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Απόφυγε το σκαθάρι')
clock = pygame.time.Clock()

sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

player = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom=(80, 300))
player_gravity = 0

snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(bottomleft=(800, 300))

# Μεταβλητή-διακόπτης: True = παίζουμε, False = χάσαμε
game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_active and player_rect.bottom >= 300:
                player_gravity = -20
            elif not game_active:           # χάσαμε και πατάμε SPACE: ξαναρχίζουμε
                game_active = True
                snail_rect.left = 800

    if game_active:
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 300))

        # Ο εχθρός πηγαίνει αριστερά. Όταν βγει από την οθόνη, ξαναμπαίνει από δεξιά.
        snail_rect.x -= 6
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail, snail_rect)

        # Παίκτης
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player, player_rect)

        # Άγγιξαν τα δύο ορθογώνια;
        if player_rect.colliderect(snail_rect):
            game_active = False
    else:
        screen.fill('red')      # οθόνη Game Over

    pygame.display.update()
    clock.tick(60)


# ΔΟΚΙΜΑΣΕ ΜΟΝΟΣ ΣΟΥ
# 1. Κάνε το σκαθάρι πιο γρήγορο (το 6). Πόσο γρήγορο μπορείς να το παίξεις;
# 2. Άλλαξε το χρώμα της οθόνης Game Over.
# 3. Αντικατέστησε τον εχθρό με τη νυχτερίδα (Fly1.png) και τοποθέτησέ την ψηλά (bottomleft=(800, 210)).
