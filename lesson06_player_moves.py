# ΜΑΘΗΜΑ 6: Ο παίκτης περπατάει
# Τι θα μάθουμε: get_rect, midbottom, κίνηση sprite, καθρέφτης εικόνας (flip)

import os
import pygame
from sys import exit

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Ο παίκτης κινείται')
clock = pygame.time.Clock()

sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

player_right = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_left = pygame.transform.flip(player_right, True, False)   # καθρέφτης (οριζόντια)

player = player_right                                            

# get_rect: φτιάχνει το ορθογώνιο της εικόνας, ώστε να ξέρουμε πού βρίσκεται.
# midbottom = (80, 300): 
# το ΜΕΣΑΙΟ-ΚΑΤΩ σημείο του παίκτη είναι στο (80, 300), 
# δηλαδή πατάει στο έδαφος.
player_rect = player.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
        player = player_right       # κοιτάει δεξιά
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
        player = player_left        # κοιτάει αριστερά

    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > 800:
        player_rect.right = 800

    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 300))
    screen.blit(player, player_rect)    # μπορούμε να δώσουμε το rect στη θέση του (x, y)

    pygame.display.update()
    clock.tick(60)


# ΔΟΚΙΜΑΣΕ ΜΟΝΟΣ ΣΟΥ
# 1. Κάνε τον παίκτη να τρέχει πιο γρήγορα.
# 2. Άλλαξε το midbottom σε center. Τι διαφορά βλέπεις στη θέση του;
# 3. Βάλε τον παίκτη να ξεκινάει από το δεξί μέρος της οθόνης.
