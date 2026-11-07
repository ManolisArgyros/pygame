# ΜΑΘΗΜΑ 7: Άλμα και βαρύτητα
# Τι θα μάθουμε: γεγονός πλήκτρου (KEYDOWN), βαρύτητα, έδαφος

import os
import pygame
from sys import exit

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Άλμα')
clock = pygame.time.Clock()

sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

player_right = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_left = pygame.transform.flip(player_right, True, False)
player = player_right
player_rect = player.get_rect(midbottom=(80, 300))
player_gravity = 0     # πόσο γρήγορα πέφτει (αρνητικό = πάει ?)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # KEYDOWN: συμβαίνει ΜΙΑ φορά τη στιγμή που πατάς το πλήκτρο
        # (διαφορετικό από το get_pressed που ελέγχει αν το κρατάς πατημένο)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if player_rect.bottom >= 300:     # μόνο αν πατάει στο έδαφος (όχι διπλό άλμα)
                player_gravity = -20          # δυνατή ώθηση προς τα ΠΑΝΩ (το y μειώνεται)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
        player = player_right
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
        player = player_left
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > 800:
        player_rect.right = 800

    # ΒΑΡΥΤΗΤΑ: σε κάθε καρέ η ταχύτητα προς τα κάτω αυξάνεται κατά 1.
    # Στην αρχή του άλματος πάμε πάνω γρήγορα (-20), μετά όλο και πιο αργά,
    # μετά σταματάμε στην κορυφή, και μετά πέφτουμε όλο και πιο γρήγορα.
    player_gravity += 1
    player_rect.y += player_gravity

    # Το έδαφος μάς σταματάει
    if player_rect.bottom >= 300:
        player_rect.bottom = 300

    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 300))
    screen.blit(player, player_rect)

    pygame.display.update()
    clock.tick(60)


# ΔΟΚΙΜΑΣΕ ΜΟΝΟΣ ΣΟΥ
# 1. Άλλαξε το -20 σε -30. Τι γίνεται; Και σε -10;
# 2. Άλλαξε το += 1 της βαρύτητας σε += 2. Σαν να είσαι σε άλλο πλανήτη
# 3. Φτιάξε "διπλό άλμα": επέτρεψε άλμα και στον αέρα (βγάλε τον έλεγχο του εδάφους).
