# ΜΑΘΗΜΑ 9: Μουσική και ήχοι
# Τι θα μάθουμε: pygame.mixer.music (μουσική υπόβαθρου), Sound (ηχητικά εφέ)

import os
import pygame
from sys import exit

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Ήχοι')
clock = pygame.time.Clock()

# ΜΟΥΣΙΚΗ: ένα μεγάλο κομμάτι που παίζει στο υπόβαθρο
pygame.mixer.music.load('audio/music.wav')
pygame.mixer.music.set_volume(0.3)     # ένταση από 0 (σιωπή) έως 1 (μέγιστη)
pygame.mixer.music.play(-1)            # -1 = ξαναπαίζει για πάντα

# ΕΦΕ: μικροί ήχοι που παίζουν όταν γίνεται κάτι
jump_sound = pygame.mixer.Sound('audio/jump.mp3')
jump_sound.set_volume(0.5)
hit_sound = pygame.mixer.Sound('audio/hit.wav')

sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

player = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom=(80, 300))
player_gravity = 0

snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(bottomleft=(800, 300))

game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_active and player_rect.bottom >= 300:
                player_gravity = -20
                jump_sound.play()           # ήχος άλματος
            elif not game_active:
                game_active = True
                snail_rect.left = 800

    if game_active:
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 300))

        snail_rect.x -= 6
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player, player_rect)

        if player_rect.colliderect(snail_rect):
            hit_sound.play()                # ήχος σύγκρουσης
            game_active = False
    else:
        screen.fill('red')

    pygame.display.update()
    clock.tick(60)


# ΔΟΚΙΜΑΣΕ ΜΟΝΟΣ ΣΟΥ
# 1. Άλλαξε την ένταση της μουσικής (set_volume) σε 0 και σε 1.
# 2. Βάλε δικό σου αρχείο ήχου στον φάκελο audio και παίξε το (.wav ή .mp3).
# 3. Σταμάτησε τη μουσική όταν χάνεις: pygame.mixer.music.stop()
#    Και ξαναξεκίνα την όταν ξαναρχίζεις το παιχνίδι.
