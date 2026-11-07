# ΜΑΘΗΜΑ 5: Εικόνες (sprites)
# Τι θα μάθουμε: φόρτωση εικόνων, blit, σειρά ζωγραφικής
# Από εδώ και πέρα χρειαζόμαστε τους φακέλους graphics, audio, font δίπλα στο αρχείο.

import os
import pygame
from sys import exit

# Το πρόγραμμα βρίσκει τους φακέλους ό,τι κι αν είναι το "τρέχον" μέρος που το ξεκίνησες
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Εικόνες')
clock = pygame.time.Clock()

# Μια εικόνα που τη βάζουμε στην οθόνη λέγεται Surface.
# convert()       -> για εικόνες χωρίς διαφάνεια (φόντο)
# convert_alpha() -> για εικόνες με διαφανές φόντο (παίκτης, εχθροί)
sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()
player = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
fly = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # blit(εικόνα, (x, y)): το (x, y) είναι η ΠΑΝΩ-ΑΡΙΣΤΕΡΑ γωνία της εικόνας.
    # Η σειρά μετράει: ό,τι ζωγραφίζουμε μετά, μπαίνει ΠΑΝΩ από τα προηγούμενα.
    screen.blit(sky, (0, 0))        # 
    screen.blit(ground, (0, 300))   # το έδαφος ξεκινάει στο y = 300
    screen.blit(player, (80, 216))  # 
    screen.blit(snail, (500, 264))  # 
    screen.blit(fly, (300, 150))

    pygame.display.update()
    clock.tick(60)


# ΔΟΚΙΜΑΣΕ ΜΟΝΟΣ ΣΟΥ
# 1. Φόρτωσε και δεύτερο σαλιγκάρι (snail2.png) και βάλ' το δίπλα στο πρώτο.
